import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.plot([1,2,3,4,5], [10,20,30,40,50])

print("on va ajouter des légendes sur le graphe")
plt.xlabel("unités")
plt.ylabel("dizaines")
plt.title("Un titre bien joli mais qui doit être un peu long non?")


plt.show()