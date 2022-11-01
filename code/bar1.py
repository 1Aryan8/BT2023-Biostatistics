from cgitb import grey
import numpy as np
import matplotlib.pyplot as plt

#setiing width of the bar 
barWidth = 0.25
fig = plt.subplots(figsize = (12, 8))

#Set height of the bar
BT = [12, 30, 1, 8, 22]
BI = [30, 40, 50, 60, 70]
BM = [1, 2, 0, 5, 6]

#Set position of bar on the X-axis
br1 = np.arange(len(BT))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]

#Making the plot
plt.bar(br1, BT, color = 'red', width = barWidth, edgecolor = 'black', label = 'BT')
plt.bar(br2, BI, color = 'orange', width = barWidth, edgecolor = 'black', label = 'BI')
plt.bar(br3, BM, color = 'yellow', width = barWidth, edgecolor = 'black', label = 'BM')

#Ticks and Labels
plt.xlabel('Branch', fontweight = 'bold', fontsize = 15)
plt.ylabel('Placements', fontweight = 'bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(BT))], ['2017', '2018', '2019', '2020', '2021'])


plt.legend()
plt.show()
