import sys
import heapq 

entrada = sys.stdin.read().split()

if entrada:
    p = 0
    n = int(entrada[p])
    p += 1
    
    salud = 0
    pociones_tomadas = 0
    malas_bebidas = []
    
    for _ in range(n):
        valor = int(entrada[p])
        p += 1
        
        salud += valor
        pociones_tomadas += 1
        
        if valor < 0:
            heapq.heappush(malas_bebidas, valor)
            
        if salud < 0:
            peor_pocion = heapq.heappop(malas_bebidas)
            
            salud -= peor_pocion

            pociones_tomadas -= 1
    print(pociones_tomadas)