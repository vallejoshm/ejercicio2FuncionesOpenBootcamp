def esPrimo(num):
    contador = 0
    for i in range(2,num+1):
        if num%i == 0:
            contador+=1
            if contador > 2:
                break
    else:
        return True
    return False
print("El numero es primo: " + str(esPrimo(100)))