class Statistics:
    def __init__(self, lista):
        self._lista = lista
    
    def suma(self):
        return sum(self._lista)
    
    def longitud(self):
        return len(self._lista)

    def promedio(self):
        return self.suma() / self.longitud()
    
