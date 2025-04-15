from src.exceptions import NumeroDebeSerPositivo
#ingrese lo de abajo para ejecutar
#python -m  src.calculo_numeros


def ingrese_numero():
    try:
        num = int(input("Ingrese un número: "))
        if num < 0:
            raise NumeroDebeSerPositivo("El número debe ser positivo")  
        return num
    except ValueError:
        raise ValueError("La entrada debe ser un numero valido.")  

def main():
    while True:
        try:
            num = ingrese_numero()
            print(f"Numero valido: {num}")
        except NumeroDebeSerPositivo as error1:
            print(f"error: {error1}")  
        except ValueError as error2:
            print(f"error: {error2}")  
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario Finalizando")
