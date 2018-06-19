from pprint import pprint
import json
import matplotlib.pyplot as plt
import pylab
import matplotlib.dates as mdates
from datetime import datetime

with open('monitoring.json') as f:
    monitoring_file = json.load(f)

graph_dict = {}

for x in sorted(monitoring_file['objects'][0]['rows']):
    if x[8] != None:
        y = x[1].split('.')
        time_stamp = datetime.strptime(y[0], "%Y-%m-%d %H:%M:%S")
        print(time_stamp)
        print(x[8])
        graph_dict[time_stamp] = x[8]

x_list = []
y_list = []

start_date = datetime(2018, 2, 16)
#end_date = datetime(2018, 2, 17)
end_date = datetime.today()

for key in list(graph_dict.keys()):
    if key < start_date or key > end_date:  #
        del graph_dict[key]

for value in list(sorted(graph_dict)):
    if graph_dict[value] != 0:
        x_list.append(value)
        y_list.append(graph_dict[value])

print(len(graph_dict.keys()))

pprint(graph_dict)

plt.plot(x_list,y_list,label=("Steps"))

plt.style.use('dark_background')
plt.rcParams['lines.linewidth'] = 1
plt.ylim(ymin=0)
#plt.title('Running Total - ' + str(input1) + ' days, Unit: ' + input2)
plt.legend()
plt.show()
