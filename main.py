import networkx as nx
# кол-во вершин
n = 20
# вероятность появления случайного ребра
p = 0.15

# генерация графа
G = nx.erdos_renyi_graph(n, p)

# рассчёт средней степени вершин графа
a = 0
for n in G.nodes():
    a = a + G.degree(n)

# средняя степень вершины фактическая
a_avr = float(a) / len(G.nodes())

# средняя степень вершины по формуле
calc_avr = (n-1)*p

# разница значений
div_a = calc_avr - a_avr
print("Средняя степень вершины фактическая: ", round(a_avr, 3))
print("Средняя степень вершины по формуле: ", round(calc_avr, 3))
print("Полученная разница значений: ", round(div_a, 3))
