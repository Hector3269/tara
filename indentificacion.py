print ("tu codigo de verificacion es : 123456789 ")
verificacion =int(input("ingresa tu codigo de verificacion :"))

while True:
    if verificacion == 123456789 :
        print ("tu codigo de verificacion es corecto ")
        break
    else :
        print ("tu codigo de verificacion es incorrecto, intentalo de nuevo")
        verificacion = int(input("ingresa tu codigo de verificacion"))
 