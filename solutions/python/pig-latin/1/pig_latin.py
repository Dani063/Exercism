def translate(text):
    vocales = ('a', 'e', 'i', 'o', 'u')
    palabras = text.split()
    resultado = []

    for palabra in palabras:
        # Regla 1: Empieza con vocal o "xr"/"yt"
        if palabra.startswith(vocales) or palabra.startswith(("xr", "yt")):
            resultado.append(palabra + "ay")
            continue

        # Regla 2: Contiene "qu" después de consonantes
        if "qu" in palabra:
            idx = palabra.find("qu")
            # mover "qu" y las consonantes previas al final
            if idx == 0 or all(c not in vocales for c in palabra[:idx]):
                resultado.append(palabra[idx + 2:] + palabra[:idx + 2] + "ay")
                continue

        # Regla 3: Si empieza con consonantes y luego "y"
        if "y" in palabra[1:]:
            idx = palabra.find("y")
            # Si antes del 'y' no hay vocales
            if all(c not in vocales for c in palabra[:idx]):
                resultado.append(palabra[idx:] + palabra[:idx] + "ay")
                continue

        # Regla 4: Empieza con consonantes, mueve hasta la primera vocal
        for i, c in enumerate(palabra):
            if c in vocales:
                resultado.append(palabra[i:] + palabra[:i] + "ay")
                break

    return " ".join(resultado)
