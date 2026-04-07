import sys

entrada = sys.stdin.read().split()

if entrada:
    p = 0
    n = int(entrada[p]) 
    s = entrada[p+1]    
    
    es_valido = True 
    
    for i in range(n - 1):
        if s[i] == '1' and s[i+1] == '1':
            es_valido = False
            break
            
    if es_valido:
        for i in range(n):
            if s[i] == '0':
                izq_libre = (i == 0 or s[i-1] == '0')
                der_libre = (i == n-1 or s[i+1] == '0')

                if izq_libre and der_libre:
                    es_valido = False
                    break

    if es_valido:
        print("Yes")
    else:
        print("No")