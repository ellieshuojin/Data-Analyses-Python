import nltk
from nltk.corpus import wordnet as wn

# synsets
synsCar = wn.synsets('car')
synsVehicle = wn.synsets('vehicle')

# initializing the max
maxSim = 0
for iCar in synsCar:
    for iVehicle in synsVehicle:
        simScore = iCar.wup_similarity(iVehicle)
        if simScore>maxSim:
            maxSim = simScore
            maxCar = iCar
            maxVehicle = iVehicle

# printing out the results
print(maxCar, ': ', end='')
print(maxCar.definition())
print(maxVehicle, ': ', end='')
print(maxVehicle.definition())
print('Similarity score: %6.4f' % maxSim)
