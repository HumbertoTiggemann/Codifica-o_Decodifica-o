
caracteres= [' ','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','Á', 'À', 'Ã', 'Â', 'É', 'È', 'Ê', 'Í', 'Ì', 'Î', 'Ó', 'Ò', 'Õ', 'Ô', 'Ú', 'Ù', 'Û', 'Ç', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','á', 'à', 'ã', 'â', 'é', 'è', 'ê', 'í', 'ì', 'î', 'ó', 'ò', 'õ', 'ô', 'ú', 'ù', 'û', 'ç', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~','´','º','ª','º','ª',]
modulo= len(caracteres)


def chave_letras(chave:str): #funçao chave - recebe a chave e transforma em lista com valor das chaves

  chave_letras= []

  for valor_chave in chave: #localizar as letras da chave na lista de todos os caracteres
    if valor_chave in caracteres:
      valor= caracteres.index(valor_chave) #valores de cada caractere
      chave_letras.append(valor)
  return chave_letras # lista com valores de cada caractere da chave



def frase_letras(frase:str): #funcao frase - recebe a chave e transforma em lista com valor das letras

  frase_letras= []

  for valor_frase in frase: #localizar as letras da frase na lista de todos os caracteres
    if valor_frase in caracteres:
      valor= caracteres.index(valor_frase) #valores de cada caracteres
      frase_letras.append(valor)
  return frase_letras# lista com valores de cada caractere da frase



def codificar(chave_letras:list, frase_letras:list):#funçao codificar - recebe lista chave e lista de frase e invoca frase codificada

#algoritimo One-time pad SOMA o valor da letra com o valor da chave(em sequencia)e receber modulo

# 1 criar lista com valor da chave em sequencia para a soma - depende do tamnho da frase
  chave_sequencia_valor= []

  while len(chave_sequencia_valor) < len(frase_letras):
    for valor1 in chave_letras:
      chave_sequencia_valor.append(valor1)

#2 somar para lista codificada
  lista_codificada_valores= []

  for posicao in range(len(frase_letras)):
    frase_modulo= (chave_sequencia_valor[posicao] + frase_letras[posicao]) #soma
    if frase_modulo > modulo:
      frase_modulo = frase_modulo%modulo
      lista_codificada_valores.append(frase_modulo)
    else:
      lista_codificada_valores.append(frase_modulo)

#3  Lista resposta codificada em letras
  frase_codificada_lista=[]

  for valor in lista_codificada_valores: #localizar os valores para formar a frase codificada
    valor_letra = caracteres[valor] #valores de cada caractere
    frase_codificada_lista.append(valor_letra) #lista com valores de cada caractere da frase codificada

  frase_codificada= "".join(frase_codificada_lista)
  return frase_codificada # frase codificada



def decotificar(chave_letras:list, frase_letras:list): #funçao decotificar - recebe lista chave e lista de frase e invoca frase codificada

#algoritimo One-time pad DIMINUI o valor da letra com o valor da chave(em sequencia)e receber modulo,

# 1 criar lista com valor da chave em sequencia para a diminuir - depende do tamnho da frase
  chave_sequencia_valor= []

  while len(chave_sequencia_valor) < len(frase_letras):
    for valor in chave_letras:
      chave_sequencia_valor.append(valor)

#2 diminui para lista codificada
  lista_decodificada_valores= []

  for posicao in range(len(frase_letras)):
    frase_modulo= -(chave_sequencia_valor[posicao] - frase_letras[posicao]) #diminui
    if frase_modulo > modulo:
      frase_modulo = frase_modulo%modulo
      lista_decodificada_valores.append(frase_modulo)
    else:
      lista_decodificada_valores.append(frase_modulo)

#3  Lista resposta codificada em letras
  frase_decodificada_lista=[]

  for valor in lista_decodificada_valores: #localizar os valores para formar a frase codificada
    valor_letra = caracteres[valor] #valores de cada caractere
    frase_decodificada_lista.append(valor_letra) #lista com valores de cada caractere da frase codificada

  frase_decodificada= "".join(frase_decodificada_lista)
  return frase_decodificada # frase decodificada



#perguntas interativas - pede  açao (codificar e decotificar (retorna se parametro correto), chave, frase,e invoca resultado - pede para parar ou repetir
def codificador():

  acao= input("Selecione o numero para ação dejesada : \n ( 1 ) Codificar \n ( 2 ) Decodificar \n ( 3 ) Sair do decoditificador \n   ") #escolha decotificada ou codificada ou sair


  while acao == "3":
    print ("\nObrigado por usar o Codificador!")
    break
  else:
    while acao != "1" and acao != "2":
      acao= input(print("Digite 1 para Codificar o texto ou 2 para Decodificar o texto ou 3 para Sair: \n   "))

    if acao == "1":
      frase= input("Digite o texto para ser Codificado: \n") #frase a ser decotificada ou codificada
      chave= input(f"Digite a chave: \n") #chave para codificaçao
      print(f"A chave é: \n\n ==>{chave}<==\n")
      frase_codificada= codificar(chave_letras(chave),frase_letras(frase))
      print(f" A frase codificada é: \n\n ==>{frase_codificada}<==")#frase codificada
      print("\n   ")
      codificador()

    elif acao == "2":
      frase= input("Digite o texto para ser Decodificado: \n") #frase a ser decotificada ou codificada
      chave= input("Digite a chave: \n") #chave para codificaçao
      print(f"A chave é: \n\n ==>{chave}<==\n")
      frase_decodificada = decotificar(chave_letras(chave),frase_letras(frase))
      print(f" A frase decodificada é: \n\n ==>{frase_decodificada}<==")#frase decodificada
      print("\n   ")
      codificador()




