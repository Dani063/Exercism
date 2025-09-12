def flatten(iterable):
    output = []
    for item in iterable:
        if isinstance(item, list):
            output.extend(flatten(item))
        elif isinstance(item, int):
            output.append(item)
    return output
