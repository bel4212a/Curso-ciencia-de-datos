class Carro:
    """Representacion basica de un carro"""
    def __init__(self, marca, modelo, anio):
        """Atributos del carro"""
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = 0   # Se define un atributo por defecto
    
    def descripcion(self):
        """Descripcion del carro segun sus atributos"""
        nombre_largo = self.marca +  ' ' + self.modelo + ' ' + str(self.anio)
        return nombre_largo.title()
    
    def leer_kilometraje(self):
        """Imprimir le kilometraje del carro"""
        print("Esta carro tiene un kilometraje registrado de " + str(self.kilometraje) + " Km.")
        
    def actualizar_km(self, valor):
        """modificacion del kilometraje"""
        if valor >= self.kilometraje:
            self.kilometraje = valor
        else:
            print("No es permitido reducir el kilometraje del auto.")
            
    def llenar_tanque(self):
        """Permite lennar el tanuqe del vehiculo"""
        print("Su tanque ahora esta lleno.")

class CarroElectrico(Carro):
    """Representacion de los vehiculos electricos"""
    def __init__(self, marca, modelo, anio):
        """Inicializa atributos de la clase padre"""
        """Tambien inicializa el tamanio de la bateria"""
        super().__init__(marca, modelo, anio) # Me permite referirme a los atributos y metodos del padre
        self.bateria = 70
        
    def imprimir_bateria(self):
        """Describe el estado de la bateria"""
        print("Este vehiculo cuenta con una bateria de " + str(self.bateria) + " Kwh.")
        
    def llenar_tanque():
        """Sobrecarga del metodo llenar tanque para carros electricos"""
        print("Los carros electricos no tiene tanque que llenar.")