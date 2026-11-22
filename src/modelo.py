import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Datos del gestor de incidencias
semana = np.array([1, 2, 3, 4, 5, 6])
hallados = np.array([28, 52, 72, 90, 105, 118])

#Crear el modelo de campanas
class CampanaPruebas:
    def __init__(self,defectos):
        self.defectos = np.array(defectos)
        self.semana =np.array([1,2,3,4,5,6,7,8])
        self.hallados = np.cumsum(self.defectos)

# Modelo de Goel-Okumoto
    def goel(self, t, a, b):
        return a * (1 - np.exp(-b * t))

    # Ajuste de los dos parámetros
    def ajustar(self):
        p, _ = curve_fit(self.goel, self.semana, self.hallados,
                         p0=[200, 0.1])
        self.a, self.b = p

    #defectos restantes
    def restantes(self):
        return self.a - self.goel(8, self.a, self.b)

    #Cuando llega al 95% de los defectos
    def semana_95(self):
        return np.log(20) / self.b

    #Grafica
    def graficar(self):
        t = np.linspace(0, 25, 100)
        plt.scatter(self.semana, self.hallados, label="Semana")
        plt.plot(t, self.goel (t, self.a, self.b), label = "Curva")
        plt.title("Modelo de Goel")
        plt.xlabel("Semana")
        plt.ylabel("Defectos Acumulados")
        plt.legend()
        plt.savefig("Modelo de Goel")
        plt.show()






