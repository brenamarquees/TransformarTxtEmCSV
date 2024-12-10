# Transformar Txt Em CSV
Desafio 1  - Para o curso de IA da flyEducação em parceria com o I2A2.

Este script Python lê arquivos `.txt` de um diretório, divide o texto em parágrafos e organiza esses parágrafos em uma matriz com um número fixo de colunas. A matriz resultante é então salva em arquivos `.csv`.

## Como funciona

O código executa as seguintes etapas:

1. **Leitura do arquivo `.txt`:** O arquivo de texto é lido e os parágrafos são extraídos.
2. **Divisão em Parágrafos:** O texto é dividido em parágrafos usando quebras de linha como delimitador.
3. **Organização em Matrizes:** O texto é organizado em uma matriz, com cada linha contendo até 3 parágrafos (por padrão). Se a última linha não tiver o número exato de colunas, as colunas vazias são preenchidas com strings vazias.
4. **Salvamento em CSV:** A matriz é salva em um arquivo `.csv`, com uma linha para cada conjunto de parágrafos.

## Pré-requisitos

- Python 3.x
- Biblioteca `csv` (inclusa no Python por padrão)
- Arquivos de texto (`.txt`) no mesmo diretório do script

## Como Usar

1. Coloque os arquivos `.txt` no mesmo diretório que este script.
2. Execute o script. Ele irá procurar automaticamente por arquivos `.txt` e gerar um arquivo `.csv` para cada um, com o mesmo nome do arquivo de entrada, mas com o prefixo `saida_`.

### Exemplo de Execução:

Se o seu diretório contém os seguintes arquivos:

documento1.txt e documento2.txt

Após executar o script, ele gerará os seguintes arquivos:


## Funções

### `divisao_por_paragrafo(arquivo_txt, num_colunas=3)`

Esta função lê o arquivo de texto, divide o conteúdo em parágrafos e organiza esses parágrafos em uma matriz com um número específico de colunas (padrão é 3). Retorna a matriz gerada.

#### Parâmetros:
- `arquivo_txt`: Caminho para o arquivo `.txt` que será processado.
- `num_colunas`: Número de colunas desejado na matriz (padrão é 3).

#### Retorno:
- Matriz organizada em parágrafos.

### `salvar_matriz_em_arquivo(matriz, arquivo_saida)`

Esta função salva a matriz gerada em um arquivo `.csv`.

#### Parâmetros:
- `matriz`: Matriz de dados a ser salva no arquivo `.csv`.
- `arquivo_saida`: Caminho para o arquivo de saída onde a matriz será salva.
