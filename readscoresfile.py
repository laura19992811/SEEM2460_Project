import matplotlib.pylab as plt
from scipy.stats import pearsonr
import numpy as np
file = open("us_scores.txt","r")
file1 = open("us_vaccinated_dataset.txt","r")
scores = []
dates = {}
datesize = {}
for line in file:
    line= line.split()
    try:
        x = float(line[9].replace('}',''))
        adate = [int(p) for p in line[0].split('-')]
        maxval = max(adate)
        if len(str(adate[1])) != 2:
            adate[1] = '0'+str(adate[1])
        if adate.index(maxval) == 2:    #2021-02-05
            line[0] = str(adate[2]) + "-" + str(adate[1]) + "-" + str(adate[0])

        if line[0] not in dates:
            dates[line[0]] = x
            datesize[line[0]] = 1
        else:
            dates[line[0]] = dates[line[0]] + x
            datesize[line[0]] += 1
    except:
        pass

for k in dates:
    dates[k] = dates[k]/datesize[k]
flag = 0
actualvac = {}
for line in file1:
    if flag == 0:
        flag=1
        continue
    line = line.split(',')
    if line[1] not in actualvac and line[1] in dates:
        actualvac[line[1]] = int(line[-1])
    elif line[1] in actualvac:
        actualvac[line[1]] = actualvac[line[1]] + int(line[-1])

print(actualvac)
lists = sorted(dates.items()) # sorted by key, return a list of tuples
lists1 = sorted(actualvac.items())
x, y = zip(*lists) # unpack a list of pairs into two tuples
x1,y1 = zip(*lists1)
print(len(x))
print(len(y1))
fig, ax = plt.subplots()
ax.plot(x, y, label='Date')
ax.plot(x1, y1, label='Vaccines')
ax.xaxis.set_major_locator(plt.MaxNLocator(10))
ax.yaxis.set_major_locator(plt.MaxNLocator(3))
# Set up grid, legend, and limits
ax.legend(frameon=False)
#plt.plot(x, y)
plt.show()

scorelist = []
vaccinelist = []
for k,v in actualvac.items():
    scorelist.append(dates[k])
    vaccinelist.append(v)


corr, _ = pearsonr(scorelist, vaccinelist)
print('Pearsons correlation: %.3f' % corr)