""""
Esse algoritmo deve ser um número de 0 a 9999 e separar ele nas casas unidades,
dezenas, centenas e unidade de milhar.
"""
print('Vamos descobrir quantas unidades, dezenas, centenas e unidades de milhar o seu número tem!')
numero = str(input('Digite um número entre 0 e 9999: ')).strip()
numero_convertido = int(numero[0:4])

unidade_milhar = numero_convertido // 1000
centena = (numero_convertido % 1000) // 100
dezena = ((numero_convertido % 1000) % 100) // 10
unidade = (((numero_convertido % 1000) % 100)%10) // 1

print("Seu número tem {} unidade(s) de milhar. "
      "\nSeu número tem {} centena(s). "
      "\nSeu número tem {} dezena(s)."
      "\nSeu número tem {} unidade(s).".format(unidade_milhar, centena, dezena, unidade))

"""
Outra maneira de fazer:

unidade_milhar =numero_convertido // 1000
#No exemplo acima eu peguei a divisão inteira do número, dividindo ele por mil.
centena = (numero_convertido - (unidade_milhar*1000)) // 100
dezena = (numero_convertido - ((unidade_milhar * 1000) + (centena *100))) // 10
unidade = (numero_convertido -((unidade_milhar * 1000) + (centena * 100) + (dezena * 10))) // 1
print("Seu número tem {} unidade(s) de milhar. "
      "\nSeu número tem {} centena(s). "
      "\nSeu número tem {} dezena(s)."
      "\nSeu número tem {} unidade(s).".format(unidade_milhar, centena, dezena, unidade))
      
Gabriel do futuro: 
   Isso deu um trabalhão pra fazer, mas você conseguiu acertar o exercício de boaça! 
   Então, não desista de continuar em frente. Supero todos eles. Seja forte, garoto. Em frente, soldado!!! 
"""