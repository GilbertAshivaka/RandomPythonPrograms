import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(size= 1000)
sns.kdeplot(data, fill= True, color="blue")

plt.title("Density plot")
plt.ylabel("Value")
plt.xlabel("Density")
plt.show()