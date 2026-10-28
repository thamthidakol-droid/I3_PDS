def celsius_to_fahrenheit(celcius, round_to=1):
    far = celcius * 9 / 5 + 32
    return far
print(celsius_to_fahrenheit(43), "F")
def fahrenheit_to_celsius(f,round_to=1):
    ce = (f - 32) * 5 / 9
    return ce
print(fahrenheit_to_celsius(78), "C")
