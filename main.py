from pyamaze import maze, agent, COLOR, textLabel

from BFSModule import BFS
from DFSModule import DFS
from timeit import timeit
from aStarModule import aStar

#Constantes
TEMPO = 50
MAPA_X = 10
MAPA_Y = 10
NUMERO_SOLUCOES = 0; #0 =  somente uma solução, quanto maior mais soluções irão aparecer

#Mapa
m = maze(MAPA_X, MAPA_Y)
m.CreateMaze(loopPercent=NUMERO_SOLUCOES)

#Agentes responsáveis por pintar o caminho
agentBFSSearch = agent(m, footprints=True, color=COLOR.yellow, filled=True)
agentDFSSearch = agent(m, footprints=True, color=COLOR.green, filled=True)
agentAStarSearch = agent(m, footprints=True, color=COLOR.blue, filled=True)
agentAStarBestPath = agent(m, footprints=True, color=COLOR.red)

#Caminho da busca BFS
BFSSearchPath, BFSBestPath = BFS(m)
m.tracePath({agentBFSSearch: BFSSearchPath}, delay=TEMPO)
BFSSearchPathCorrect = 0

#Caminho da busca DFS
DFSSearchPath, DFSBestPath = DFS(m)
m.tracePath({agentDFSSearch: DFSSearchPath}, delay=TEMPO)

#Caminhos da busca e menor caminho AStar
aStarSearchPath, aStarBestPath = aStar(m)
m.tracePath({agentAStarSearch: aStarSearchPath}, delay=TEMPO)
m.tracePath({agentAStarBestPath: aStarBestPath}, delay=TEMPO)

#Temporizadores
t1 = timeit(stmt='BFS(m)', number=1000, globals=globals())
t2 = timeit(stmt='DFS(m)', number=1000, globals=globals())
t3 = timeit(stmt='aStar(m)', number=1000, globals=globals())

correct = 0
if len(BFSSearchPath) == MAPA_X * MAPA_Y - 2:
    correct = len(BFSSearchPath) + 2
else:
    correct = len(BFSSearchPath) + 1

#Labels
textLabel(m, 'BFS busca', correct)
textLabel(m, 'BFS menor caminho', len(BFSBestPath) + 1)
textLabel(m, 'Tempo BFS', round(t1, 3))
textLabel(m, 'DFS busca', len(DFSSearchPath))
textLabel(m, 'DFS menor caminho', len(DFSBestPath) + 1)
textLabel(m, 'Tempo DFS', round(t2, 3))
textLabel(m, 'AStar busca', len(aStarSearchPath) - 1)
textLabel(m, 'Tempo AStar', round(t3, 3))
textLabel(m, 'AStar Menor caminho ', len(aStarBestPath) + 1)

m.run()
