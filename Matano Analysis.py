# This script calculates diffusivity coefficient D as a function of
# concentration c using the Matano analysis.
# Written by Seth Rutman.

import math
positionDataDictionary = {}

# These are arbitrary bounds, for some normalized distance -4 to 4
# This is also using a function given in Kinetics assignment 4. The concentration
# can be altered to be any function.
for number in range(40,-41,-1):
    positionDataDictionary[float(number)/10] = {'concentration' : (0.25)*(math.tanh(float(number)/10)+2)}

# Initialize leftmost position to 0 so the math doesn't explode
positionDataDictionary[sorted(positionDataDictionary)[len(positionDataDictionary)-1]]['derivative'] = 0
positionDataDictionary[sorted(positionDataDictionary)[len(positionDataDictionary)-1]]['integral'] = 0
positionDataDictionary[sorted(positionDataDictionary)[len(positionDataDictionary)-1]]['D'] = 0

# Calculate the left-derivative and left-integral necessary for the Matano Analysis
# Then calculate D per concentration

for number in range(len(sorted(positionDataDictionary))-2,-1,-1):
    changeOfPosition = sorted(positionDataDictionary)[number] - sorted(positionDataDictionary)[number+1]
    averageOfPosition = (sorted(positionDataDictionary)[number]+sorted(positionDataDictionary)[number+1])/2
    changeOfConcentration = positionDataDictionary[sorted(positionDataDictionary)[number]]['concentration'] - positionDataDictionary[sorted(positionDataDictionary)[number+1]]['concentration']
    derivative = changeOfPosition/changeOfConcentration
    integral = (averageOfPosition*changeOfConcentration)+positionDataDictionary[sorted(positionDataDictionary)[number+1]]['integral']
    positionDataDictionary[sorted(positionDataDictionary)[number]]['derivative'] = derivative
    positionDataDictionary[sorted(positionDataDictionary)[number]]['integral'] = integral
    positionDataDictionary[sorted(positionDataDictionary)[number]]['D'] = (-1)*derivative*integral
    


    
