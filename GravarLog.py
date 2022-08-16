def GravarLog(indice):
    blocoNotas = open("log.txt", "a")
    blocoNotas.write("\n=============================\n")
    blocoNotas.write("Número de Comentários: {0}".format(indice))
    blocoNotas.write("\n")
    blocoNotas.close()
