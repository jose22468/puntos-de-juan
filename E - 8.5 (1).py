import sys
import heapq

def resolver():
    def traer_datos():
        for linea in sys.stdin:
            for palabra in linea.split():
                yield palabra
    
    tokens = traer_datos()
    
    salida = []

    while True:
        try:
            token = next(tokens)
            n = int(token)
        except StopIteration:
            break
            
        if n == 0:
            break
            
        numeros = []
        for _ in range(n):
            numeros.append(int(next(tokens)))

        heapq.heapify(numeros)
        
        costo_total = 0
        
        while len(numeros) > 1:
            primero = heapq.heappop(numeros)
            segundo = heapq.heappop(numeros)
            
            suma = primero + segundo
            costo_total += suma
            
            heapq.heappush(numeros, suma)
            
        
        salida.append(str(costo_total))

    sys.stdout.write("\n".join(salida) + "\n")

if __name__ == "__main__":
    resolver()