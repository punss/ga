# from fuzzywuzzy import fuzz
# import random
# import string


# class Agent:
# 	"""docstring for Agent"""
# 	def __init__(self, length):
# 		super(Agent, self).__init__()
# 		self.string = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
# 		self.fitness = -1

# 	def __str__(self):
# 		return "String: " + str(self.string) + "Fitness: " + str(self.fitness)

# init_string = None
# init_string_length = None
# population = 200
# generations = 1000


# def ga():
# 	agents = init_agents(population, init_string_length)

# 	for generation in range(generations):
# 		print("generation: " + str(generation))

# 		agents = fitness(agents)
# 		agents = selection(agents)
# 		agents = crossover(agents)
# 		# agents = mutation(agents, 0.02)
# 		for agent in agents:
# 			agent = mutation(agent, 0.02)

# 		if (any(agents.fitness) >= 90 for agent in agents):
# 			print("Threshold met")
# 			exit(0)


# def init_agents(population, length):
# 	return [Agent(length) for _ in range(population)]


# def fitness(agents):
# 	for agent in agents:
# 		agent.fitness = fuzz.ratio(agent.string, init_string)

# 	return agents


# def selection(agents):
# 	agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True)
# 	print("\n".join(map(str, agents)))
# 	agents = agents[:int(0.2*len(agents))]
# 	return agents


# def crossover(agents):
# 	offspring = []

# 	for _ in range(int(population - int(len(agents))/2)):
# 		parentA = random.choice(agents)
# 		parentB = random.choice(agents)
# 		childA = Agent(init_string_length)
# 		childB = Agent(init_string_length)
# 		split = random.randint(0, init_string_length)
# 		childA = parentA.string[0:split] + parentB.string[split:init_string_length]
# 		childB = parentB.string[0:split] + parentA.string[split:init_string_length]

# 		offspring.append(childA)
# 		offspring.append(childB)
# 	agents.extend(offspring)
# 	return agents


# def mutation(agent, prob):
# 	# for agent in agents:
# 	idx = random.randint(0, init_string_length-1)
# 	mutate = random.random()
# 	if mutate <= prob:	
# 		letter_list = list(agent.string)
# 		letter_list[idx] = random.choice(string.ascii_lowercase)
# 		agent.string = "".join(letter_list)
# 	return agent
        
    


# if __name__ == '__main__':
# 	init_string = "hridik"
# 	init_string_length = len(init_string)
# 	ga()


from fuzzywuzzy import fuzz
import random
import string


class Agent:

    def __init__(self, length):

        self.string = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        self.fitness = -1

    def __str__(self):

        # return 'String: ' + str(self.string) + ' Fitness: ' + str(self.fitness)
        return None

in_str = None
in_str_len = None
population = 200
generations = 10000


def ga():

    agents = init_agents(population, in_str_len)

    for generation in range(generations):

        print('Generation: ' + str(generation))

        agents = fitness(agents)
        agents = selection(agents)
        agents = crossover(agents)
        agents = mutation(agents)
        agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True)
        print('Highest threshold: '+str(agents[0].string)+' Fitness: '+str(agents[0].fitness))

        if any(agent.fitness >= 95 for agent in agents):
            agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True)
            print('Highest threshold: '+str(agents[0].string)+' Fitness: '+str(agents[0].fitness))
            exit(0)


def init_agents(population, length):

    return [Agent(length) for _ in range(population)]


def fitness(agents):

    for agent in agents:

        agent.fitness = fuzz.ratio(agent.string, in_str)

    return agents


def selection(agents):

    agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True)
    print('\n'.join(map(str, agents)))
    agents = agents[:int(0.2 * len(agents))]

    return agents


def crossover(agents):

    offspring = []

    for _ in range(int((population - len(agents)) / 2)):

        parent1 = random.choice(agents)
        parent2 = random.choice(agents)
        child1 = Agent(in_str_len)
        child2 = Agent(in_str_len)
        split = random.randint(0, in_str_len)
        child1.string = parent1.string[0:split] + parent2.string[split:in_str_len]
        child2.string = parent2.string[0:split] + parent1.string[split:in_str_len]

        offspring.append(child1)
        offspring.append(child2)

    agents.extend(offspring)

    return agents


def mutation(agents):

    for agent in agents:

        for idx, param in enumerate(agent.string):

            if random.uniform(0.0, 1.0) <= 0.1:

                agent.string = agent.string[0:idx] + random.choice(string.ascii_lowercase) + agent.string[idx+1:in_str_len]

    return agents


if __name__ == '__main__':

    in_str = 'hridik'
    in_str_len = len(in_str)
    ga()