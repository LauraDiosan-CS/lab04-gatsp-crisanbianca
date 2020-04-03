from random import randint

from Domain.Chromosome import Chromosome


class GA:

    def __init__(self, populationSize, problParam):
        self.__populationSize = populationSize
        self.__problParam = problParam
        self.__population = []

    def initialization(self):
        for _ in range(0, self.__populationSize):
            c = Chromosome(self.__problParam)
            self.__population.append(c)
        self.evaluation(self.__population)


    def evaluation(self, list):
        for c in list:
            dist = 0
            matrix = self.__problParam['mat']
            for i in range(len(c.repres) - 1):
                dist += matrix[c.repres[i]][c.repres[i + 1]]
            dist += matrix[c.repres[len(c.repres) - 1]][c.repres[0]]
            c.fitness = dist

    def worstChromosome(self):
        worst = self.__population[0]
        for c in self.__population:
            if c.fitness > worst.fitness:
                worst = c
        return worst

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if c.fitness < best.fitness:
                best = c
        return best

    def selection(self):
        pos1 = randint(0, self.__populationSize - 1)
        pos2 = randint(0, self.__populationSize - 1)
        if (self.__population[pos1].fitness < self.__population[pos2].fitness):
            return pos1
        else:
            return pos2


    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        for _ in range(self.__populationSize):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation(self.__population)
