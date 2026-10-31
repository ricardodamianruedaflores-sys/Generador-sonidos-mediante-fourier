#Recursividad
"""def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Dame un numero entero: "))
print(f"El factorial de {num} es: {factorial(num)}")

def suma_lista(lista):
    if len(lista) == 0: # Caso base: lista vacía
        return 0
    else: # Caso recursivo
        return lista[0] + suma_lista(lista[1:])

# Ejemplo de uso

print(suma_lista([1, 2, 3, 4, 5])) # Salida: 15

def suma(n):
    if n == 1:
        return 1
    else:
        return n + suma(n-1)
num = int(input("Ingresa un numero natural: "))
print(f"La suma de los primeros {num} numeros naturales es: {suma(num)}")


def atenuacion(señal,factor):
    if señal < 0.5:
        print("Nivel minimo alcanzado, fin de la transmision")
    else:
        print(f"Nivel de la señal {señal} V")
        atenuacion(señal*factor,factor)

nivel_inicial = float(input("Ingresa el valor inicial de la señal: "))
fac_atenuacion = float(input("Ingresa el facyor de atenuacion de la señal: "))
atenuacion(nivel_inicial,fac_atenuacion)

def buscar(lista,elemento):
    if elemento not in lista:
        print(f"El elemento {elemento} no se encuentra en la lista")
    elif elemento == lista[0]:
        print(f"El elemento {elemento} se encuentra en la lista")
    else:
        return buscar(lista[1:],elemento)

datos = [1,2,3,4,5,6,7,8,9,10]
buscar(datos,9)
class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_arista(self, nodo1, nodo2):
        if nodo1 in self.grafo and nodo2 in self.grafo:
            self.grafo[nodo1].append(nodo2)
            self.grafo[nodo2].append(nodo1)

    def mostrar_grafo(self):
        for nodo in self.grafo:
            print(f"{nodo}: {self.grafo[nodo]}")

grafo = Grafo()
grafo.agregar_nodo(1)
grafo.agregar_nodo(2)
grafo.agregar_nodo(3)
grafo.agregar_nodo(4)
grafo.agregar_arista(1,2)
grafo.agregar_arista(1,3)
grafo.agregar_arista(2,4)
grafo.agregar_arista(3,4)
grafo.mostrar_grafo()

import numpy as np # Importamos la librería para manejar matrices
# Definir el número de nodos en el grafo
num_nodos = 4 # Tenemos 4 nodos: A, B, C y D
# Crear una matriz de adyacencia vacía (solo ceros)
matriz_adyacencia = np.zeros((num_nodos, num_nodos), dtype=int)
# Función para agregar conexiones al grafo
def agregar_conexion(matriz, nodo1, nodo2, peso):
    matriz[nodo1][nodo2] = peso
    matriz[nodo2][nodo1] = peso # Si el grafo es no dirigido
# Agregar conexiones con pesos
agregar_conexion(matriz_adyacencia, 0, 1, 5) # A ↔ B (peso 5)
agregar_conexion(matriz_adyacencia, 0, 2, 3) # A ↔ C (peso 3)
agregar_conexion(matriz_adyacencia, 1, 2, 2) # B ↔ C (peso 2)
agregar_conexion(matriz_adyacencia, 1, 3, 1) # B ↔ D (peso 1)
agregar_conexion(matriz_adyacencia, 2, 3, 4) # C ↔ D (peso 4)
#Mostrar la matriz de adyacencia
print("Matriz de Adyacencia con Pesos:")
print(matriz_adyacencia)

from collections import deque
# Representación de un grafo con un diccionario
grafo = {
    'R1':['R2','R3'],
    'R2':['R1','R4','R5'],
    'R3':['R1','R6'],
    'R4':['R2'],
    'R5':['R2','R6'],
    'R6':['R3','R5']
}


def bfs(grafo,inicio):
    visitados = []
    cola = deque([inicio])

    while cola:
        nodo= cola.popleft()
        if nodo not in visitados:
            visitados.append(nodo)
            vecinos = grafo[nodo]
            for vecino in vecinos:
                if vecino not in visitados:
                    cola.append(vecino)
    return visitados

orden = bfs(grafo,'R1')
print("Orden de propagacion de la señal: ",orden)

# Representación de un grafo con un diccionario
grafo = {
    'R1':['R2','R3'],
    'R2':['R1','R4','R5'],
    'R3':['R1','R6'],
    'R4':['R2'],
    'R5':['R2','R6'],
    'R6':['R3','R5']
}

def dfs(grafo,inicio,visitados=None):
    if visitados is None:
     visitados = []
    visitados.append(inicio)
    for vecino in grafo[inicio]:
        if vecino not in visitados:
            dfs(grafo,vecino,visitados)
    return visitados

orden_dfs = dfs(grafo,'R1')
print("Orden de inspección de la red: ",orden_dfs)


import heapq
grafo = {
    'A':{'B':5,'C':2},
    'B':{'D':4,'E':2},
    'C':{'B':8,'D':7},
    'D':{'E':6},
    'E':{}
}

def dijkstra(grafo,inicio):
    distancias = {}
    for nodo in grafo:
        distancias[nodo]= float('inf')
    distancias[inicio] = 0
    cola_prioridad = [(0,inicio)]

    while cola_prioridad:
        dist_actual,nodo_actual = heapq.heappop(cola_prioridad)
        for vecino,peso in grafo[nodo_actual].items():
            nueva_dist = dist_actual + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                heapq.heappush(cola_prioridad,(nueva_dist,vecino))
    return distancias
resultados = dijkstra(grafo,'A')
print("El costo minimo al almacen E es: ",resultados['E'])


etapas = 5
def atenuacion(num):
    if num == 0:
        return 0
    else:
        return 2 + atenuacion(num-1)
    
print(f"Atenuacion total de la señal: {atenuacion(etapas)} dB")


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None
class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None
    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(self.raiz, dato)
    def _insertar(self, actual, dato):
        if dato < actual.dato:
            if actual.izq is None:
                actual.izq = Nodo(dato)
            else:
                self._insertar(actual.izq, dato)
        elif dato > actual.dato:
            if actual.der is None:
                actual.der = Nodo(dato)
            else:
                self._insertar(actual.der, dato)
    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izq)
            print(nodo.dato, end=" ")
            self.inorden(nodo.der)

    def preorden(self, nodo):
        if nodo is not None:
            print(nodo.dato,end=" ")
            self.preorden(nodo.izq)
            self.preorden(nodo.der)
    def postorden(self, nodo):
        if nodo is not None:
            self.postorden(nodo.izq)
            self.postorden(nodo.der)
            print(nodo.dato,end=" ")

# Crear árbol
arbol = ArbolBinarioBusqueda()
datos = [50, 30, 70, 20, 40, 60, 80]
for d in datos:
    arbol.insertar(d)
print("Recorrido Inorden: ")
arbol.inorden(arbol.raiz)
print("\nRecorrido Preorden: ")
arbol.preorden(arbol.raiz)
print("\nRecorrido Postorden: ")
arbol.postorden(arbol.raiz)

class NodoRed:
    def __init__(self, potencia):
        self.potencia = potencia
        self.izq = None
        self.der = None
class RedComunicacion:
    def __init__(self):
        self.raiz = None
    def agregar_nodo(self, potencia):
        if self.raiz is None:
            self.raiz = NodoRed(potencia)
        else:
            self._agregar(self.raiz, potencia)
    def _agregar(self, actual, potencia):
        if potencia < actual.potencia:
            if actual.izq is None:
                actual.izq = NodoRed(potencia)
            else:
                self._agregar(actual.izq, potencia)
        else:
            if actual.der is None:
                actual.der = NodoRed(potencia)
            else:
                self._agregar(actual.der, potencia)
    def recorrido_inorden(self, nodo):
        if nodo:
            self.recorrido_inorden(nodo.izq)
            print(f"Potencia de nodo: {nodo.potencia} dBm")
            self.recorrido_inorden(nodo.der)
# Ejemplo de simulación
red = RedComunicacion()
potencias = [15, 10, 20, 8, 12, 18, 25]
for p in potencias:
    red.agregar_nodo(p)
print("Análisis jerárquico de potencia (recorrido inorden): ")
red.recorrido_inorden(red.raiz)

class NodoDecision:
    def __init__(self, pregunta, si=None, no=None):
        self.pregunta = pregunta
        self.si = si
        self.no = no

def clasificar(nodo):
    respuesta = input(nodo.pregunta + " (s/n): ").lower()
    if respuesta == "s":
        if isinstance(nodo.si, NodoDecision):
            clasificar(nodo.si)
        else:
            print("Resultado:", nodo.si)
    else:
        if isinstance(nodo.no, NodoDecision):
            clasificar(nodo.no)
        else:
            print("Resultado:", nodo.no)

# Construcción del árbol de decisión
arbol = NodoDecision(
    "¿La señal es mayor a -60 dBm?",
    si=NodoDecision(
        "¿El ruido es bajo?",
        si="Señal fuerte y clara. Conexión óptima.",
        no="Señal aceptable con interferencia."
    ),
    no=NodoDecision(
        "¿La antena está alineada?",
        si="Señal débil, requiere amplificación.",
        no="Falla de comunicación. Revisar equipo."
    )
)

#clasificar(arbol)
class Nodo:
    def __init__(self, frecuencia):
        self.frecuencia = frecuencia
        self.izq = None
        self.der = None

class ArbolFrecuencias:
    def __init__(self):
        self.raiz = None

    def insertar(self, frecuencia):
        if self.raiz is None:
            self.raiz = Nodo(frecuencia)
        else:
            self._insertar(self.raiz, frecuencia)

    def _insertar(self, actual, frecuencia):
        if frecuencia < actual.frecuencia:
            if actual.izq is None:
                actual.izq = Nodo(frecuencia)
            else:
                self._insertar(actual.izq, frecuencia)
        else:
            if actual.der is None:
                actual.der = Nodo(frecuencia)
            else:
                self._insertar(actual.der, frecuencia)
    def clasificar(self, valor):
            nodo = self.raiz
            while nodo:
                if valor == nodo.frecuencia:
                    return "Frecuencia conocida"
                elif valor < nodo.frecuencia:
                    if nodo.izq is None:
                        return "Frecuencia baja"
                    nodo = nodo.izq
                else:
                    if nodo.der is None:
                        return "Frecuencia alta"
                    nodo = nodo.der

# Simulación
arbol = ArbolFrecuencias()
for f in [100, 500, 1000, 2000, 5000]:
    arbol.insertar(f)

valor = int(input("Ingresa la frecuencia de la señal (Hz): "))
print(arbol.clasificar(valor))
"""
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