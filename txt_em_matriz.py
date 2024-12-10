import csv
import os

def divisao_por_paragrafo(arquivo_txt, num_colunas=3):
   
    with open(arquivo_txt, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()
    
    # Faz a quebra do texto por paragrafos
    paragrafos = texto.strip().split("\n")
    
    # Cada parágrafo é transformado em linhas e colunas da matriz
    matriz = []
    for i in range(0, len(paragrafos), num_colunas):
        linha = paragrafos[i:i + num_colunas]
        while len(linha) < num_colunas:
            linha.append("")
        matriz.append(linha)
    
    return matriz

def salvar_matriz_em_arquivo(matriz, arquivo_saida):
    
    #escreve a matriz gerada em um arquivo csv
    with open(arquivo_saida, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        
        for linha in matriz:
            writer.writerow(linha)

# Todo arquvio .txt que você colocar no repoitório será transformado
caminho_pasta = os.getcwd()  
arquivos_txt = [f for f in os.listdir(caminho_pasta) if f.endswith(".txt")]

#confere se existe arquivo .txt e chama as funções
if not arquivos_txt:
    print("Insira um arquivo .txt no diretório!")
else:
    for arquivo in arquivos_txt:
        caminho_arquivo = os.path.join(caminho_pasta, arquivo)
        
        nome_saida = f"saida_{arquivo.replace('.csv', '')}.csv"
        caminho_saida = os.path.join(caminho_pasta, nome_saida)

        #chama as funções para gerar a matriz e salvar no arquivo .csv a saída
        matriz = divisao_por_paragrafo(caminho_arquivo, num_colunas=3)
        salvar_matriz_em_arquivo(matriz, caminho_saida)
