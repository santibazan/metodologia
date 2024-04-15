n = 18
i = 1
divisor = 0
for i in range(1,n):
    if (n % i == 0):
        divisor = divisor + 1
if (divisor>2):
    print("No es un numero primo")
else:
    print("Es un numero primo")    

#Chat GPT

def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= numero:
            if numero % i == 0 or numero % (i + 2) == 0:
                return False
            i += 6
        return True

numero = 29

if es_primo(numero):
    print(f"{numero} es primo.")
else:
    print(f"{numero} no es primo.")

#AMAZON CODEWHISPERER
def is_prime(num):
  if num < 2:
    return False
  
  for i in range(2,num):
    if num % i == 0:
      return False

  return True

number = int(input("Ingrese un numero: "))
if is_prime(number):
  print(f"{number} es un numero primo")
else: 
  print(f"{number} no es un numero primo")
