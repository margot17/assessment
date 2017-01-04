#!/usr/bin/env python
from argparse import ArgumentParser
import greengraph
# The code greengraph should change the same except from the fact
#that  in _init_ I would add the variable 'steps' fos compatibility with this script
#also I would change the locations to London and Oxford
    def process():
        parser = argparse.ArgumentParser()
        parser.add_argument('-c1','--city1',type=str,help='name of city1')
        parser.add_argument('-c2','--city2', type=str, help='name of city2')
        parser.add_argument('s','--steps',type=int, help='number of steps')
        arguments= parser.parse_args()
        print greengraph(arguments.city1, arguments.city2,
        arguments.steps)

    if __name__ == "__main__":
    process()
Writing command.py