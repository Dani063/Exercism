# Números del 0 al 19
UNITS = [
    "zero", "one", "two", "three", "four", "five", "six", "seven",
    "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]

# Decenas
TENS = [
    "", "", "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety"
]

# Escalas (hasta 999,999,999,999)
SCALES = [
    "",
    "thousand",
    "million",
    "billion"
]

def say(number):
    if number > 999999999999 or number < 0:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"

    chunks = []
    while number != 0:
        chunks.append(number % 1000)
        number //= 1000

    parts = []
    for i, chunk in enumerate(chunks):
        if chunk == 0:
            continue
        text = say_999(chunk)
        scale = SCALES[i]
        parts.append(text + (f" {scale}" if scale else ""))

    return " ".join(reversed(parts))


def say_999(num):
    if num < 20:
        return UNITS[num]

    if num < 100:
        ten = TENS[num // 10]
        unit = num % 10
        return ten if unit == 0 else f"{ten}-{UNITS[unit]}"

    hundred_part = f"{UNITS[num // 100]} hundred"
    rest = num % 100
    return hundred_part if rest == 0 else f"{hundred_part} {say_999(rest)}"
