from pipeline import cargar_config, limpiar_nombres, registrar, resumen


def main():
    print("--- 1. Probando limpiar_nombres ---")
    nombres_raw = ["  JUAN ", " MAría", "pedro  "]
    nombres_limpios = limpiar_nombres(nombres_raw)
    print(f"Nombres procesados: {nombres_limpios}\n")

    print("--- 2. Probando registrar ---")
    registrar("Inicio de sesión")
    registrar("Compra realizada")
    registrar("Cierre de sesión")
    print()

    print("--- 3. Probando resumen ---")
    ventas = {"Enero": 1500.50, "Febrero": 2300.00, "Marzo": 1800.25}
    mensaje_resumen = resumen(ventas)
    print(f"{mensaje_resumen}\n")


if __name__ == "__main__":
    main()
