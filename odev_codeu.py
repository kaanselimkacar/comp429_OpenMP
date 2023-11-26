import matplotlib.pyplot  as plt
'''
#part a
#order is static, (dynamic,1), (dynamic,10), (dynamic,100)
data_mixed = [2806, 1009, 917, 888]
data_white = [125, 327, 126, 159]
data_black = [4774, 4559, 4512, 4486]

x_axis = ["static", "(dynamic,1)", "(dynamic,10)", "(dynamic,100)"]
'''
#'''
#part b
x_axis = ["serial", "1 THREADS",
           "2 THREADS", "4 THREADS",
             "8 THREADS", "16 THREADS","32 THREADS"]
data_mixed = [24146, 24323, 19322, 13984, 8572, 4846, 2727]
data_white = [137, 137, 107, 99, 58, 32, 83]
data_black = [129915, 130041, 65606, 33565, 17466, 9150, 4809]
#'''

#plot these data on different plots with different colors
# i want 3 different plots by the end
plt.plot(x_axis, data_mixed, color='green', marker='o')

plt.xlabel('Scheduling Method')
#y label is time in milliseconds
plt.ylabel('Time (ms)')
#title is the graph title
plt.title('Scheduling Method vs Time')
#legend is the legend
plt.legend(['Mixed'])

#rotate the x axis labels
plt.xticks(rotation=45)

#show the graph
plt.show()

plt.plot(x_axis, data_white, color='red')

plt.xlabel('Scheduling Method')
#y label is time in milliseconds
plt.ylabel('Time (ms)')
#title is the graph title
plt.title('Scheduling Method vs Time')
#legend is the legend
plt.legend(['White'])

#show the graph
plt.show()

plt.plot(x_axis, data_black, color='blue')

plt.xlabel('Scheduling Method')
#y label is time in milliseconds
plt.ylabel('Time (ms)')
#title is the graph title
plt.title('Scheduling Method vs Time')
#legend is the legend
plt.legend(['Black'])

#show the graph
plt.show()








 


