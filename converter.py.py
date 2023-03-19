import sys
import gzip
from Bio import SeqIO

# Obtém a lista de arquivos a serem convertidos da linha de comando
arquivos = sys.argv[1:]

for arquivo in arquivos:
    # Lê o arquivo FASTAQ.gz
    with gzip.open(arquivo, "rt") as handle:
        # Converte cada sequência para o formato FASTA e escreve no arquivo de saída
        with open(f"{arquivo.rsplit('.', 2)[0]}.fasta", "w") as saida:
            for registro in SeqIO.parse(handle, "fastq"):
                SeqIO.write(registro, saida, "fasta")

