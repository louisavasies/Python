'''
Created on Mar 10, 2018

@author: Louis
'''
from problem.Problem import Problem
from ui.Console import Console
from controller.Controller import Controller

class App(object):
    def main(self):
        filename = "sudoku.txt"
        problem = Problem()
        problem.readFromFile(filename)

        contr = Controller(problem)

        cons = Console(contr)
        cons.mainMenu()



if __name__ == '__main__':
        app = App()
        app.main()