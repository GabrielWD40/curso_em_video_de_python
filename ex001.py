print('\033[1;32;40mOlá, mundo!\033[m')#aqui eu estou colorindo o meu código com negrito, letras de cor verde e background preto.
msg = input('\033[4;31;40mQual é o seu nome? ') #aqui eu estou dizendo que eu quero que meu código fique sublinhado, com letra vermelha e background preto.
print('\033[7molá, ', msg)#O prefixo 7 é usado para inverter os valores se a çetra é preta, o background passa a ser preto. Se o backgroun é amarelo, as letras ficam amarelas.
#Além disso, eu deixei sem finalizar a formatação para que você veja que se não colocar o fim, ele aplica pra linha toda.
