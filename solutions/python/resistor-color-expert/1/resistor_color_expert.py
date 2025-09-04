def resistor_label(colors):
    if len(colors) == 1:
        if colors[0] == "black":
            return "0 ohms"
        raise ValueError("One-band resistors must be black (0 ohms).")

    digit = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    tol = {
        "grey": "±0.05%", "violet": "±0.1%", "blue": "±0.25%", "green": "±0.5%",
        "brown": "±1%", "red": "±2%", "gold": "±5%", "silver": "±10%"
    }

    if len(colors) == 4:
        d_bands = colors[:2]
        mult_c  = colors[2]
        tol_c   = colors[3]
    elif len(colors) == 5:
        d_bands = colors[:3]
        mult_c  = colors[3]
        tol_c   = colors[4]

    #EXCEPCIONES
    else:
        raise ValueError("Expected 1, 4, or 5 bands.")
    try:
        base = int("".join(str(digit[c]) for c in d_bands))
    except KeyError as e:
        raise ValueError(f"Unknown digit color: {e.args[0]}")
    try:
        power = digit[mult_c]
    except KeyError as e:
        raise ValueError(f"Unknown multiplier color: {e.args[0]}")
    if tol_c not in tol:
        raise ValueError(f"Unknown tolerance color: {tol_c}")

    value_ohms = base * (10 ** power)

    def fmt_num(x):
        s = f"{x:.2f}"
        return s.rstrip("0").rstrip(".")

    if value_ohms >= 1_000_000:
        value = fmt_num(value_ohms / 1_000_000) + " megaohms"
    elif value_ohms >= 1_000:
        value = fmt_num(value_ohms / 1_000) + " kiloohms"
    else:
        value = f"{int(value_ohms)} ohms" if float(value_ohms).is_integer() \
                else fmt_num(value_ohms) + " ohms"

    return f"{value} {tol[tol_c]}"