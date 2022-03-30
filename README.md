# Interface do BLAST (*WINDOWS E LINUX*)

Com o objetivo de auxiliar os pesquisadores a utilizar e ensinar como se faz um alinhamento de sequencias no **BLAST+** construi esta ferramenta.
Seguem os passos para a sua utilização:

## Instalando ferramentas Blast+ no Linux

Obtenha os executáveis compilados deste URL: 

```
ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/
```

Descompacte o arquivo. Por exemplo:

```
tar xvfz ncbi-blast-2.9.0+-x64-linux.tar.gz
```

Adicione a pasta `bin` do arquivo extraído ao seu *PATH*:

```
export PATH="/PATH/TO/ncbi-blast-2.9.0+/bin":$PATH
```

E mude a parte `/PATH/TO` para o caminho onde você colocou o arquivo extraído
arquivo.

## Instalando o Python  e os pacotes utilizados no Linux

Use o comando no Terminal: 

```
sudo apt-get install python3/
```

Adicione ao PATH:

```
PATH = "$ PATH: / usr / local / bin / python3"
```

Instale o pacote TKINTER ao Python

```
sudo apt-get install python-tk python3-tk 
```

**Para usar o programa no Linux você precisa substituir no código com o local de entrada dos arquivos de imagem**


Importar imagens Linux

```
#img_fundo = PhotoImage(file="/home/ufpa/PycharmProjects/pythonProject/BLAST/imagens/Fundo.png")
#img_botao1 = PhotoImage(file="/home/ufpa/PycharmProjects/pythonProject/BLAST/imagens/DB.png")
#img_botao2 = PhotoImage(file="/home/ufpa/PycharmProjects/pythonProject/BLAST/imagens/BLASTAR.png")
```

#

## Instalando ferramentas Blast+ no Windows

Obtenha os executáveis compilados deste URL e instale: 

```
 ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.7.1/ncbi-blast-2.7.1+-win64.exe
```


## Instalando o Python e os pacotes utilizados no Windows

Acompanhe a instalação neste tutorial 

```
https://python.org.br/instalacao-windows/
```


Instale o pacote TKINTER ao Python

```
pip install tk
```


## COMO UTILIZAR O PROGRAMA?

O programa é instintivo de se utilizar.

Para testar o blast, você precisa de um arquivo fasta de teste. 
Use os seguintes arquivos que vem com este software:

- `databas.fna`
- `genes.fasta` 

Após isso você irá:
- Clicar na busca pelo arquivo do banco de dados
- Selecionar o formato do seu banco de dados entre Nucleotideos (nucl) e Proteinas (prot)
- Clicar em Fazer Banco de Dados.

Depois irá fazer o alinhamento das sequencias:

- Escolha o arquivo que será alinhado
- Escolha o tipo de Blast
- Escolha o Evalue a ser utilizado
- Clice quem **Fazer Blast**

Dúvidas: *savscosta@gmail.com*

