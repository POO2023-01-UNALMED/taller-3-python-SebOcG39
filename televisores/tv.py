class TV:
    numTV = 0
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.volumen = 1
        self.precio = 500
        self.control = None
        TV.numTV += 1
    
    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca
    
    def setControl(self, control):
        self.control = control

    def getControl(self):
        return self.control

    def setPrecio(self, precio):
        self.precio = precio
    
    def getPrecio(self):
        return self.precio
    
    def setVolumen(self, volumen):
        if self.estado:
            if volumen>=0 and volumen<=7:
                self.volumen = volumen
    
    def getVolumen(self):
        return self.volumen
    
    def setCanal(self, canal):
        if self.estado:
            if canal<=120 and canal >= 1:
                self.canal = canal

    def getCanal(self):
        return self.canal
    
    @classmethod
    def getNumTv(cls):
        return cls.numTV
    
    @classmethod
    def setNumTv(cls, num):
        cls.numTV = num
    
    def turnOn(self):
        self.estado = True
    
    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if self.estado:
            if self.canal<120:
                self.canal += 1
    
    def canalDown(self):
        if self.estado:
            if self.canal>1:
                self.canal -= 1
    
    def volumenUp(self):
        if self.estado:
            if self.volumen<7:
                self.volumen += 1

    def volumenDown(self):
        if self.estado:
            if self.volumen>0:
                self.volumen -= 1