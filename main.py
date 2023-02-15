import os
import random

from structure import solution, instance
from constructives import greedy, ctabu
from localsearch import lsfirstimprove
from algorithms import tabu
import datetime

def executeInstance():
    random.seed(1309)
    path = "instances/Amparo.csv"
    inst = instance.readInstance(path)
    sol = greedy.construct(inst)
    [best, bs] = tabu.execute(inst, 60, 5, sol)
    solution.printSol(best)

def executeDir():
    dir = "instances"
    with os.scandir(dir) as files:
        ficheros = [file.name for file in files if file.is_file() and file.name.endswith(".csv")]
    with open("resultados.csv", "w") as results:
        for f in ficheros:
            path = dir+"/"+f
            print("Solving "+f+": ", end="")
            inst = instance.readInstance(path)
            results.write(f+"\t"+str(inst['n'])+"\t")
            start = datetime.datetime.now()
            sol = greedy.construct(inst)
            [best, bs] = tabu.execute(inst, 60, 5, sol)
            [best2, bs2]= tabu.execute(inst, 240, 15, best)
            [best3, bs3]= tabu.execute(inst, 300, 25, best2)
            [final, bs4] = tabu.execute(inst, 300, 50, best3)
            elapsed = datetime.datetime.now() - start
            secs = round(elapsed.total_seconds(),2)
            #print(str(bs['of'])+"\t"+str(secs))
            print(str(bs4) + "\t" + str(secs))
            #results.write(str(round(bs['of'],2))+"\t" + str(secs) + "\n")
            results.write(str(round(bs4, 2)) + "\t" + str(secs) + "\n")


if __name__ == '__main__':
    #executeInstance()
    executeDir()