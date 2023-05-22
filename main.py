from scrapper import scrap, dbscrap
from graphs import plotCSV

def main():
    print("Web Scrapping")

    no = int(input("Número de cursos:"))
    types = input("0 para candidatos ou 1 para colocados:")
    filepath = []
    siglas = []

    for x in range(no):
        codCurso = input("Código Curso:")
        codR = input("Código R:")
        codEstab = input("Código Estabelecimento:")
        ano = input("Ano:")
        filename = input("Nome do ficheiro csv:")
        curso = input("id de curso:")
        #sigla = input("Etiqueta da curva do curso:")
        #siglas.append(sigla)

        filepath.append("csv/" + filename + ".csv")
        dbscrap(codCurso, codR, codEstab, ano, types, filepath[x], curso)

    if types == "0":
        plotCSV(filepath, siglas)


main()