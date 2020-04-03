from Domain.GA import GA
from Repository.readData import readData2, readData1


def run():
    while True:
        print("1. Run \n")
        print("0. Exit\n")
        print("Introduceti comanda:\n")

        cmd = input()
        if cmd == "1":
            print("Introduceti numele fisierului: \n")
            filename = input()
            if (filename != ""):
                print("Marimea populatiei = \n")
                populationSize = int(input())
                print("Numarul de generatii = \n")
                noGenerations = int(input())
                if filename == "150p_eil51.txt":
                    graph = readData2(filename)
                else:
                    graph = readData1(filename)
                ga = GA(populationSize, graph)
                ga.initialization()
                contor = 0
                gen = contor + 1
                contor +=1
                best = ga.bestChromosome()
                print("generation " + str(gen) + " " + str(best.repres) + " fitness " + str(best.fitness))
                while (contor < noGenerations):
                    ga.oneGenerationElitism()
                    best = ga.bestChromosome()
                    gen = contor + 1
                    print("generation " + str(gen) + " " + str(best.repres) + " fitness "+str(best.fitness))
                    contor += 1
        else:
            break


run()