from collections import defaultdict

data=[]
with open('./input.csv','r') as f:
    data.extend([row.split(',')[0] for row in f])

regions=defaultdict(lambda: defaultdict(lambda: 0))
for i in data:
    temp = i.split('.')
    hostname=i.split('-')[0]
    regions[temp[1]][temp[2]]+=1
print('Region, environment, count')
for region in dict(regions):
    for env in regions[region]:
        print(f"{region},{env},{regions[region][env]}")