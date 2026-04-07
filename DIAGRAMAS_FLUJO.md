# Diagramas de flujo de los códigos

A continuación se muestran diagramas de flujo (Mermaid) para cada script del repositorio.

## 1) `E - 8.5 (1).py`

```mermaid
flowchart TD
    A[Inicio] --> B[Leer toda la entrada y separar tokens]
    B --> C{¿Hay entrada?}
    C -- No --> Z[Fin]
    C -- Sí --> D[Leer n y cadena s]
    D --> E[es_valido = True]
    E --> F[Recorrer i=0..n-2]
    F --> G{¿s[i]=='1' y s[i+1]=='1'?}
    G -- Sí --> H[es_valido = False y salir del ciclo]
    G -- No --> I[Continuar]
    I --> J{¿Termina ciclo?}
    H --> K
    J -- No --> F
    J -- Sí --> K{¿es_valido?}
    K -- No --> N[Imprimir No]
    K -- Sí --> L[Recorrer i=0..n-1 buscando '0']
    L --> M{¿s[i]=='0' y ambos vecinos son '0' o borde libre?}
    M -- Sí --> O[es_valido=False y salir]
    M -- No --> P[Continuar]
    P --> Q{¿Termina ciclo?}
    O --> R{¿es_valido?}
    Q -- No --> L
    Q -- Sí --> R
    R -- Sí --> S[Imprimir Yes]
    R -- No --> N
    S --> Z
    N --> Z
    A[Inicio] --> B[Leer tokens de stdin]
    B --> C{¿Hay token n?}
    C -- No --> Z[Imprimir salida acumulada y fin]
    C -- Sí --> D[n = int(token)]
    D --> E{¿n == 0?}
    E -- Sí --> Z
    E -- No --> F[Leer n números en lista]
    F --> G[heapify(lista)]
    G --> H[costo_total = 0]
    H --> I{¿len(heap) > 1?}
    I -- Sí --> J[Extraer 2 mínimos]
    J --> K[suma = a + b]
    K --> L[costo_total += suma]
    L --> M[Insertar suma al heap]
    M --> I
    I -- No --> N[Guardar costo_total en salida]
    N --> C
```

## 2) `F - 8.6 (1).py`

```mermaid
flowchart TD
    A[Inicio] --> B[Leer tokens de entrada]
    B --> C{¿Hay entrada?}
    C -- No --> Z[Fin]
    C -- Sí --> D[p=0, consultas_heap=[]]
    D --> E[Procesar tokens hasta '#']
    E --> F{token == '#'?}
    F -- Sí --> G[p++ y salir del registro]
    F -- No --> H{token == 'Register'?}
    H -- Sí --> I[Leer qid y periodo]
    I --> J[Agregar (periodo,qid,periodo) al heap]
    J --> E
    H -- No --> K[p++]
    K --> E
    G --> L[heapify(consultas_heap)]
    L --> M{¿Queda token para k?}
    M -- No --> Z
    M -- Sí --> N[Leer k_ejecuciones]
    N --> O[Repetir k veces]
    O --> P[pop mínimo (tiempo,qid,periodo)]
    P --> Q[Guardar qid en resultados]
    Q --> R[Calcular próximo tiempo y push]
    R --> S{¿faltan iteraciones?}
    S -- Sí --> O
    S -- No --> T[Imprimir resultados]
    A[Inicio] --> B[Leer entrada y dividir en tokens]
    B --> C{¿entrada vacía?}
    C -- Sí --> Z[Fin]
    C -- No --> D[p = 0, heap = []]
    D --> E{Recorrer tokens}
    E --> F{token == '#'}
    F -- Sí --> G[p++, salir del registro]
    F -- No --> H{token == 'Register'}
    H -- Sí --> I[Leer qid y periodo]
    I --> J[Agregar (periodo, qid, periodo) al heap]
    J --> K[p += 3]
    K --> E
    H -- No --> L[p += 1]
    L --> E
    G --> M[heapify(heap)]
    M --> N{¿p < len(entrada)?}
    N -- No --> Z
    N -- Sí --> O[Leer k_ejecuciones]
    O --> P[Repetir k veces]
    P --> Q[Extraer mínimo (tiempo, qid, periodo)]
    Q --> R[Guardar qid en resultados]
    R --> S[Reinsertar (tiempo+periodo, qid, periodo)]
    S --> P
    P --> T[Imprimir resultados]
    T --> Z
```

## 3) `G - 8.7 (1).py`

```mermaid
flowchart TD
    A[Inicio] --> B[Leer tokens]
    B --> C{¿Hay entrada?}
    C -- No --> Z[Fin]
    C -- Sí --> D[Leer n]
    D --> E[salud=0, tomadas=0, heap malas=[]]
    E --> F[Repetir para cada poción]
    F --> G[Leer valor]
    G --> H[salud += valor; tomadas += 1]
    H --> I{¿valor < 0?}
    I -- Sí --> J[push valor en heap malas]
    I -- No --> K
    J --> K{¿salud < 0?}
    K -- Sí --> L[pop peor_pocion (más negativa)]
    L --> M[salud -= peor_pocion]
    M --> N[tomadas -= 1]
    N --> O
    K -- No --> O{¿quedan pociones?}
    O -- Sí --> F
    O -- No --> P[Imprimir tomadas]
    P --> Z
    A[Inicio] --> B[Leer n y cadena s]
    B --> C[es_valido = True]
    C --> D[Recorrer i=0..n-2]
    D --> E{¿s[i]=='1' y s[i+1]=='1'?}
    E -- Sí --> F[es_valido=False]
    F --> J
    E -- No --> D
    D --> G{¿es_valido?}
    G -- No --> J
    G -- Sí --> H[Recorrer i=0..n-1]
    H --> I{¿s[i]=='0' y vecinos libres?}
    I -- Sí --> F
    I -- No --> H
    H --> J{¿es_valido?}
    J -- Sí --> K[Imprimir Yes]
    J -- No --> L[Imprimir No]
    K --> Z[Fin]
    L --> Z
```

## 4) `M - 7.13 (1).py`

```mermaid
flowchart TD
    A[Inicio] --> B[Leer entrada: n y acciones]
    B --> C{¿Hay entrada?}
    C -- No --> Z[Fin]
    C -- Sí --> D[Inicializar hotel[10]=0 y p=0]
    D --> E{¿p < n?}
    E -- No --> F[Construir string resultado]
    F --> G[Imprimir resultado]
    G --> Z
    E -- Sí --> H[accion = acciones[p]]
    H --> I{¿accion == 'L'?}
    I -- Sí --> J[Buscar habitación libre de 0 a 9 y ocuparla]
    J --> N[p += 1]
    I -- No --> K{¿accion == 'R'?}
    K -- Sí --> L[Buscar libre de 9 a 0 y ocuparla]
    L --> N
    K -- No --> M[Liberar habitación indicada por dígito]
    M --> N
    N --> E
    A[Inicio] --> B[Leer n y acciones]
    B --> C[hotel = 10 ceros]
    C --> D[p = 0]
    D --> E{¿p < n?}
    E -- No --> N[Construir string resultado]
    N --> O[Imprimir resultado y fin]
    E -- Sí --> F[accion = acciones[p]]
    F --> G{¿accion == 'L'?}
    G -- Sí --> H[Buscar de 0 a 9 primera libre y ocupar]
    H --> M[p += 1]
    G -- No --> I{¿accion == 'R'?}
    I -- Sí --> J[Buscar de 9 a 0 primera libre y ocupar]
    J --> M
    I -- No --> K[accion es dígito]
    K --> L[Liberar habitación indicada]
    L --> M
    M --> E
```

## 5) `O - 8.15 (1).py`

```mermaid
flowchart TD
    A[Inicio] --> B[Crear generador de tokens]
    B --> C[Inicializar lista salida]
    C --> D[Intentar leer n]
    D --> E{¿Fin de tokens (StopIteration)?}
    E -- Sí --> Z[Terminar ciclo principal]
    E -- No --> F{¿n == 0?}
    F -- Sí --> Z
    F -- No --> G[Leer n números en lista]
    G --> H[heapify(numeros)]
    H --> I[costo_total=0]
    I --> J{¿len(numeros) > 1?}
    J -- No --> K[Agregar costo_total a salida]
    K --> D
    J -- Sí --> L[pop primero y segundo]
    L --> M[suma = primero + segundo]
    M --> N[costo_total += suma]
    N --> O[push suma al heap]
    O --> J
    Z --> P[Imprimir salida unida por saltos de línea]
    P --> Q[Fin]
    A[Inicio] --> B[Leer n]
    B --> C[salud=0, tomadas=0, heap_neg=[]]
    C --> D[Para cada poción]
    D --> E[Leer valor]
    E --> F[salud += valor; tomadas += 1]
    F --> G{¿valor < 0?}
    G -- Sí --> H[Guardar valor en heap_neg]
    G -- No --> I
    H --> I{¿salud < 0?}
    I -- Sí --> J[Quitar peor poción negativa]
    J --> K[salud -= peor; tomadas -= 1]
    K --> D
    I -- No --> D
    D --> L[Imprimir tomadas]
    L --> Z[Fin]
```

## 6) `P - 8.16 (1).py`

```mermaid
flowchart TD
    A[Inicio] --> B[Leer tokens]
    B --> C{¿Hay entrada?}
    C -- No --> Z[Fin]
    C -- Sí --> D[Leer t_casos]
    D --> E[Inicializar respuestas_finales]
    E --> F{¿Quedan casos?}
    F -- No --> Y[Imprimir todas las respuestas]
    Y --> Z
    F -- Sí --> G[Leer n y crear resultado de tamaño n]
    G --> H[Inicializar heap con segmento total (-n,0,n-1)]
    H --> I[Para i=1..n]
    I --> J[pop segmento más largo (y más a la izquierda)]
    J --> K[Calcular mid según longitud par/impar]
    K --> L[resultado[mid] = i]
    L --> M{¿Hay subsegmento izquierdo?}
    M -- Sí --> N[push subsegmento izquierdo]
    M -- No --> O
    N --> O{¿Hay subsegmento derecho?}
    O -- Sí --> P[push subsegmento derecho]
    O -- No --> Q
    P --> Q{¿Sigue i?}
    Q -- Sí --> I
    Q -- No --> R[Agregar resultado del caso a respuestas_finales]
    R --> F
    A[Inicio] --> B[Leer t_casos]
    B --> C[Para cada caso]
    C --> D[Leer n, resultado=[0..0]]
    D --> E[heap segmentos = [(-n,0,n-1)]]
    E --> F[Para i=1..n]
    F --> G[Extraer segmento más largo]
    G --> H[Calcular mid]
    H --> I[resultado[mid] = i]
    I --> J{¿hay subsegmento izquierdo?}
    J -- Sí --> K[Insertar izq..mid-1]
    J -- No --> L
    K --> L{¿hay subsegmento derecho?}
    L -- Sí --> M[Insertar mid+1..der]
    L -- No --> F
    M --> F
    F --> N[Guardar resultado del caso]
    N --> C
    C --> O[Imprimir todos los casos]
    O --> Z[Fin]
```
