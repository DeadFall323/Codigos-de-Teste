import random as rd
import time
import multiprocessing


def digite_senha():
    senha = input("Insira a senha: ")
    return senha


def cria_senha(tamanho, complexidade):
    if complexidade == 0:
        caracteres = 'abcdefghijklmnopqrstuvwxyz'
        senha_final = ''.join(rd.choice(caracteres) for _ in range(tamanho))
        return senha_final
    elif complexidade == 1:
        caracteres = '0123456789'
        senha_final = ''.join(rd.choice(caracteres) for _ in range(tamanho))
        return senha_final
    elif complexidade == 2:
        caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        senha_final = ''.join(rd.choice(caracteres) for _ in range(tamanho))
        return senha_final
    elif complexidade == 3:
        caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        senha_final = ''.join(rd.choice(caracteres) for _ in range(tamanho))
        return senha_final
    else:
        caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?'
        senha_final = ''.join(rd.choice(caracteres) for _ in range(tamanho))
        return senha_final


def confere_senha(tentativa_senha, senha, arquivo, tentativas):
    armazena_tentativa(tentativa_senha, arquivo)
    tentativas.value += 1
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


def limpar_arquivo(arquivo):
    with open(arquivo, 'w') as f:
        f.truncate(0)


def tentativa_parallel(senha, arquivo_tentativas, tamanho, complexidade, tentativas):
    tentativa_senha = cria_senha(tamanho, complexidade)
    while not confere_senha(tentativa_senha, senha, arquivo_tentativas, tentativas):
        tentativa_senha = cria_senha(tamanho, complexidade)


if __name__ == "__main__":
    senha = digite_senha()
    print("Digite o nivel de complexidade:")
    print("0 - Letras a até z")
    print("1 - Numeros 0 até 9")
    print("2 - Letras de a até z(Maiúsculas e Minúsculas)")
    print("3 - Letras de a até z(Maiúsculas e Minúsculas) + Numeros 0 até 9")
    print("4 - Letras de a até z(Maiúsculas e Minúsculas) + Numeros 0 até 9 + Caracteres especiais ")
    complexidade = int(input("Digite a complexidade"))
    arquivo_tentativas = 'senhas.txt'
    tamanho_senha = len(senha)
    tentativas = multiprocessing.Value('i', 0)
    limpar_arquivo(arquivo_tentativas)

    print("Iniciando tentativa de senha")

    inicio_tempo = time.time()

    processes = [multiprocessing.Process(target=tentativa_parallel,
                                         args=(senha, arquivo_tentativas, tamanho_senha, complexidade, tentativas)) for
                 _ in range(4)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    fim_tempo = time.time()
    tempo_total = fim_tempo - inicio_tempo

    print(f"Tempo total: {tempo_total:.2f} segundos")
    print(f"Número total de tentativas: {tentativas.value}")
