def invertir(cadena):
    """Inverteix la cadena passada com a argument."""
    # Inverteix la cadena i canvia la capitalització
    return cadena[::-1]

# Proves de la funció
print(invertir("Soc del Ramis"))  # Retorna "simaR led coS"
print(invertir("Hola món"))       # Retorna "nòm aloH"
print(invertir("Python"))          # Retorna "nohtyP"