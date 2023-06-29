import matplotlib.pyplot as plt 
import numpy as np
import json

coordinates = []

def calc_mean_std_dev(data):
    means = []
    std_devs = []
    for d in data:
        means += [np.mean(d)]
        std_devs += [np.std(d)]
    return means, std_devs 

for i in range(30): 
    with open("graph/BEST/chainlengthbest" + str(i) + ".txt", 'r') as f:
        data = f.read().split('!')

    line_x = []
    line_y = []
    for element in data:
        element_json = json.loads(element)
        line_x += [int(element_json["time"])]
        line_y += [int(element_json["chainlength"])]

    coordinates += zip(line_x, line_y) 

minx = []
std_minx = []
meanx = []
std_maxx = []
maxx = []

for i in range(1,200): 
    list_i = [x for x,y in coordinates if y == i*10]
    std_devx = np.std(np.array(list_i))
    mean_x = np.mean(np.array(list_i))
    minx += [(min(list_i), i*10)]
    std_minx += [(mean_x-std_devx, i*10)]
    meanx += [(mean_x, i*10)]
    std_maxx += [(mean_x+std_devx, i*10)]
    maxx += [(max(list_i), i*10)]

plt.plot([x[0] for x in meanx], [x[1] for x in meanx], 'r-', label='mean_best')
#plt.plot([x[0] for x in minx], [x[1] for x in minx], 'r', linestyle="dotted", alpha=0.25)
#plt.plot([x[0] for x in maxx], [x[1] for x in maxx], 'r', linestyle="dotted", alpha=0.25)
plt.plot([x[0] for x in std_minx], [x[1] for x in std_minx], 'r', linestyle="dashed", alpha=0.5)
plt.plot([x[0] for x in std_maxx], [x[1] for x in std_maxx], 'r', linestyle="dashed", alpha=0.5)
# plt.plot(line_x, line_y, color="r", alpha=0.1)

coordinates = []

for i in range(30):
    with open('graph/RAND/chainlengthrand' + str(i) + '.txt', 'r') as f:
        data = f.read().split('!')
    
    line_x = []
    line_y = []
    for element in data:
        element_json = json.loads(element)
        line_x += [int(element_json["time"])]
        line_y += [int(element_json["chainlength"])]
    
    coordinates += zip(line_x, line_y) 

minx = []
std_minx = []
meanx = []
std_maxx = []
maxx = []

for i in range(1,200): 
    list_i = [x for x,y in coordinates if y == i*10]
    std_devx = np.std(np.array(list_i))
    mean_x = np.mean(np.array(list_i))
    minx += [(min(list_i), i*10)]
    std_minx += [(mean_x-std_devx, i*10)]
    meanx += [(mean_x, i*10)]
    std_maxx += [(mean_x+std_devx, i*10)]
    maxx += [(max(list_i), i*10)]

plt.plot([x[0] for x in meanx], [x[1] for x in meanx], 'b-', label='mean_rand')
#plt.plot([x[0] for x in minx], [x[1] for x in minx], 'b', linestyle="dotted", alpha=0.25)
#plt.plot([x[0] for x in maxx], [x[1] for x in maxx], 'b', linestyle="dotted", alpha=0.25)
plt.plot([x[0] for x in std_minx], [x[1] for x in std_minx], 'b', linestyle="dashed", alpha=0.5)
plt.plot([x[0] for x in std_maxx], [x[1] for x in std_maxx], 'b', linestyle="dashed", alpha=0.5)


plt.ylabel("Chain Length (in block)")
plt.xlabel("Timesteps")
plt.legend()
plt.rcParams['figure.figsize'] = [50,50]
plt.savefig('testresult.png', dpi=1000)
plt.show()
