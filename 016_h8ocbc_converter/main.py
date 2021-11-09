def celcius2kelvin(celcius):
    """
    this function convert celcius to kelvin
    :param celcius: int or float
    :return float in kelvin
    """
    return celcius + 273.15


def kelvin2celcius(kelvin):
    """
    this function convert kelvin to celcius
    :param kelvin: int or float
    :return float in celcius
    """
    return kelvin - 273.15


def to_fahrenheit(value, temp_type):
    """
    this function convert kelvin or celcius value into fahrenheit
    :param value: int or float
    :param temp_type: dictate whether value is 'kelvin' or 'celcius'
    :return int or float in fahrenheit
    """
    assert temp_type in ['kelvin', 'celcius'], "type must be kelvin or celcius"
    temp_value = 0
    if temp_type == "kelvin":
        temp_value = kelvin2celcius(value)
    else:
        temp_value = value

    return (temp_value * 9 / 5) + 32  #


def from_fahrenheit(value, output_temp_type):
    """
    this function convert fahrenheit value into kelvin or celcius
    :param value: int or float
    :param output_temp_type: dictate return value is in 'kelvin' or 'celcius'
    :return int or float in kelvin or celcius (depends on output_temp_type param)
    """
    assert output_temp_type in ['kelvin', 'celcius'],"type must be kelvin or celcius"

    celcius_value = (value - 32) * (5 / 9)

    if output_temp_type == "kelvin":
        return celcius2kelvin(celcius_value)

    return celcius_value


if __name__ == '__main__':
    print(from_fahrenheit(20, "kelvin"))
