import random as rd
import time


def digite_senha():
    senha = input("Insira a senha: ")
    return senha


def cria_senha(tamanho):
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?'
    senha_final = ''.join(rd.choice(caracteres) for _ in range(tamanho))
    return senha_final


def confere_senha(tentativa_senha, senha, arquivo):
    armazena_tentativa(tentativa_senha, arquivo)
    if tentativa_senha == senha:
        print("Senha encontrada com sucesso:", senha)
        return True
    else:
        print("Tentativa:", tentativa_senha)
        return False


def armazena_tentativa(senha_armazenada, arquivo):
    with open(arquivo, 'a') as f:
        f.write(senha_armazenada + '\n')


def verifica_tentativa(tentativa, arquivo):
    with open(arquivo, 'r') as f:
        return tentativa in f.read()


if __name__ == "__main__":
    senha = digite_senha()
    arquivo_tentativas = 'senhas.txt'
    tentativa_senha = ''
    contador_tentativas = 0

    print("Iniciando tentativa de senha")

    inicio_tempo = time.time()

    while not confere_senha(tentativa_senha, senha, arquivo_tentativas):
        tentativa_senha = cria_senha(len(senha))
        while verifica_tentativa(tentativa_senha, arquivo_tentativas):
            tentativa_senha = cria_senha(len(senha))

        contador_tentativas += 1

    fim_tempo = time.time()
    tempo_total = fim_tempo - inicio_tempo

    print(f"Tempo total: {tempo_total:.2f} segundos")
    print(f"Número total de tentativas: {contador_tentativas}")
