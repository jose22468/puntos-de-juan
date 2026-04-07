import sys
import heapq 

entrada = sys.stdin.read().split()

if entrada:

    p = 0
    
    consultas_heap = []
    
    while p < len(entrada):
        token = entrada[p]

        if token == "#":
            p += 1
            break
            
        if token == "Register":
            qid = int(entrada[p+1])    
            periodo = int(entrada[p+2])  

            consultas_heap.append((periodo, qid, periodo))
            p += 3
        else:
            p += 1

    heapq.heapify(consultas_heap)

    if p < len(entrada):
        k_ejecuciones = int(entrada[p])
        
        resultados = []

        for _ in range(k_ejecuciones):
            tiempo_actual, qid, periodo = heapq.heappop(consultas_heap)

            resultados.append(str(qid))
            
            proximo_tiempo = tiempo_actual + periodo
            heapq.heappush(consultas_heap, (proximo_tiempo, qid, periodo))

        sys.stdout.write("\n".join(resultados) + "\n")