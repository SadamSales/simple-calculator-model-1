# Programa inicial 1:
# Desenvolver um programa que some 2 numeros inteiros.
# Requisitos:
#   - Os 2 números deve ser digitados pelo usuário
#   - utilizando a instrução print informar o usário sobre o que
# o programa irá realizar
#   - Executar a operação de adição utilizado o operador +
#   - Mostrar para o usuário a resposta final

def main():
    print("------- SOMA DE 2 NÚMEROS -------")

    numero1 = int( input("Digite o primeiro numero para soma: ") )  #float
    numero2 = int( input("Digite o segundo numero para soma: ") )

    soma = numero1 + numero2

    print("O resultado da soma é ", soma)


if __name__ == "__main__":
    main()