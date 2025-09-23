import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

### Basic Graph

x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 6, 8]

#Resize Graph
plt.figure(figsize=(5,3), dpi=300)#it has the size and it also has the pixel per inch

#linewidth is how wide the linear slope is, a marker to indicate each point, color of marker, style of the slope
#plt.plot(x, y, label='2x', color='red', linewidth=2, marker='.', linestyle='--', markersize=12, markeredgecolor='blue')

#Short hand notation
#fmt = '[color][marker][line]
plt.plot(x, y, 'b^--', label='2x')

##Line Number Two
x2 = np.arange(0,4.5,0.5)
plt.plot(x2[:6], x2[:6]**2, 'r', label='X^2') #it shows how far it goes to, it doesnt include 6, then it sqaures it and changes the color to red
plt.plot(x2[5:], x2[5:]**2, 'r--')#same but it includes 5 and it makes it dashed

#Title
plt.title("My First Graph", fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X Axis', fontdict={'fontname':'Comic Sans MS'})
plt.ylabel('Y Axis')

#Scale of the graph (x and y)
plt.xticks([0, 1, 2, 3, 4])
#plt.yticks([0, 2, 4, 6, 8, 10])

plt.legend()

plt.savefig('Private/mygraph1.png', dpi=300)

plt.show()

#Bar Chart
labels = ['A', 'B', 'C']
values = [1, 4, 2]

plt.bar(labels, values)

bars = plt.bar(labels, values)

patterns = ['/', 'O', '*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))

# bars[0].set_hatch('/')
# bars[1].set_hatch('O')
# bars[2].set_hatch('*')

plt.figure(figsize=(6,4))

plt.show()