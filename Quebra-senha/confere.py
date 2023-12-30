from collections import Counter

def contar_strings_repetidas(arquivo):
    # Abrir o arquivo e ler as linhas
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    # Juntar todas as linhas em uma única string
    texto_completo = ' '.join(linhas)

    # Dividir a string em palavras
    palavras = texto_completo.split()

    # Contar a frequência das palavras
    contagem = Counter(palavras)

    # Filtrar palavras que aparecem mais de uma vez
    palavras_repetidas = {palavra: frequencia for palavra, frequencia in contagem.items() if frequencia > 1}

    # Ordenar as palavras por frequência em ordem decrescente
    palavras_ordenadas = sorted(palavras_repetidas.items(), key=lambda x: x[1], reverse=True)

    # Imprimir o resumo crescente
    print("Resumo Crescente:")
    for palavra, frequencia in palavras_ordenadas:
        print(f'{palavra}: {frequencia} repetições')

if __name__ == "__main__":
    arquivo_txt = "senhas.txt"
    contar_strings_repetidas(arquivo_txt)
