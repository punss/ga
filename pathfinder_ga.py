import numpy as np
import random


class Gene:
    def __init__(self, length):
        self.path = [0]
        self.fitness = -1


def initialise_map(N):
    map_array = np.zeros((N, N))
    for i in range(0, N):
        for j in range(0, i):
            map_array[i][j] = random.random()
            map_array[j][i] = map_array[i][j]
    return map_array


def create_route(N):
    gene = Gene(N)
    temp = np.arange(1, N)
    np.random.shuffle(temp)
    gene.path.extend(list(temp))
    return gene

POPULATION_SIZE = 100
NUMBER_OF_NODES = 100
NUMBER_OF_GENERATIONS = 5000
CROSSOVER_RATE = 0.2
best_route = Gene(NUMBER_OF_NODES)


def create_init_pop(population):
    gene_pool = []
    for i in range(population):
        gene_pool.append(create_route(NUMBER_OF_NODES))
    return gene_pool


def calculate_fitness(gene_pool, map_array):
    for gene in gene_pool:
        score = 0
        for i in range(0, len(gene.path) - 1):
            score += map_array[gene.path[i]][gene.path[i+1]]
        gene.fitness = score
    gene_pool = sorted(gene_pool, key=lambda gene: gene.fitness)
    return gene_pool


def selection(gene_pool):
    gene_pool = sorted(gene_pool, key=lambda gene: gene.fitness)
    new_pool = gene_pool[:int(CROSSOVER_RATE * POPULATION_SIZE)]
    return new_pool


def crossover(gene_pool):
    for _ in range(int((1-CROSSOVER_RATE) * POPULATION_SIZE)):
        parentA = random.choice(gene_pool)
        parentB = random.choice(gene_pool)
        childA = Gene(NUMBER_OF_NODES)
        childB = Gene(NUMBER_OF_NODES)

        cut_idx = random.randint(1, NUMBER_OF_NODES-1)

        remainder_path = list(np.arange(NUMBER_OF_NODES))
        for element in parentA.path[:cut_idx]:
            remainder_path.remove(element)
        childA.path = parentA.path[:cut_idx] + remainder_path

        remainder_path = list(np.arange(NUMBER_OF_NODES))
        for element in parentB.path[:cut_idx]:
            remainder_path.remove(element)
        childB.path = parentB.path[:cut_idx] + remainder_path

        gene_pool.append(childA)
        gene_pool.append(childB)

    return gene_pool


def mutate(gene_pool, prob):
    for gene in gene_pool:
        dice = random.random()
        if dice <= prob:
            idx = random.randint(1, NUMBER_OF_NODES-1)
            ele = gene.path[idx]
            new_ele = random.randint(1, NUMBER_OF_NODES-1)
            new_idx = gene.path.index(new_ele)
            gene.path[idx] = new_ele
            gene.path[new_idx] = ele
    return gene_pool


def check_completion(gene_pool):
    if best_route.fitness == -1:
        gene_pool = sorted(gene_pool, key=lambda gene: gene.fitness)
        best_route.fitness = gene_pool[0].fitness
        best_route.path = gene_pool[0].path
        print("Best route: " + str(best_route.path) + " Distance: " + str(
            best_route.fitness))
    else:
        if gene_pool[0].fitness < best_route.fitness:
            best_route.fitness = gene_pool[0].fitness
            best_route.path = gene_pool[0].path
            print("Best route: " + str(best_route.path) + " Distance: " + str(
                best_route.fitness))

    # print("Best route: " + str(gene_pool[0].path) + " Distance: " + str(
    #     gene_pool[0].fitness))


def main():
    DIST_LIST = initialise_map(NUMBER_OF_NODES)
    route_pool = create_init_pop(POPULATION_SIZE)
    route_pool = calculate_fitness(route_pool, DIST_LIST)
    check_completion(route_pool)
    for gen in range(NUMBER_OF_GENERATIONS):
        # print("Generation: " + str(gen) + "\n")
        route_pool = selection(route_pool)
        route_pool = crossover(route_pool)
        route_pool = mutate(route_pool, 0.2)
        calculate_fitness(route_pool, DIST_LIST)
        check_completion(route_pool)
    print("The most optimised route was: " + str(
        best_route.path
        ) + " distance covered: " + str(best_route.fitness))

if __name__ == "__main__":
    main()
