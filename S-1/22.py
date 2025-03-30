import random
def lanzar_dado():
    """Simula el lanzamiento de un dado de seis caras."""
    return random.randint(1, 6)
def lanzar_moneda():
    """Simula el lanzamiento de una moneda."""
    return random.choice(["Cara", "Cruz"])
if __name__ == "__main__":
    print(f"Resultado del dado: {lanzar_dado()}")
    print(f"Resultado de la moneda: {lanzar_moneda()}")