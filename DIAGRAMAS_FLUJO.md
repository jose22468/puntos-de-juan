# Diagramas de flujo de los códigos

A continuación se muestran diagramas de flujo (Mermaid) para cada script del repositorio.

## 1) `E - 8.5 (1).py`

```mermaid
flowchart TD
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
