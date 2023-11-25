import matplotlib.pyplot  as plt

#part a
#order is static, (dynamic,1), (dynamic,10), (dynamic,100)
data_mixed = [2806, 1009, 917, 888]
data_white = [125, 327, 126, 159]
data_black = [4774, 4559, 4512, 4486]

x_axis = ["static", "(dynamic,1)", "(dynamic,10)", "(dynamic,100)"]
#plot these data on different plots with different colors
# i want 3 different plots by the end
plt.plot(x_axis, data_mixed, color='green')

plt.xlabel('Scheduling Method')
#y label is time in milliseconds
plt.ylabel('Time (ms)')
#title is the graph title
plt.title('Scheduling Method vs Time')
#legend is the legend
plt.legend(['Mixed'])

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





 


