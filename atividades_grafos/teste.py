from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia

Paraiba = GrafoListaAdjacencia(["J", "C", "E", "P", "M", "T", "Z"])

Paraiba.adicionaAresta("a1", "J", "C")
Paraiba.adicionaAresta("a2", "C", "E")
Paraiba.adicionaAresta("a3", "C", "E")
Paraiba.adicionaAresta("a4", "C", "P")
Paraiba.adicionaAresta("a5", "C", "P")
Paraiba.adicionaAresta("a6", "C", "T")
Paraiba.adicionaAresta("a7", "C", "M")
Paraiba.adicionaAresta("a8", "M", "T")
Paraiba.adicionaAresta("a9", "T", "Z")

print(Paraiba)

meuGrafo = GrafoListaAdjacencia(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])

meuGrafo.adicionaAresta("1", "A", "B")
meuGrafo.adicionaAresta("2", "A", "G")
meuGrafo.adicionaAresta("3", "A", "J")
meuGrafo.adicionaAresta("4", "K", "G")
meuGrafo.adicionaAresta("5", "K", "J")
meuGrafo.adicionaAresta("6", "J", "G")
meuGrafo.adicionaAresta("7", "J", "I")
meuGrafo.adicionaAresta("8", "G", "I")
meuGrafo.adicionaAresta("9", "G", "H")
meuGrafo.adicionaAresta("10", "H", "F")
meuGrafo.adicionaAresta("11", "F", "B")
meuGrafo.adicionaAresta("12", "B", "G")
meuGrafo.adicionaAresta("13", "B", "C")
meuGrafo.adicionaAresta("14", "C", "D")
meuGrafo.adicionaAresta("15", "D", "E")
meuGrafo.adicionaAresta("16", "B", "D")
meuGrafo.adicionaAresta("17", "B", "E")

print(meuGrafo)
