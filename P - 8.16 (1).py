import sys
import heapq 

entrada = sys.stdin.read().split()

if entrada:
    p = 0
    t_casos = int(entrada[p])
    p += 1
    
    respuestas_finales = []
    
    for _ in range(t_casos):
        n = int(entrada[p])
        p += 1
        
        resultado = [0] * n
        
        segmentos_heap = [(-n, 0, n - 1)]
        heapq.heapify(segmentos_heap)
        
        for i in range(1, n + 1):
            neg_long, izq, der = heapq.heappop(segmentos_heap)
            
            longitud = der - izq + 1
            if longitud % 2 != 0:
                mid = (izq + der) // 2
            else:
                mid = (izq + der - 1) // 2
            
            resultado[mid] = i
            
            if izq <= mid - 1:
                nueva_long = mid - 1 - izq + 1
                heapq.heappush(segmentos_heap, (-nueva_long, izq, mid - 1))
            
            if mid + 1 <= der:
                nueva_long = der - (mid + 1) + 1
                heapq.heappush(segmentos_heap, (-nueva_long, mid + 1, der))
        
        respuestas_finales.append(" ".join(map(str, resultado)))

    sys.stdout.write("\n".join(respuestas_finales) + "\n")