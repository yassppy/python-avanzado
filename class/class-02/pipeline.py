import json


def limpiar_nombres(nombres: list[str]) -> list[str]:
    limpios = []
    for i in range(len(nombres)):
        limpios.append(nombres[i].strip().lower())
    return limpios


def cargar_config(ruta: str | None = None) -> dict:
    if ruta is None:
        ruta = "config.json"
    f = open(ruta)
    datos = json.load(f)
    f.close()
    return datos


def registrar(evento, historial=None):
    if historial is None:
        historial = []
    historial.append(evento)
    print(f"evento {evento} registrado, total: {len(historial)}")
    return historial


def resumen(ventas: dict[str, float]) -> str:
    total = sum(ventas.values())
    return f"total de ventas: {total}"
