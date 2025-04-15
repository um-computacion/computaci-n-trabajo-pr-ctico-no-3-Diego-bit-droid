from src.exceptions import NumeroDebeSerPositivo

def ingrese_numero():
    
    try:
        num = int(input("Ingrese un número: "))
        
        if num < 0:
            raise NumeroDebeSerPositivo("El número debe ser positivo")  
        return num
    
    except ValueError:
        raise ValueError("La entrada debe ser un número válido.")