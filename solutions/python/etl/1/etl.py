def transform(legacy_data):
    result = {}
    for value, sublist in legacy_data.items():
        for item in sublist:
            result[item.lower()] = value
    return result