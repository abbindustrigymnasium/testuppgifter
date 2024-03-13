def factorial(n):
    result = 1
    for i in range(n):
        result *= i
    return result

try:
    ans=int(input("Skriv en siffra så får du fakulteten tillbaka!"))
    print(factorial(ans))
except ValueError:
    print("Din input är inte en int - försök igen!")
