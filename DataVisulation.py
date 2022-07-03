import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataframe = pd.DataFrame({'Name' : ['Dharma', 'Dharma', 'Dharma',
                                    'Mukesh', 'Mukesh', 'Mukesh' ,'Mukesh',
                                    'Mina', 'Mina'],
                          'Votes' : [12,23,24,
                                     23,23,25,25,
                                     24,23]})
dataframe.groupby(['Name']).sum().plot(kind='pie', autopct='%1.0f%%', y='Votes', startangle=90)


df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('1/1/2000',
periods=10), columns=list('ABCD'))
df.plot()



# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


#plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')
#plt.show()

#plt.plot([1, 5, 9, 4], [1, 20, 9, 40])
#plt.show()


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'rD')
#he axis function in the example above takes a list of [xmin, xmax, ymin, ymax] and specifies the viewport of the axes.
plt.axis([0, 7, 0, 25])
plt.show()


