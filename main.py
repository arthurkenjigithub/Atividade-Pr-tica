import re


def validar_email(email):
    # Expressão regular para validar o formato de um endereço de e-mail
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Verifica se o e-mail corresponde ao padrão
    if re.match(padrao, email):
        return True
    else:
        return False


def main():
    email = input("Digite o endereço de e-mail a ser validado: ")

    if validar_email(email):
        print("O endereço de e-mail é válido.")
    else:
        print("O endereço de e-mail é inválido.")


if __name__ == "__main__":
    main()
