#Author: Figen Güngör
#Year: 2013
#Artifical Intelligence HW1: Implementation of A Star Graph Search Algorithm

from search_problem import *

a = State('Arad')
b = State('Bucharest')
c = State('Craiova')
d = State('Drobeta')
e = State('Eforie')
f = State('Fagaras')
g = State('Giurgiu')
h = State('Hirsova')
i = State('Iasi')
l = State('Lugoj')
m = State('Mehadia')
n = State('Neamt')
o = State('Oradea')
p = State('Pitesti')
r = State('Rimnicu Vilvea')
s = State('Sibiu')
t = State('Timisoara')
u = State('Urziceni')
v = State('Vaslui')
z = State('Zerind')

STRAIGHT_LINE_DIST_TO_B = {
    a : 366, b : 0,   c : 160, d : 242, e : 161,
    f : 176, g : 77,  h : 151, i : 226, l : 244,
    m : 241, n : 234, o : 380, p : 100, r : 193,
    s : 253, t : 329, u : 80,  v : 199, z : 374
}

def straight_line_distance_to_b(node):
    return STRAIGHT_LINE_DIST_TO_B[node.state]

Problem.connect_states_both_ways(a, z, 75)
Problem.connect_states_both_ways(a, s, 140)
Problem.connect_states_both_ways(a, t, 118)

Problem.connect_states_both_ways(o, z, 71)
Problem.connect_states_both_ways(o, s, 151)

Problem.connect_states_both_ways(l, t, 111)
Problem.connect_states_both_ways(l, m, 70)
Problem.connect_states_both_ways(m, d, 75)
Problem.connect_states_both_ways(d, c, 120)

Problem.connect_states_both_ways(s, f, 99)
Problem.connect_states_both_ways(s, r, 80)
Problem.connect_states_both_ways(r, c, 146)
Problem.connect_states_both_ways(r, p, 97)
Problem.connect_states_both_ways(c, p, 138)

Problem.connect_states_both_ways(f, b, 211)
Problem.connect_states_both_ways(p, b, 101)
Problem.connect_states_both_ways(b, g, 90)
Problem.connect_states_both_ways(b, u, 85)

Problem.connect_states_both_ways(u, h, 98)
Problem.connect_states_both_ways(h, e, 86)

Problem.connect_states_both_ways(u, v, 142)
Problem.connect_states_both_ways(v, i, 92)
Problem.connect_states_both_ways(i, n, 87)

problem = Problem('Romania Routes')

if __name__ == '__main__':
    print('A* Graph Search with a null heuristic:')
    print('-' * 40)
    print(problem.a_star_graph_search(a, [b], lambda node: 0))
    print('')
    print('A* Graph Search with straight line heuristic:')
    print('-' * 40)
    print(problem.a_star_graph_search(a, [b], straight_line_distance_to_b))
