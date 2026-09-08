# Ruff y UV

## UV

### Crear proyecto con Python 3.14

Crea un nuevo proyecto y utiliza Python 3.14.

```sh
uv init python-avanzado --python 3.14
```

**Resultado:** crea la estructura inicial del proyecto y el `pyproject.toml`.

---

### Agregar dependencias

Agrega una librería al proyecto.

```sh
uv add pandas
```

**Resultado:** `pandas` se agrega como dependencia y se actualiza `pyproject.toml` y `uv.lock`.

---

### Agregar dependencias de desarrollo

Agrega una librería que se utilizará durante el desarrollo.

```sh
uv add --dev pytest
```

**Resultado:** `pytest` queda registrado como dependencia de desarrollo.

---

### Eliminar dependencias

Elimina una dependencia del proyecto.

```sh
uv remove pandas
```

**Resultado:** `pandas` se elimina de las dependencias y se actualiza `uv.lock`.

---

### Ver árbol de dependencias

Muestra las dependencias del proyecto y sus dependencias internas.

```sh
uv tree
```

**Resultado:** muestra un árbol con las librerías instaladas.

---

### Sincronizar dependencias

Sincroniza el entorno virtual con las dependencias del proyecto.

```sh
uv sync
```

**Resultado:** instala o elimina paquetes para que el entorno coincida con `pyproject.toml` y `uv.lock`.

---

### Ver versión de Ruff

Comprueba qué versión de Ruff está disponible en el entorno.

```sh
uv run ruff --version
```

**Resultado:** muestra algo como:

```text
ruff 0.x.x
```

---

### Ejecutar Python dentro del entorno

Ejecuta Python utilizando el entorno del proyecto.

```sh
uv run python main.py
```

**Resultado:** ejecuta `main.py` con las dependencias del proyecto.

---

## Ruff

### Revisar problemas del código

Analiza el archivo buscando problemas de linting.

```sh
uv run ruff check pipeline.py
```

**Resultado:** muestra los errores o advertencias encontrados.

Ejemplo:

```text
F401 `pandas` imported but unused
```

---

### Ver estadísticas de los problemas

Muestra un resumen de los problemas encontrados agrupados por regla.

```sh
uv run ruff check --statistics pipeline.py
```

**Resultado:** muestra cuántos problemas existen de cada regla.

Ejemplo:

```text
2	F401
1	E501
```

---

### Ver los cambios que Ruff realizaría

Muestra las correcciones que Ruff podría realizar sin modificar el archivo.

```sh
uv run ruff check --diff pipeline.py
```

**Resultado:** muestra un `diff` con los cambios propuestos.

---

### Corregir problemas automáticamente

Aplica las correcciones automáticas consideradas seguras.

```sh
uv run ruff check --fix pipeline.py
```

**Resultado:** modifica `pipeline.py` y corrige los problemas que Ruff puede solucionar automáticamente.

---

### Ver correcciones inseguras antes de aplicarlas

Permite a Ruff considerar correcciones inseguras y muestra los cambios sin modificar el archivo.

```sh
uv run ruff check --fix-only --unsafe-fixes --diff pipeline.py
```

**Resultado:** muestra qué cambios adicionales podría realizar Ruff.

> `--unsafe-fixes` puede realizar cambios que podrían afectar el comportamiento del código. Por eso es recomendable revisar primero el `diff`.

---

### Aplicar correcciones inseguras

Aplica las correcciones automáticas, incluyendo las consideradas inseguras.

```sh
uv run ruff check --fix --unsafe-fixes pipeline.py
```

**Resultado:** modifica `pipeline.py` aplicando las correcciones disponibles.

---

## Ruff Format

### Ver cambios de formato

Muestra cómo Ruff formatearía el archivo sin modificarlo.

```sh
uv run ruff format --diff pipeline.py
```

**Resultado:** muestra un `diff` con los cambios de formato.

---

### Formatear el código

Aplica automáticamente el formato de Ruff.

```sh
uv run ruff format pipeline.py
```

**Resultado:** modifica `pipeline.py` para dejarlo con el formato de Ruff.

---

### Verificar el formato sin modificar

Comprueba si el archivo ya tiene el formato correcto.

```sh
uv run ruff format --check pipeline.py
```

**Resultado:** indica si el archivo necesita ser formateado, pero no realiza ningún cambio.

````

Así cada comando te queda con la misma estructura mental:

**comando → qué hace → resultado que obtengo**.

Y especialmente para Ruff puedes recordar:

```text
ruff check       → busca problemas
ruff check --fix → corrige problemas
ruff format      → ordena/formatea el código
--diff           → muestra los cambios
--check          → verifica sin modificar
--unsafe-fixes   → permite correcciones más riesgosas
```
````
