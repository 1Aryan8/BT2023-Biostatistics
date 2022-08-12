import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {'C':10, 'Fortran':6, 'SQL':15,
        'Python':35}
courses = list(data.keys())
values  = list(data.values())
  
fig = plt.figure()
#fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
#plt.bar(courses, values, color ='maroon')
plt.bar(courses, values, color=['C0', 'C1', 'C2', 'C3'],        width = 0.4)
 
plt.xlabel("Programming Languages")
plt.ylabel("No. of students enrolled")
plt.title("No. of students enrolled  vs. Favorite programming language")
plt.tight_layout()
plt.show()
#fig.savefig('bar.png', format='png',bbox_inches='tight',dpi=300)
