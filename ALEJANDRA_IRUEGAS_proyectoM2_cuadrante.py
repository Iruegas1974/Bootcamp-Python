"""
Programa para identificar coordenadas en un plano cartesiano

1. saluda
2. Con ciclo while, pregunta si quiere introducir unas coordenadas, en caso de que no: se imprime: fin del programa
3. Al introducir las coordenadas se verifica que sean numéricas, con un ciclo while: hasta que se introduzca un número
4. con una serie de condicionales, se corrobora en qué cuadrante están las coordenadas. 
    cuadrante I:    x +, y +
    cuadrante II:   x -, y +
    cuadrante III:  x -, y -
    cuadrante IV:   x +, y -
"""

print ("Hola! Este programa identifica el cuadrante del plano cartesiano en el que se encuentran las coordenadas.")

while True:
    respuesta = input('Quieres introducir unas coordenadas? (si /no): ')
    if respuesta.lower() == 'no':
        print ('Fin del programa')
        break
    
    while True:
        try:
            coord_x = input('Ingresa la coordenada de las x: ')
            if coord_x.isnumeric():
                x = int(coord_x)
                break
            else: 
                print('El dato es incorrecto, debe ser numérico.')
        except ValueError: 
            print('Error')
                    
    while True:
        try:
            coord_y = input('Ìngresa la coordenada de las y: ')
            if coord_y.isnumeric():
                y = int(coord_y)
                break
            else: 
                print ('El dato es incorrecto, debe ser numérico')
        except ValueError: 
            print('Error')
    

    if x < 0 and y < 0:
        print (f'Las coordenadas ({x}, {y}) se encuentra en el cuadrante III.')
    if x < 0 and y > 0:
        print (f'Las coordenadas ({x}, {y}) se encuentra en el cuadrante II.')    
    if x > 0 and y < 0:
        print (f'Las coordenadas ({x}, {y}) se encuentra en el cuadrante IV.')
    if x > 0 and y > 0:
        print (f'Las coordenadas ({x}, {y}) se encuentra en el cuadrante I.')   
    if x == 0 or y == 0: 
        print ("No está permitido ingresar el '0' (cero) como coordenada")    
        
