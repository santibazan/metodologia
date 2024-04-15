def fibo(n):
    if (n == 1 or n == 0):
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("Ingrese la cantidad de terminos que desea imprimir: "))
for i in range(0,n):
    print("Termino "+str((i+1))+": "+str(fibo(i)))

#chat GPT
def fibonacci(n):
    fibonacci_seq = [0, 1] 

    for i in range(2, n):
        next_term = fibonacci_seq[i - 1] + fibonacci_seq[i - 2]
        fibonacci_seq.append(next_term)

    return fibonacci_seq[:n]  

n = int(input("Ingrese la cantidad de términos de Fibonacci que desea: "))

resultado = fibonacci(n)
print("Los primeros", n, "términos de la secuencia de Fibonacci son:", resultado)
