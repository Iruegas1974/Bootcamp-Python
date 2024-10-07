"""
Programa para verificar que la palabra tenga la longitud correcta
1. Saludo.
2. pregunta si el usuario quiere introducir una palabra, con un ciclo while. Cuando se introduce 'no' se detiene el programa.
3. se verifica la longitud de la palabra con la función len(), 
    si es menor de 4 se imprime que hacen falta lentras e imprime la longitud de la palabara
    si es mayor de 8 se imprime que sobran letras e imprime la longitud de la palabra
    si la longitud de la palabra está entre 4 y 8 letras, imprime que la palabra es correcta. 
"""

print ("Hola. Este programa verifica que la palabra tenga la longitud correcta (entre 4 y 8 caracteres)")

while True:
    respuesta = input('Quieres introducir una palabra? (si /no): ')
    if respuesta.lower() == 'no':
        print ('Fin del programa')
        break

    palabra = input('Ingresa una palabra: ')

    if len(palabra) < 4:
        print (f'Hacen falta letras, solo tiene {len(palabra)} letras.')
    elif len(palabra) >8:
        print(f'Sobran letras, tiene {len(palabra)} letras.')
    else: 
        print('La palabra es correcta.')
