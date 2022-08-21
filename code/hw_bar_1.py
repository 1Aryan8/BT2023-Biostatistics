#from cProfile import label
from tkinter import font
import numpy as np
import matplotlib.pyplot as plt

#x = ['2003-04', '2004-05', '2005-06', '2006-07', '2007-08', '2008-09', '2009-10', '2010-11'] 

y = [57.1, 59.2, 60.8, 62.7, 63.2, 63.6, 61.9, 63.6]
z = [78.0, 81.1, 84.3, 86.8, 88.1, 88.9, 85.1, 89.4]


n = 8
r = np.arange(n) 
width = 0.25\

plt.bar(r, y, color = 'purple', width=width, label = "Gross irrigated area")
plt.bar(r + width , z, color = 'orange', width=width, label = "Net irrigated area")

# naming y axis
plt.ylabel('Irrigated area (in million hectares)')
plt.ylim((0, 100))

# naming x axis
plt.xlabel('Years')
plt.title('Irrigated Area in Each Year')

plt.xticks(r + width/2, ['2003-04', '2004-05', '2005-06', '2006-07', '2007-08', '2008-09', '2009-10', '2010-11'], rotation = 45)
plt.legend()

plt.show()