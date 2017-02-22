import string
import random
import itertools

# Possible genes (whole character set)
charset = string.ascii_uppercase + " "

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
                # Nasty bug no 1: charset NOT state (generations won't variate)
                newGene = charset[random.randint(0, len(charset)-1)]        
                mutation += newGene
            else:
                mutation += state[j]                       
        mutations.append(mutation)
   
    return mutations

# Compute Hamming distance between two strings
def hamming(str1, str2):
  return sum(itertools.imap(str.__ne__, str1, str2))

# Live free or die
def fittest(mutations, target):
    min = numGenes+1
    fittest = None

    for m in mutations:
        d = hamming(m, target)
        if d<min:
            min = d
            fittest = m                                     

    # Nasty bug no 2: return fittest NOT m (generations won't evolve at all)) 
    return fittest                  

# While target not reached, evolve!
def evolve(numOffspring, mutationProb):
    cur = "".join(random.choice(charset) for _ in range(numGenes))
    fin = "METHINKS IT IS LIKE A WEASEL"
    
    gen = 0
    
    while cur != fin:
        offspring = mutate(cur, numOffspring, mutationProb)
        cur = fittest(offspring, fin)
        gen += 1
        print "[*] Gen %3d:" % gen, cur, hamming(cur, fin)


if __name__ == "__main__":
    # Number of offspring per generation
    numOffspring = 100

    # Probability that a gene (character) will mutate (percent)
    mutationProb = 5

    evolve(numOffspring, mutationProb)
