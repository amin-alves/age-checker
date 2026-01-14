nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print("Nome:", nome)

if idade >= 18:
    print("Status: Maior de idade")
else:
    print("Status: Menor de idade")