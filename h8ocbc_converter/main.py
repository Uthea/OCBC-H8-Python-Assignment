def celcius2kelvin(celcius):
    return celcius + 273.15


def kelvin2celcius(kelvin):
    return kelvin - 273.15


def to_fahrenheit(value, temp_type):
    assert temp_type in ['kelvin', 'celcius']
    temp_value = 0
    if temp_type == "kelvin":
        temp_value = kelvin2celcius(value)
    else:
        temp_value = value

    return (temp_value * 9 / 5) + 32


def from_fahrenheit(value, output_temp_type):
    assert output_temp_type in ['kelvin', 'celcius']

    celcius_value = (value - 32) * (5 / 9)

    if output_temp_type == "kelvin":
        return celcius2kelvin(celcius_value)

    return celcius_value


if __name__ == '__main__':
    print(from_fahrenheit(20, 'meong'))
