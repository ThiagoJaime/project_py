#importação do módulo 're' para simplificar as consultas
import re

db = [
   ['Candidato 1', 'e5_t10_p8_s8'],
   ['Candidato 2', 'e10_t7_p7_s8'],
   ['Candidato 3', 'e8_t5_p4_s9'],
   ['Candidato 4', 'e2_t2_p2_s1'],
   ['Candidato 5', 'e10_t10_p8_s9']
]

#função para validação do padrão definido
def validaInput(entrada):
    padrao = r'^\d+,\d+,\d+,\d+$'
    return bool(re.match(padrao, entrada))

#função para pegar tudo entre (0-9) na string
def extrairNumbers(notas):
    numeros = []
    for nota in notas:
        #usando método extend junto do list comprehension + findall para pegar as notas em int
        numeros.extend([int(num) for num in re.findall(r'\d+', nota)])
    return numeros
   
def main():

   #vai repetir até o usuário colocar no formato correto
   while True:
      notas = input('''
         Digite as notas: 1º entrevista, 2º teórico, 3º prático, 4º softSkill
         Exemplo: 4,4,8,8
         -> ''').replace(' ', '')
      
      if(not validaInput(notas)):
         print("\n**Digite no formato correto!**")
      else:
         break
   
   #lista em int do input do user
   listaNota = list(map(int, notas.split(',')))

   listaPesquisa = []

   #looping para ir em cada candidato
   for candidato in db:

      #pega as notas de cada usuário
      numbers = extrairNumbers(candidato[1].split('_'))

      ehMenor = False

      #compara as notas em cada lista
      for i in range(len(numbers)):

            if(numbers[i] < listaNota[i]):
               ehMenor = True
               break
      
      if(not ehMenor):
            
            listaPesquisa.append(candidato)   

   #se a lista estiver vazia
   if(not listaPesquisa):
            
      print("Resultados não compatíveis")
            
   else:

      #exibe os resultados      
      for candidato in listaPesquisa:
         
         user = extrairNumbers(candidato[1].split('_'))

         print(f'''{candidato[0]}: Entrevista: {user[0]}, Teórico: {user[1]}, Prático: {user[2]}, SoftSkill: {user[3]}
# ----------------------------------------------------------------- #''') 
                 
if __name__ == "__main__":
    main()