import matplotlib.pyplot  as plt
'''
#part 2a1
x_axis = ["serial", "1 THREADS", 
           "2 THREADS", "4 THREADS", 
             "8 THREADS", "16 THREADS","32 THREADS"]
times = [115, 122, 173, 74, 47, 24, 19]

plt.plot(x_axis, times, color='green', marker='o')

plt.xlabel('Scheduling Method')
#y label is time in milliseconds
plt.ylabel('Time (ms)')
#title is the graph title
plt.title('Scheduling Method vs Time')
#legend is the legend
plt.legend(['hard3'])

#rotate the x axis labels
plt.xticks(rotation=45)

#show the graph
plt.show()
'''

#'''
#part 2a2
#plot of early termination
x_axis = ["serial", "1 THREADS", 
           "2 THREADS", "4 THREADS", 
             "8 THREADS", "16 THREADS","32 THREADS"]
times = [1.05, 6.66, 1.11, 1.07, 1.19, 1.82, 0.72]

plt.plot(x_axis, times, color='green', marker='o')

plt.xlabel('Scheduling Method')
#y label is time in milliseconds
plt.ylabel('Time (ms)')
#title is the graph title
plt.title('Scheduling Method vs Time')
#legend is the legend
plt.legend(['hard3'])

#rotate the x axis labels
plt.xticks(rotation=45)

#show the graph
plt.show()


#'''

'''
#part 2b
#two lines on the same plot
#one for serial, one for parallel
x_axis = ["hard1", "hard2", "hard3"]
data_serial = [83,153,166]
data_parallel = [10, 18, 19]

plt.plot(x_axis, data_serial, color='green', marker='o')
plt.plot(x_axis, data_parallel, color='red', marker='o')

plt.xlabel('Scheduling Method')
#y label is time in milliseconds
plt.ylabel('Time (ms)')
#title is the graph title
plt.title('Scheduling Method vs Time')
#legend is the legend
plt.legend(['Serial', 'Parallel'])

#rotate the x axis labels
plt.xticks(rotation=45)

#show the graph

plt.show()
'''