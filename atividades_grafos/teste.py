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