numero= int(input("Por favor digite un numero:  "))
    
def numero_par_impar(numero):
    
    if numero%2==0:
        return True
    else:
        return False


if numero_par_impar(numero)==True:
    print("El numero que digito es PAR" )
else:
  
    print("El numero que digito es IMPAR")



