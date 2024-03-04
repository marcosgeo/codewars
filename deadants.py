
def dead_ant_count(ants):
    # Your code here
    ants = ants.split()
    heads = 0
    tails = 0
    bodies = 0
    for ant in ants:
        if ant != "ant":
            if "ant" in ant:
                ant = ant.replace("ant", "")
            heads += ant.count("a")
            tails += ant.count("t")
            bodies += ant.count("n")

    return max([heads, tails, bodies])


"""
OTHTER SOLUTIONS:

# Best solution
def dead_ant_count(ants):
    ants = ants.replace("ant", "")
    return max([ants.count("a"), ants.count("n"), ants.count("t")])


# Clever solution
def deadAntCount (ants):
    return max(ants.count('a'), ants.count('n'), ants.count('t')) - ants.count('ant')


"""
