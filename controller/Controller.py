'''
Created on Mar 10, 2018

@author: Louis
'''
from queue import Queue
from state.State import State

class Controller(object):
    def __init__(self, problem):
        self.instance = problem
        
    def orderStates(self, states):
        for state in states:
            self.writeState(self.problem, state)
            print("\n")
            
    def BFS(self, problem):
        state = State(problem.initialState)
        print("state: ", state.state)
        if problem.goal_test(state.state):
            return state
        
        frontier = Queue()
        frontier.put(state)
        
        
        # Loop until all nodes are explored or solution found
        while (frontier.qsize() != 0):

            node = frontier.get()
            print("node: ", node)
            for child in node.expandState(problem):
                if problem.goal_test(child):
                    return child
    
                frontier.put(child)
                print("Child: ", child)
        
                
        return None
    

        