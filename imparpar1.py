def Numeroparimpar():
    numero= int(input("Por favor digite un numero: "))
    if numero%2==0:
        print("El numero que usted digito es par")
    else:
        print("El numero que usted digito es impar")

    return()


def main():
    Numeroparimpar()

if __name__ == "__main__":
    main()
