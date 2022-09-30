import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Initialize an empty list to store moving averages
moving_averages = []

data=pd.read_csv("BTC-USD-3M.csv")

closingPrice = data['Adj Close']
closingPrice=closingPrice.values


# every window of size ...
window_size = 10

# Loop through the array to consider
i = 0
while i + window_size <= len(closingPrice):
    
    # Store elements from i to i+window_size
    # in list to get the current window
    window = closingPrice[i : i + window_size]
  
    # Calculate the average of current window
    window_average = round(sum(window) / window_size, 2)
      
    # Store the average of current
    # window in moving average list
    moving_averages.append(window_average)
      
    # Shift window to right by one position
    i += 1
    
print(moving_averages)

nan_list = []
for x in range(0, window_size-1,1):
    nan_list.append(np.NaN)

moving_averages = nan_list + moving_averages

data=data.assign(Moving_average=pd.Series(moving_averages,index=data.index))

fig1=plt.figure(figsize=(10,8))
ax1=fig1.add_subplot(111)
data['Adj Close'].plot(ax=ax1, color='b', lw=3, legend=True)
data['Moving_average'].plot(ax=ax1, color='r', lw=3, legend=True)
plt.show()