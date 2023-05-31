#esse algoritmo deve converter as temperaturas em Celsius para fahrenheit e kelvin

print("Digite uma temperatura em °C (graus celsius) para converter em °F(fahrenheit) e °K(kelvin)!")
c = float(input("°C: "))
conversação_fahrenheit = ((c*9) + (-5 * -32)) / 5
#Para converter em fahrenheit vc poder usar também: (1.8 * c) + 32

conversação_kelvin = c + 273

print('{}°C graus celsius equivalem a {:.2f}°F (fahrenheit) '.format(c, conversação_fahrenheit))
print('{}°C graus celsius equivalem a {:.2f}°K (Kelvin) '.format(c, conversação_kelvin))

"""
c     tf  - 32
-    ________
5         9
"""