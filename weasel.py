import string
import random
import itertools

# Possible genes (whole character set)
charset = string.ascii_uppercase + "_"

# Number of genes (characters in the string)
numGenes = 28

# Create a next generation of mutated offspring 
def mutate(state, numOffspring, mutationProb):
    mutations = []

    for i in range(numOffspring):
        mutation = ""
        for j in range(numGenes):
            # Will character j be mutated?
            p = random.randint(1, 100)
            if p<=mutationProb:
                # (Possible) Nasty bug no 1: charset NOT state (generations won't variate)
                newGene = charset[random.randint(0, len(charset)-1)]        
                mutation += newGene
            else:
                mutation += state[j]                       
        mutations.append(mutation)
   
    return mutations

# Compute Hamming distance between two strings
def hamming(str1, str2):
  return sum(itertools.imap(str.__ne__, str1, str2))


# Select the fittest offspring from the pool
# (Live free or die - UNIX)
def fittest(mutations, target):
    min = numGenes+1
    fittest = None

    for m in mutations:
        d = hamming(m, target)
        if d<min:
            min = d
            fittest = m                                     

    # (Possible) Nasty bug no 2: return fittest NOT m (generations won't evolve at all)) 
    return fittest                  

# Colourise mutation based on distance from target
# (We don't care about performance so light the Christmas tree)
def colorise(mutation, target):
    W  = '\033[0m'  # white (normal)
    R  = '\033[31m' # red
    G  = '\033[32m' # green
  
    s = ""
    for i in range(len(mutation)):
        if mutation[i] == target[i]:
            s += G + mutation[i]
        else:
            s += R + mutation[i]
    s += W  
    return s

# While target not reached, evolve!
def evolve(numOffspring, mutationProb):
    cur = "".join(random.choice(charset) for _ in range(numGenes))
    fin = "METHINKS_IT_IS_LIKE_A_WEASEL"
    
    gen = 0
   
    print "%4s %28s %4s" % ("Gen", "Mutation", "Dist") 
    while cur != fin:
        offspring = mutate(cur, numOffspring, mutationProb)
        cur = fittest(offspring, fin)
        gen += 1
        print "%4d" % gen, colorise(cur, fin), hamming(cur, fin)


if __name__ == "__main__":
    # Number of offspring per generation
    numOffspring = 100

    # Probability that a gene (character) will mutate (percent)
    mutationProb = 5 

    evolve(numOffspring, mutationProb)
