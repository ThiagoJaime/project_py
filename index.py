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
   
if __name__ == "__main__":
    main()