import numpy as np
import matplotlib.pyplot as plt


# Graph for Correctness cases
 
# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
speaker = [28, 19, 20, 19, 17, 17, 29 ]
confine = [11, 13, 12, 14, 12, 10, 11 ]
docker_slim = [0, 19, 18, 19, 24, 17, 27 ] 
 
# Set position of bar on X axis
br1 = np.arange(len(speaker))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]


print(br1)
print(br2)

 
# # Make the plot
plt.bar(br1, speaker, color ='r', width = 0.15,
        edgecolor ='grey', label ='speaker')

plt.bar(br2, confine, color ='g', width = 0.15,
        edgecolor ='grey', label ='confine')

plt.bar(br3, docker_slim, color ='b', width = 0.15,
        edgecolor ='grey', label ='Slimtoolkit')
 
# Adding Xticks
plt.xlabel('Applications', fontweight ='bold', fontsize = 18)
plt.ylabel('Number of CVEs Mitigated', fontweight ='bold', fontsize = 18)
plt.xticks([r + barWidth for r in range(len(speaker))],
        ['mysql', 'nginx', 'httpd', 'redis', 'nodeJS', 'mongo', 'python'], fontsize=17)
 
plt.legend(prop={'size':15, 'weight':'bold'}, loc='upper center', bbox_to_anchor =(0.50, 1.15), ncol=3, fancybox=True)
# plt.show()
plt.savefig("CVEs.png")



barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# set height of bar
original = [142, 145, 117, 910, 594, 653, 907]
reduced =  [12.3, 8.68, 33.4, 99.2,98.4, 273, 20.6]
percentage = [ round(100-((reduced[i]/original[i])*100),2) for i in range(len(original))]
print(percentage)
# Set position of bar on X axis
br1 = np.arange(len(original))
br2 = [x + barWidth for x in br1]
# br3 = [x + barWidth for x in br2]
 
print(br1)
print(br2)

# Make the plot
# plt.bar(br1, original, color ='r', width = 0.15,
#         edgecolor ='grey', label ='original size')

plt.bar(br2, percentage, color ='g', width = 0.25,
        edgecolor ='grey')

# Adding Xticks

plt.xlabel('Applications', fontweight ='bold', fontsize = 18)
plt.ylabel('Percentage Size Reduction', fontweight ='bold', fontsize = 18)
plt.xticks([r + barWidth for r in range(len(original))],
        ['nginx', 'httpd', 'redis', 'nodeJS', 'mysql', 'mongo', 'python'], fontsize=17)
 

# plt.legend(prop={'size':15, 'weight':'bold'}, loc='upper center', bbox_to_anchor =(0.50, 1.15), ncol=3, fancybox=True)
# plt.show()
plt.savefig("size.png")




barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))

speaker = [100, 100, 100, 100, 100, 100, 100 ]
confine = [100, 100, 100, 100, 100, 100, 100 ]
docker_slim = [0, 100, 0, 100, 100, 100, 83 ]
 
# Set position of bar on X axis
br1 = np.arange(len(speaker))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
 
# # Make the plot
# plt.bar(br1, speaker, color ='r', width = 0.1,
#         edgecolor ='grey', label ='docker slim')
# plt.bar(br2, confine, color ='g', width = 0.1,
#         edgecolor ='grey', label ='confine')
# plt.bar(br3, docker_slim, color ='b', width = 0.1,
#         edgecolor ='grey', label ='speaker')

plt.bar(br1, speaker, color ='r', width = 0.15,
        edgecolor ='grey', label ='speaker')

plt.bar(br2, confine, color ='g', width = 0.15,
        edgecolor ='grey', label ='confine')

plt.bar(br3, docker_slim, color ='b', width = 0.15,
        edgecolor ='grey', label ='Slimtoolkit')
 
# Adding Xticks
plt.xlabel('Applications', fontweight ='bold', fontsize = 18)
plt.ylabel('% Tests Passed', fontweight ='bold', fontsize = 18)
plt.xticks([r + barWidth for r in range(len(speaker))],
        ['mysql', 'nginx', 'httpd', 'redis', 'nodeJS', 'mongo', 'python'], fontsize=17)
 
plt.legend(prop={'size':15, 'weight':'bold'}, loc='upper center', bbox_to_anchor =(0.50, 1.15), ncol=3, fancybox=True)
plt.savefig("tests.png")