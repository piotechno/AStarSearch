#Author: Figen Güngör
#Year: 2013
#Artifical Intelligence HW1: Implementation of A Star Graph Search Algorithm

from romania_routes import *

print("\nShortest route from Timisoara to Bucharest using the straight line heuristic:\n")
x = problem.a_star_graph_search(t, [b], straight_line_distance_to_b)
print(x)
print('-' * 40)

print("\nThe shortest route from Mehadia to Bucharest:\n")    
y = problem.a_star_graph_search(m,[b], straight_line_distance_to_b)
print(y)
print('-' * 40)

print("\nIf we add a connection from Lugoj to Sibiu at step cost 85:\n")
Problem.connect_states_both_ways(l, s, 85)
z = problem.a_star_graph_search(m,[b],straight_line_distance_to_b)
print(z)
print('-' * 40)