class Statistics:
    def __init__(self, lista):
        self._lista = lista
    
    def suma(self):
        return sum(self._lista)
    
    def longitud(self):
        return len(self._lista)

    def promedio(self):
        return self.suma() / self.longitud()
    
milista = [23, 3, 32, 32, 54, 36, 54645, 3]
stat = Statistics(milista)

print(f"Suma: {stat.suma()} y Longitud: {stat.longitud()}")
print(f"Promedio: {stat.promedio():.2f}") # Redondeado a 2 decimales para que se vea limpio