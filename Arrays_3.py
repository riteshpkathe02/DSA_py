# My Code

n = int(input("Enter the number till which you have to print odd numbers: "))

for i in range(n+1):
    if i%2==1:
        print(i)

#Ideal code
'''max = int(input("Enter max number: "))

odd_numbers = []

for i in range(1, max):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Odd numbers: ", odd_numbers)'''