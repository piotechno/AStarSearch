#Author: Figen Güngör
#Year: 2013
#Artifical Intelligence HW1: Implementation of A Star Graph Search Algorithm

from __future__ import print_function
from heapq import *

class State:
    def __init__(self, name):
        self.name = name
        self.actions = []
        self.is_goal = False

    def add_action(self, action):
        self.actions.append(action)

class Action:
    def __init__(self, name, next_state, step_cost):
        self.name = name
        self.next_state = next_state
        self.step_cost = step_cost

class Node:
    """Class that represents nodes in the search algorithm. Use the
    constructor to initialize the state, parent node, action at the parent
    node and the path cost. You should manually set the heuristic function value."""
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.heuristic = 0

    def copy_of(self, node):
        """You can use this function to update the frontier node when a better
path has been found. First update the frontier node by making it a
copy of the new child node. Then use heapq.heapify(self.__frontier) to
satisfy the heap condition."""
        self.__init__(node.state, node.parent, node.action, node.path_cost)
        self.heuristic = node.heuristic

    def __repr__(self):
        return 'Node({}, {})'.format(self.state.name, self.path_cost + self.heuristic)

    def __lt__(self, other):
        return (self.path_cost + self.heuristic) < (other.path_cost + other.heuristic)

class Problem:
    def __init__(self, name):
        self.__name = name
        self.__init_state = None
        self.__frontier = None
        self.__explored = None
        self.__goal_states = None
        self.__heuristic = None

    def a_star_graph_search(self, init_state, goal_states, heuristic):
        """Computest the A* graph search result from the initial state to the
closest of the states in the goal states list. heuristic parameter
should be a function that takes a node and returns the heuristic value
for that node. When a goal node has been reached it should call and
return the value of self.__solution(goal_node)."""
        
        #Update problem and create first node with given initial state 
        self.__init_state=init_state
        initialNode = Node(self.__init_state, None, None, 0)
        self.__frontier = [initialNode]
        self.__explored = set()
        self.__goal_states=goal_states
        self.__heuristic = heuristic
        
        #This is not necessary because if the destination is the initial state then it will find it at first pop
        #But I am just assigning the heuristic value to the initial node if heuristic is used.
        if self.__heuristic:
            initialNode.heuristic = self.__heuristic(initialNode)
        
        #Until frontier becomes empty, explore the nodes.
        while self.__frontier:
            
            #pop the node with lowest (path_cost+heuristic)
            node = heappop(self.__frontier) 
            
            #Check if the node's state is in goal states after popping from frontier
            if node.state in self.__goal_states:
                return self.__solution(node, len(self.__explored))  
            
            
            #Create new nodes with the actions from popped node.
            for action in node.state.actions:
                
                newNode = Node(action.next_state, node, action, node.path_cost+action.step_cost)
                
                if self.__heuristic:
                    newNode.heuristic = self.__heuristic(newNode)
                
                #this boolean is assigned true if newNode's state same with one of the node's state in frontier.
                inFrontier=False
                
                #If new node's state in explored list, it shouldn't be explored again, so it's not added to frontier.
                #For example, Arad and Zerind is connected both ways, so after Arad is explored, 
                #it creates nodes at Zerind, Sibiu and Timisoara and when Zerind is explored, it creates node at Arad, 
                #But it shouldn't be pushed to the frontier because Arad is already explored.
                #Arad -> Zerind -> Arad -> Zerind, the back and forth situation is prevented with explored list.
                if newNode.state not in self.__explored:
                
                    #if newNode's state is same with one of the node's state in frontier
                    #then the (path_cost+heuristic) of the nodes is compared and
                    #if new node is more economical, the node in the frontier will be updated with 
                    # new node's values.
                    #Otherwise, the newNode will not be added to frontier.
                    for n in self.__frontier:    
                        if n.state==newNode.state:
                            inFrontier=True
                            if newNode.__lt__(n):
                                n.copy_of(newNode) #after updating values of the node with new node
                                heapify(self.__frontier) # the heap should be sorted again.
                    
                    #If the node's state is not same with any of the node's state in frontier, just push it to frontier.
                    if not inFrontier:
                        heappush(self.__frontier, newNode)
                        
            #the node is explored, so it can be added to explored list.
            self.__explored.add(node.state)  
            
        return None                        
                                                       

    def __solution(self, goal_node, n_explored):
        """Returns a string representation of the solution containing the
state names and actions starting from the initial state to the given
goal node. It should also contain information about the path cost and
the number of explored nodes. """
        
        cost=goal_node.path_cost #path cost
        l=[]
        while goal_node.parent:
            l.insert(0,goal_node.state.name)
            l.insert(0,goal_node.action.name)
            goal_node=goal_node.parent
        l.insert(0,goal_node.state.name)
        s = '->'.join(l)
        return s+"\n(path_cost= "+str(cost)+", explored "+str(n_explored)+" nodes.)"

    def __print_diagnostics(self, node):
        """You can use this function to debug your code."""
        print('Explored node {}'.format(node))
        print('  Frontier: {}'.format(self.__frontier))

    @staticmethod
    def connect_states(source_state, dest_state, step_cost):
        source_initial = source_state.name[0].lower()
        dest_initial = dest_state.name[0].lower()
        action_name = source_initial + dest_initial
        source_state.add_action(Action(action_name, dest_state, step_cost))

    @staticmethod
    def connect_states_both_ways(state0, state1, step_cost):
        Problem.connect_states(state0, state1, step_cost)
        Problem.connect_states(state1, state0, step_cost)

if __name__ == '__main__':
    a = State('A')
    b = State('B')
    c = State('C')
    d = State('D')
    e = State('E')
    f = State('F')
    g = State('G')

    Problem.connect_states_both_ways(a, b, 10)
    Problem.connect_states_both_ways(a, d, 15)
    Problem.connect_states_both_ways(b, c, 120)
    Problem.connect_states_both_ways(d, e, 40)
    Problem.connect_states_both_ways(c, e, 70)
    Problem.connect_states_both_ways(c, f, 10)
    Problem.connect_states_both_ways(e, g, 140)
    Problem.connect_states_both_ways(g, f, 20)

    problem = Problem('small')

    print(problem.a_star_graph_search(a, [c], None))
    print(problem.a_star_graph_search(a, [g], None))
