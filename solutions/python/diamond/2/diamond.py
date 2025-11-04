def rows(letter: str) -> list[str]:
    letter = letter.upper()
    idx = ord(letter) - 65  # 65 == ord('A')
    result = []

    for i in range(idx + 1):
        ch = chr(65 + i)
        outer = " " * (idx - i)
        if i == 0:
            texto = f"{outer}{ch}{outer}"
        else:
            inner = " " * (2 * i - 1)
            texto = f"{outer}{ch}{inner}{ch}{outer}"
        result.append(texto)

    return result + result[:-1][::-1]
