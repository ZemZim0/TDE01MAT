# GABRIEL ZEM MURARO


def união():
  #Cria o conjunto final
  lista_final = set()
  #Passa por todo o arquivo txt
  for op in range(len(texto)):
  #Identifica o U  
    if texto[op].strip() == "U":
  #Seleciona para trabalhar com as próximas 2 lihas após o U que serão os conjuntos
      if op + 2 < len(texto):
  #Retira todos os espaços e virgulas para que a função trabalhe apenas com inteiros       
        primeira_lista = texto[op + 1].strip().split(", ")
        segunda_lista = texto[op + 2].strip().split(", ")
  #Cria um conjunto com os elementos da primeira lista e da segunda lista    
        lista_final.update(primeira_lista)
        lista_final.update(segunda_lista)
  #Remove os números repetidos e organiza eles em ordem crescente      
        lista_final = sorted(lista_final)
  #Imprime o resultado final da União
        return(print("União: \nconjunto 1 {",primeira_lista,"} \nconjunto 2 {",segunda_lista,"} \nResultado: {",lista_final,"}"))    



def Intersecao():
  #Cria o conjunto final
  lista_final = set()
  #Passa por todo o arquivo txt
  for op in range(len(texto)):
  #Identifica o I
    if texto[op].strip() == "I":
  #seleciona para trabalhar com as proximas 2 lihas após o I que serão os conjuntos
      if op + 2 < len(texto):
  #Retira todos os espaços e virgulas para que a função trabalhe apenas com inteiros
        primeira_lista = texto[op + 1].strip().split(", ")
        segunda_lista = texto[op + 2].strip().split(", ")
  #Faz a interseção entre os conjuntos e adiciona os elementos iguais em ordem crescente
        lista_final = set(primeira_lista).intersection(segunda_lista)
        lista_final = sorted(lista_final)
        return(print("Interseção: \nconjunto 1 {",primeira_lista,"}\nconjunto 2 {",segunda_lista,"} \nResultado: {",lista_final,"}")) 





def Diferenca():
  #Cria o conjunto final
  lista_final = set()
  #Passa por todo o arquivo txt
  for op in range(len(texto)):
  #Identifica o I
    if texto[op].strip() == "D":
  #seleciona para trabalhar com as proximas 2 lihas após o I que serão os conjuntos
      if op + 2 < len(texto):
  #Retira todos os espaços e virgulas para que a função trabalhe apenas com inteiros
        primeira_lista = texto[op + 1].strip().split(", ")
        segunda_lista = texto[op + 2].strip().split(", ")
  #Faz a diferença entre os conjuntos e adiciona os elementos que estão apenas presentes     #no primeiro conjunto e não presentes no segundo
        lista_final = set(primeira_lista) - set(segunda_lista)

        return(print("Diferença: \nconjunto 1 {",primeira_lista,"} \nconjunto 2 {",segunda_lista,"} \nResultado: {",lista_final,"}")) 
        


def Cartesiano():
  #Cria o conjunto final
  lista_final = []
  #Passa por todo o arquivo txt
  for op in range(len(texto)):
  #Identifica o I
    if texto[op].strip() == "C":
  #seleciona para trabalhar com as proximas 2 lihas após o I que serão os conjuntos
      if op + 2 < len(texto):
  #Retira todos os espaços e virgulas para que a função trabalhe apenas com inteiros
        primeira_lista = texto[op + 1].strip().split(", ")
        segunda_lista = texto[op + 2].strip().split(", ")

        for i in range(len(primeira_lista)):
          for j in range(len(segunda_lista)):
            lista_final.append(primeira_lista[i])
            lista_final.append(segunda_lista[j])
            #lista_final.update(segunda_lista[j])
        return(print("Produto cartesiano: \nconjunto 1 {",primeira_lista,"} \nconjunto 2 {",segunda_lista,"} \nResultado: {",lista_final,"}")) 
        



#Para selecionar qual arquivo .txt deseja que seja utilizado
SA = str(input("Digite o arquivo que deseja realizar as operações (No formato .txt)"))
Ar = open(SA, "r")
texto = Ar.readlines()


união()
print()
Intersecao()
print()
Diferenca()
print()
Cartesiano()






#ENUNCIADO
#Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
#linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
#operações que serão realizadas entre dois conjuntos de dados.
#O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
#contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
#em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
#segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
#operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
#seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
#operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
#terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
#das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
#4
#U
#3, 5, 67, 7
#1, 2, 3, 4
#I
#1, 2, 3, 4, 5
#4, 5
#D
#1, A, C, 34
#A, C, D, 23
#C
#3, 4, 5, 5, A, B, R
#1, B, C, D, 1
#Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
#produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e
#{𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
#A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
#dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
#a informação e a formatação mostrada a seguir:
#União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}
#Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
#um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
#de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
#minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
#No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e
#pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
#implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.