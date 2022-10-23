from cProfile import label
from turtle import color, shapesize
import matplotlib.pyplot as plt

apples_prod=[12,34,45,67]
plt.plot(apples_prod,[123,245,233,154],color='yellow',linestyle='--',label='Legend',linewidth=2,marker=7, markersize=9,markeredgecolor='red')

plt.xlabel('X axis label') # you can use the fontdict parameter like the one you used for title
plt.ylabel('y axis label') # you can use the fontdict parameter like the one you used for title
plt.title("This is tite",fontdict={'fontname':'Comic Sans MS','fontsize':18})
plt.xticks([10,20,30])
plt.yticks([100,200,300])

plt.legend()
plt.show()





