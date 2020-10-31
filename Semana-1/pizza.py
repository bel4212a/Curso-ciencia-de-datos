def preparar(size, *toppings):
    """Resumen de la pizza que se elaborara."""
    print("Haciendo una pizza de " + str(size) + "-cm con las siguientes adiciones:")
    for topping in toppings:
        print("- " + topping)
        
def bebida(bebida):
    """imprime la bebida solicitada"""
    print("La bebida que usted eligio es " + bebida)
    
def saludar(usuario):
    print("Hola " + usuario + " como esta?")