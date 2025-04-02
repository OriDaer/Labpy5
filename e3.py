n = int(input('Ingresa un número entero: '))

def fibonacci(n):
    arr = [] 
    for i in range(n):
        if i <= 1:
            arr.append(i) 
        else:
            arr.append(arr[i - 1] + arr[i - 2])  
    return arr

print(fibonacci(n)) 