def celcius2kelvin(celcius):
    return celcius + 273.15


def kelvin2celcius(kelvin):
    return kelvin - 273.15


def to_fahrenheit(value, temp_type):
    assert temp_type in ['kelvin', 'celcius'], "type must be kelvin or celcius"  # make sure to limit the options
    temp_value = 0
    if temp_type == "kelvin":  # if input value is kelvin then convert it first to celcius
        temp_value = kelvin2celcius(value)
    else:
        temp_value = value  # if already in celcius, just assign the value

    return (temp_value * 9 / 5) + 32  # celcius to fahrenheit equation


def from_fahrenheit(value, output_temp_type):
    assert output_temp_type in ['kelvin', 'celcius'],"type must be kelvin or celcius"  # make sure to limit the options

    celcius_value = (value - 32) * (5 / 9)  # convert to celcius by default

    if output_temp_type == "kelvin":  # if output temperature type is kelvin then convert celcius to kelvin
        return celcius2kelvin(celcius_value)  # convert to kelvin and return it

    return celcius_value  # if output type is celcius then no further processing needed


if __name__ == '__main__':
    print(from_fahrenheit(20, 'celcius'))
