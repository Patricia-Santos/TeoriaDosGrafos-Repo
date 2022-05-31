from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from collections import deque

class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        vna = set()
        for v1 in self.N:
            for v2 in self.N:
                achei = False
                for a in self.A:
                    if v1 != v2:
                        if (v1 == self.A[a].getV1() and v2 == self.A[a].getV2()) or \
                                (v2 == self.A[a].getV1() and v1 == self.A[a].getV2()):
                            achei = True
                if not achei and v1 != v2:
                    vna.add("{}-{}".format(v1, v2))
        return vna

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in self.A:
            if self.A[i].getV1() == self.A[i].getV2():
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        vertice = False
        grau = 0

        for i in self.N:
            if i == V:
                vertice = True
                for j in self.A:
                    if self.A[j].getV1() == i:
                        grau+=1
                    if self.A[j].getV2() == i:
                        grau+=1

        if vertice == False:
            raise VerticeInvalidoException("O vértice ", V, " é inexistente")
        else:
            return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in self.A:
            cont = 0
            for j in self.A:
                if (self.A[i].getV1() == self.A[j].getV1()) and (self.A[i].getV2() == self.A[j].getV2()):
                    cont+=1
                elif (self.A[i].getV1() == self.A[j].getV2()) and (self.A[i].getV2() == self.A[j].getV1()):
                    cont+=1

            if cont >= 2:
                return True

        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        vertice = False
        arestas = set()

        for i in self.N:
            if i == V:
                vertice = True

        for j in self.A:
            if (self.A[j].getV1() == V) or (self.A[j].getV2() == V):
                arestas.add("{}".format(j))

        if vertice == False:
            raise VerticeInvalidoException("O vértice ", V, " é inexistente")
        else:
            return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        qtdVertices = len(self.N)

        if self.ha_laco() or self.ha_paralelas():
            return False

        for i in self.N:
            if (self.grau(i) != qtdVertices-1):
                return False

        return True

    def __gerarVerticesAdjacencentes(self):
        '''
        Gera dicionário com os vertices adjacentes de cada vértice do grafo
        para otimizar a realização da DFS e da BFS.
        '''
        verticesAdjacentes = {}

        for aresta in self.A:
            arestaAtual = self.A[aresta]
            if arestaAtual.getV1() not in verticesAdjacentes:
                verticesAdjacentes[arestaAtual.getV1()] = [(arestaAtual.getV2(), aresta)]
            else:
                verticesAdjacentes[arestaAtual.getV1()].append((arestaAtual.getV2(), aresta))

            if arestaAtual.getV2() not in verticesAdjacentes:
                verticesAdjacentes[arestaAtual.getV2()] = [(arestaAtual.getV1(), aresta)]
            else:
                verticesAdjacentes[arestaAtual.getV2()].append((arestaAtual.getV1(), aresta))

        return verticesAdjacentes

    def __dfs_recursivo(self, V, dfs, verticesVisitados, verticesAdjacentes):
        '''
        Responsável por percorrer o grafo de modo recursivo
        :param V: O vértice atual
        :param dfs: Grafo que será construido pela DFS
        :param verticesVisitados: Conjunto responsável por armazenar os
        vértices já visitados durante a busca
        :param verticesAdjacentes: Lista de Adjacência do grafo
        '''
        verticesVisitados.add(V)

        for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[V]:

            if verticeAdjacente not in verticesVisitados:
                dfs.adicionaAresta(rotuloAresta, V, verticeAdjacente)
                self.__dfs_recursivo(verticeAdjacente, dfs, verticesVisitados, verticesAdjacentes)

    def dfs(self, V=''):
        '''
        Provê um grafo gerado pela DFS partindo do vértice passado como parâmetro.
        :param V: O vértice de partida
        :return: Um objeto do tipo MeuGrafo com o grafo gerado
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        # O(n+m) -> n - Quantidade de vértices; m - Quantidade de arestas
        if not self.existeVertice(V):
            raise VerticeInvalidoException(f'O vértice {V} passado como parâmetro não existe.')

        verticesAdjacentes = self.__gerarVerticesAdjacencentes()

        dfs = MeuGrafo(self.N[::])
        verticesVisitados = set()

        if V not in verticesAdjacentes: return dfs

        self.__dfs_recursivo(V, dfs, verticesVisitados, verticesAdjacentes)

        return dfs

    def bfs(self, V=''):
        '''
        Provê um grafo gerado pela BFS partindo do vértice passado como parâmetro.
        :param V: O vértice de partida
        :return: Um objeto do tipo MeuGrafo com o grafo gerado
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        # O(n+m) -> n - Quantidade de vértices; m- Quantidade de arestas
        if not self.existeVertice(V):
            raise VerticeInvalidoException(f'O vértice {V} passado como parâmetro não existe.')

        bfs = MeuGrafo(self.N[::])

        verticesVisitados = set([V])
        fila = deque([V])

        verticesAdjacentes = self.__gerarVerticesAdjacencentes()

        if V not in verticesAdjacentes: return bfs

        while len(fila) != 0:
            verticeAtual = fila.popleft()

            for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[verticeAtual]:
                if verticeAdjacente not in verticesVisitados:
                    bfs.adicionaAresta(rotuloAresta, verticeAtual, verticeAdjacente)

                    verticesVisitados.add(verticeAdjacente)
                    fila.append(verticeAdjacente)

        return bfs

    def dijkstra_drone(self, vi, vf, carga:int, carga_max:int, pontos_recarga:list()):
        pass
