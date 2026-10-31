import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sounddevice as sd

class FourierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador y Visualizador de Formas de Onda - Serie de Fourier")
        self.root.geometry("1000x700")
        
        # Configurar color de fondo general de la ventana (Azul Marino Oscuro)
        self.root.configure(bg="#0a192f")
        
        # Aplicar estilo oscuro a los widgets ttk
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('.', background='#0a192f', foreground='#e2e8f0', fieldbackground='#172a45')
        style.configure('TLabel', background='#0a192f', foreground='#e2e8f0', font=('Arial', 10))
        style.configure('TLabelFrame', background='#0a192f', foreground='#64ffda', font=('Arial', 10, 'bold'))
        style.configure('TLabelFrame.Label', background='#0a192f', foreground='#64ffda')
        style.configure('TRadiobutton', background='#0a192f', foreground='#e2e8f0', font=('Arial', 10))
        style.map('TRadiobutton', background=[('active', '#0a192f'), ('selected', '#0a192f')], foreground=[('active', '#64ffda')])
        style.configure('TButton', background='#172a45', foreground='#64ffda', font=('Arial', 10, 'bold'), borderwidth=1)
        style.map('TButton', background=[('active', '#233554')])

        # Variables de control
        self.wave_type = tk.StringVar(value="Senoidal")
        self.n_terms = tk.IntVar(value=5)
        self.amplitude = tk.DoubleVar(value=0.5)
        self.frequency = tk.DoubleVar(value=440.0)
        self.is_playing = False
        
        # Fase para la onda viajera
        self.phase = 0.0
        
        # Configuración del flujo de audio único y continuo
        self.fs = 44100
        self.audio_t = 0
        try:
            self.stream = sd.OutputStream(channels=1, callback=self.audio_callback, samplerate=self.fs)
            self.stream.start()
        except Exception:
            self.stream = None

        # Construcción de la Interfaz
        self.create_widgets()
        
        # Bucle de animación protegido
        self.animate()

    def create_widgets(self):
        # ---------------------------------------------------------
        # PARTE SUPERIOR: Panel de Visualización
        # ---------------------------------------------------------
        top_frame = tk.Frame(self.root, bg="#0a192f")
        top_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Gráfica con tema oscuro coherente
        self.fig, self.ax = plt.subplots(figsize=(9, 4.5))
        self.fig.patch.set_facecolor('#0a192f')
        self.ax.set_facecolor('#112240')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=top_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.setup_fixed_plot()

        # ---------------------------------------------------------
        # PARTE INFERIOR: Panel de Control (Distribuido a lo ancho)
        # ---------------------------------------------------------
        bottom_frame = ttk.LabelFrame(self.root, text=" Panel de Control de Onda y Sonido ", padding=15)
        bottom_frame.pack(fill=tk.X, expand=False, padx=15, pady=15)

        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.columnconfigure(1, weight=1)
        bottom_frame.columnconfigure(2, weight=2)

        # --- BLOQUE 1: Selección de Tipo de Onda ---
        block1 = ttk.LabelFrame(bottom_frame, text=" 1. Tipo de Onda ", padding=10)
        block1.grid(row=0, column=0, padx=8, pady=5, sticky="nsew")

        waves = [("Senoidal", "Senoidal"), ("Cuadrada", "Cuadrada"), 
                 ("Diente de sierra", "Diente de sierra"), ("Triangular", "Triangular")]
        for text, val in waves:
            rb = ttk.Radiobutton(block1, text=text, variable=self.wave_type, value=val)
            rb.pack(anchor=tk.W, padx=5, pady=4)

        # --- BLOQUE 2: Número de Términos de la Serie ---
        block2 = ttk.LabelFrame(bottom_frame, text=" 2. Términos de la Serie ", padding=10)
        block2.grid(row=0, column=1, padx=8, pady=5, sticky="nsew")
        
        ttk.Label(block2, text="Armónicos activos:", font=("Arial", 9, "bold")).pack(anchor=tk.W, padx=5, pady=2)
        terms = [5, 10, 15, 20]
        for t in terms:
            btn = ttk.Radiobutton(block2, text=f"{t} Términos", variable=self.n_terms, value=t)
            btn.pack(anchor=tk.W, padx=5, pady=4)

        # --- BLOQUE 3: Parámetros y Reproducción ---
        block3 = ttk.LabelFrame(bottom_frame, text=" 3. Parámetros y Reproducción ", padding=10)
        block3.grid(row=0, column=2, padx=8, pady=5, sticky="nsew")

        # Control de Amplitud
        ttk.Label(block3, text="Amplitud:").pack(anchor=tk.W, padx=5)
        amp_frame = ttk.Frame(block3)
        amp_frame.pack(fill=tk.X, pady=2, padx=5)
        self.amp_slider = ttk.Scale(amp_frame, from_=0.0, to=1.0, variable=self.amplitude, orient=tk.HORIZONTAL)
        self.amp_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.amp_label = ttk.Label(amp_frame, text="0.50", width=5)
        self.amp_label.pack(side=tk.RIGHT, padx=5)
        self.amplitude.trace_add("write", self.update_amp_label)

        # Control de Frecuencia
        ttk.Label(block3, text="Frecuencia (Hz):").pack(anchor=tk.W, padx=5, pady=(5, 0))
        freq_frame = ttk.Frame(block3)
        freq_frame.pack(fill=tk.X, pady=2, padx=5)
        self.freq_slider = ttk.Scale(freq_frame, from_=100.0, to=1000.0, variable=self.frequency, orient=tk.HORIZONTAL)
        self.freq_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.freq_label = ttk.Label(freq_frame, text="440 Hz", width=7)
        self.freq_label.pack(side=tk.RIGHT, padx=5)
        self.frequency.trace_add("write", self.update_freq_label)

        # Botones de Play y Salida
        btn_frame = ttk.Frame(block3)
        btn_frame.pack(fill=tk.X, pady=10, padx=5)
        
        self.play_btn = ttk.Button(btn_frame, text="▶ Play", command=self.toggle_play)
        self.play_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        exit_btn = ttk.Button(btn_frame, text="✖ Salir", command=self.quit_app)
        exit_btn.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))

    def update_amp_label(self, *args):
        val = self.amplitude.get()
        self.amp_label.config(text=f"{val:.2f}")

    def update_freq_label(self, *args):
        val = self.frequency.get()
        self.freq_label.config(text=f"{int(val)} Hz")

    def setup_fixed_plot(self):
        self.ax.set_ylim(-1.2, 1.2)
        self.ax.set_xlim(0, 0.015)
        self.ax.set_ylabel("Amplitud", color="#64ffda", fontsize=10)
        self.ax.set_xlabel("Tiempo (s)", color="#64ffda", fontsize=10)
        self.ax.tick_params(colors="#8892b0", labelsize=9)
        self.ax.spines['bottom'].set_color('#8892b0')
        self.ax.spines['top'].set_color('#8892b0')
        self.ax.spines['left'].set_color('#8892b0')
        self.ax.spines['right'].set_color('#8892b0')
        self.ax.grid(True, linestyle="--", alpha=0.3, color="#8892b0")

    def audio_callback(self, outdata, frames, time_info, status):
        try:
            # Si está pausado, rellenamos con silencio absoluto de manera segura
            if not self.is_playing:
                outdata.fill(0)
                return

            t = (np.arange(frames) + self.audio_t) / self.fs
            self.audio_t += frames
            
            freq = self.frequency.get()
            A = self.amplitude.get()
            w_type = self.wave_type.get()
            N = self.n_terms.get()
            
            phase_signal = 2 * np.pi * freq * t
            audio_wave = np.zeros_like(t)
            
            if w_type == "Senoidal":
                audio_wave = A * np.sin(phase_signal)
            elif w_type == "Cuadrada":
                for n in range(1, N + 1, 2):
                    audio_wave += (4 * A / np.pi) * (1 / n) * np.sin(n * phase_signal)
            elif w_type == "Diente de sierra":
                for n in range(1, N + 1):
                    audio_wave += (2 * A / np.pi) * ((-1)**(n+1) / n) * np.sin(n * phase_signal)
            elif w_type == "Triangular":
                for n in range(1, N + 1, 2):
                    audio_wave += (8 * A / np.pi**2) * ((-1)**((n-1)/2) / n**2) * np.sin(n * phase_signal)

            outdata[:] = audio_wave.reshape(-1, 1)
        except Exception:
            outdata.fill(0)

    def toggle_play(self):
        # Cambio de estado ultraseguro sin destruir el stream de audio
        if not self.is_playing:
            self.is_playing = True
            self.play_btn.config(text="❚❚ Pausa")
            self.audio_t = 0
        else:
            self.is_playing = False
            self.play_btn.config(text="▶ Play")

    def animate(self):
        try:
            if self.is_playing:
                self.phase += 0.15
            
            duration = 0.015
            t = np.linspace(0, duration, 600)
            freq = self.frequency.get()
            A = self.amplitude.get()
            w_type = self.wave_type.get()
            N = self.n_terms.get()
            
            omega = 2 * np.pi * freq
            y = np.zeros_like(t)
            
            if w_type == "Senoidal":
                y = A * np.sin(omega * t + self.phase)
            elif w_type == "Cuadrada":
                for n in range(1, N + 1, 2):
                    y += (4 * A / np.pi) * (1 / n) * np.sin(n * (omega * t + self.phase))
            elif w_type == "Diente de sierra":
                for n in range(1, N + 1):
                    y += (2 * A / np.pi) * ((-1)**(n+1) / n) * np.sin(n * (omega * t + self.phase))
            elif w_type == "Triangular":
                for n in range(1, N + 1, 2):
                    y += (8 * A / np.pi**2) * ((-1)**((n-1)/2) / n**2) * np.sin(n * (omega * t + self.phase))
            
            self.ax.clear()
            self.setup_fixed_plot()
            self.ax.plot(t, y, color='#64ffda', lw=2.2)
            self.ax.set_title(f"Onda: {w_type}  |  Términos: {N}  |  Frecuencia: {int(freq)} Hz", color="#e2e8f0", fontsize=11, fontweight='bold', pad=10)
            self.canvas.draw()
        except Exception:
            pass
        
        self.root.after(30, self.animate)

    def quit_app(self):
        try:
            if self.stream:
                self.stream.stop()
                self.stream.close()
        except:
            pass
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FourierApp(root)
    root.protocol("WM_DELETE_WINDOW", app.quit_app)
    root.mainloop()