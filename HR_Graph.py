from pprint import pprint
import json
import matplotlib.pyplot as plt
import pylab
import matplotlib.dates as mdates
from datetime import datetime

with open('HR_Data.json') as f:
    HR_Dict = json.load(f)

HR_final = {}

for x in sorted(HR_Dict['objects'][0]['rows']):
    y = x[0].split('.')
    time_stamp = datetime.strptime(y[0], "%Y-%m-%d %H:%M:%S")
    HR_final[time_stamp] = x[1]
    #pprint(x)

x_list = []
y_list = []

start_date = datetime(2018, 2, 16)
#end_date = datetime(2018, 2, 17)
end_date = datetime.today()

for key in list(HR_final.keys()):
    if key < start_date or key > end_date:  #
        del HR_final[key]

for value in HR_final:
    if HR_final[value] != 0:
        x_list.append(value)
        y_list.append(HR_final[value])

print(len(HR_final.keys()))

plt.plot(x_list,y_list,label=("HR"))

plt.style.use('dark_background')
plt.rcParams['lines.linewidth'] = 1
plt.ylim(ymin=0)
#plt.title('Running Total - ' + str(input1) + ' days, Unit: ' + input2)
plt.legend()
plt.show()
