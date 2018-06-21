import matplotlib.pyplot as plt
import numpy as np
#import plotly.plotly as py

gaussian_numbers = np.random.normal(0,3,1000)
#plt.hist(gaussian_numbers)
bins_array = np.arange(-10,10,0.1)
count, bins, ignored = plt.hist(gaussian_numbers, bins = bins_array,density=True)
mu, sigma = 0,3
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
          linewidth=2, color='r')
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()