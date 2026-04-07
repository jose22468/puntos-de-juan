import sys
entrada = sys.stdin.read().split()

if entrada:
    n = int(entrada[0])
    acciones = entrada[1]
    hotel = [0] * 10
    
    p = 0
    while p < n:
        accion = acciones[p]
        
        if accion == 'L':
            i = 0
            while i < 10:
                if hotel[i] == 0:
                    hotel[i] = 1 
                    break 
                i += 1
                
        elif accion == 'R':
            i = 9
            while i >= 0:
                if hotel[i] == 0:
                    hotel[i] = 1 
                    break
                i -= 1
                
        else:
            habitacion_index = int(accion)
            hotel[habitacion_index] = 0 
            
        p += 1 

    resultado = ""
    for estado in hotel:
        resultado += str(estado)
        
    print(resultado)