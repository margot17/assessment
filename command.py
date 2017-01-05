#!/usr/bin/env python
from argparse import ArgumentParser
from graph import greengraph
from map import Map
from matplotlib import pyplot as plt

    def process():
        parser = ArgumentParser()
        parser.add_argument('-c1','--city1',type=str,help='name of city1')
        parser.add_argument('-c2','--city2', type=str, help='name of city2')
        parser.add_argument('s','--steps',type=int, help='number of steps')
        arguments= parser.parse_args()
        print greengraph(arguments.city1, arguments.city2,
        arguments.steps)
        g=greengraph(arguments.city1, arguments.city2, arguments.steps)
        g_between=g.green_between(arguments.steps)
        
        plt.plot(g_between)
            plt.title('Green ratio:')
            plt.xlabel('Steps')
            plt.ylabel('Green ratio')
            plt.savefig('out.png')

    if __name__ == "__main__":
    process()
Writing command.py