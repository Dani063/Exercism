def is_paired(input_string):
    pairs = {')': '(', ']': '[', '}': '{'}
    openings = set(pairs.values()) # Eficiencia O(1) 
    stack = []

    for ch in input_string:
        if ch in openings:
            stack.append(ch)
        elif ch in pairs:
            if stack and stack[-1] == pairs[ch]:
                stack.pop()
            else: 
                return False
    return not stack