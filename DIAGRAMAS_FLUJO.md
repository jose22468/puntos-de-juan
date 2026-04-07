# Diagramas de flujo de los códigos

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
```
