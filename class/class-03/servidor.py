"""
Los métodos mágicos (dunders) se utilizan precisamente para eso: para que tú decidas y controles la
lógica interna de cómo van a reaccionar tus objetos ante las operaciones estándar de Python.
Depende de la lógica interna del negocio
"""


class Servidor:
    def __init__(self, nombre, so, version, servicios=None):
        """Inicializa los atributos básicos de un servidor."""
        self.nombre = nombre
        self.so = so
        self.version = version
        self.servicios = list(servicios or [])

    def __repr__(self):
        """Define cómo se muestra el objeto visualmente al hacer un print()."""
        return f"Servidor({self.nombre!r}, {self.so} {self.version}, {len(self.servicios)} svc)"

    def __eq__(self, otro):
        """Define la regla de igualdad (==) basada en el nombre."""
        return self.nombre == otro.nombre

    def __lt__(self, otro):
        """Define la regla de menor que (<) basada en la versión del SO."""
        return self._version_tupla() < otro._version_tupla()

    def _version_tupla(self):
        """Convierte la versión (ej. '22.04') en una tupla de enteros (22, 4) para comparar bien."""
        return tuple(int(p) for p in self.version.split("."))


if __name__ == "__main__":
    a = Servidor("web-01", "ubuntu", "22.04", ["nginx", "postgres"])
    b = Servidor("web-01", "ubuntu", "22.04", ["nginx", "postgres"])
    c = Servidor("db-01", "ubuntu", "20.10", ["postgres"])

    print("a:", a)

    # Evalúa si la versión de 'a' es menor que la de 'c' (22.04 < 20.10 -> False)
    # print("a < c:", a < c)

    servidores = [a, c]

    # min() utiliza por debajo el método __lt__ que definiste para encontrar el menor
    print("Servidor con menor versión:", min(servidores))
