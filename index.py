import re

db = [
   ['Candidato 1', 'e5_t10_p8_s8'],
   ['Candidato 2', 'e10_t7_p7_s8'],
   ['Candidato 3', 'e8_t5_p4_s9'],
   ['Candidato 4', 'e2_t2_p2_s1'],
   ['Candidato 5', 'e10_t10_p8_s9']
]

def validaInput(entrada):
    padrao = r'^\d+,\d+,\d+,\d+$'
    return bool(re.match(padrao, entrada))

def extrairNumbers(notas):
    numeros = []
    for nota in notas:
        numeros.extend([int(num) for num in re.findall(r'\d+', nota)])
    return numeros
   
def main():

   while True:
      notas = input('''
         Digite as notas: 1º entrevista, 2º teórico, 3º prático, 4º softSkill
         Exemplo: '4,4,8,8'
         -> ''').replace(' ', '')
      
      if(not validaInput(notas)):
         print("Digite no formato correto!\n")
      else:
         break
   
   listaNota = notas.split(',')
   listaPesquisa = []
   MAX_SIZE = len(db)
   cont = 0

   while True:

      for candidato in db:

         numbers = extrairNumbers(candidato[1].split('_'))

         ehMenor = False

         for i in range(len(numbers)):

               if(numbers[i] < int(listaNota[i])):
                  ehMenor = True
                  break
         
         if(not ehMenor):
               
               listaPesquisa.append(candidato)   
      
         cont += 1

      if(cont == MAX_SIZE):
         
         if(not listaPesquisa):
                  
               print("Resultados não compatíveis")
                  
         else:
                  
               for candidato in listaPesquisa:
                  
                  user = extrairNumbers(candidato[1].split('_'))

                  print(f'''{candidato[0]}: Entrevista: {user[0]}, Teórico: {user[1]}, Prático: {user[2]}, SoftSkill: {user[3]}
--------------------------------------------------------------------''') 
            
         break
      
if __name__ == "__main__":
    main()