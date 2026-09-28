# Python Data Model: El Manual de Usuario de tus Objetos

Imagina que Python es un gran juego de mesa y tus objetos son las piezas que creas. Para que tus piezas puedan interactuar con el tablero y las reglas del juego, necesitan seguir un manual de instrucciones. Ese manual es el **Data Model**.

## 1. ¿Qué es un Objeto en Python?

- Todo en Python es una entidad viva llamada **objeto**.

- Cada objeto tiene tres características principales:

  - **Tipo de clase:** Qué tipo de objeto es (ej. un número, un texto, una caja).

  - **Dato:** La información o valor que guarda en su interior.

  - **Comportamiento:** Las acciones que puede realizar.

## 2. Operaciones

- Son las funciones genéricas que Python te ofrece para interactuar con las cosas (por ejemplo, medir el tamaño con `len(caja)` o sumar dos elementos con `+`).

- **La regla de oro:** Tú escribes la operación de alto nivel (lo que ves), y Python se encarga de buscar y disparar el comportamiento interno correspondiente.

- _Ejemplo:_ Escribes `len(caja)` y Python busca cómo calcular la longitud de esa caja de forma automática. Nunca llamas directamente al método interno.

## 3. Protocolos

- Un protocolo es como una **lista de requisitos o un contrato** que un objeto debe cumplir para poder participar en una operación específica.

- Si quieres que tu objeto sepa su longitud, debe cumplir con el protocolo de longitud implementando el requisito que Python espera.

## 4. Métodos Mágicos (Dunder Methods / Specification Methods)

- Son los métodos especiales que tienen doble guion bajo al inicio y al final (por eso se llaman _dunder_, de _double underscore_).

- **Están escritos para el intérprete, no para ti:** Tú no los ejecutas directamente escribiendo `caja.__len__()`, sino que escribes la operación `len(caja)` y Python los llama por detrás.

- Se dividen en dos familias principales:

  - **Con red de seguridad (con _default_):** Objetos como `object` ya te dan un comportamiento genérico por defecto (como `__eq__` para comparar o `__repr__`). Si no los tocas, la operación no explota y usa ese comportamiento por defecto.

  - **Sin red de seguridad (sin _default_):** Si no los escribes, la operación falla directamente con un `TypeError` (como `__len__` o `__getitem__`). Los agregas tú mismo para habilitar una operación que antes no existía en tu clase.

## 5. La Escalera Completa: Del Concepto al Código

Para entender cómo funciona todo conectado de abajo hacia arriba:

1. **Nivel 4 - Operación:** Lo único que tú tocas en tu código (ej. `len(caja)`).

2. **Nivel 3 - Special Method (Dunder):** El código real que tú escribes para cumplir la regla (ej. `def __len__(self): return 5`).

3. **Nivel 2 - Protocolo:** Los requisitos que exige esa operación en particular.

4. **Nivel 1 - Data Model:** El reglamento completo del lenguaje que gobierna todo.

## 6. Mapa de Referencia Rápida

| **Operación que escribes** | **Comportamiento / Protocolo** | **Método Mágico (Dunder) típico** |
| -------------------------- | ------------------------------ | --------------------------------- |
| `len(obj)`                 | Longitud                       | `__len__`                         |
| `obj[0]`                   | Acceso / Indexación            | `__getitem__`                     |
| `obj + x`                  | Suma                           | `__add__`                         |
| `obj == x`                 | Comparación                    | `__eq__`                          |
| `for x in obj`             | Iteración                      | `__iter__` / `__next__`           |
| `x in obj`                 | Pertenencia                    | `__contains__`                    |
| `obj()`                    | Llamada                        | `__call__`                        |
| `with obj`                 | Context Manager                | `__enter__` / `__exit__`          |

_Nota:_ Algunos comportamientos complejos (como los administradores de contexto con `with`) requieren más de un dunder porque tienen varios momentos distintos (por ejemplo, abrir y cerrar un archivo).
