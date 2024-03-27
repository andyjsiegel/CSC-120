def fmt(spec, values):
    if "{}" not in spec:
        return spec
    else:
        first_occurrence = spec.index("{}")
        return spec[:first_occurrence] + str(values[0]) + fmt(spec[first_occurrence + 2:], values[1:])

# Example usage
fmt("x = {}, y = {}", [10, 20])
