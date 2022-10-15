from collections import defaultdict

data=[]
with open('./input.csv','r') as f:
    data.extend([row.split(',')[0] for row in f])

# regions=defaultdict(lambda: defaultdict(lambda: 0))
# for i in data:
#     temp = i.split('.')
#     hostname=i.split('-')[0]
#     regions[temp[1]][temp[2]]+=1
# print('Region, environment, count')
# for region in dict(regions):
#     for env in regions[region]:
#         print(f"{region},{env},{regions[region][env]}")


i_region = "use1"
i_env = "prod"
existing_host_seq=[i.split('-')[0][4:] for i in data if (i.split('.')[1]==i_region and i.split('.')[2]==i_env)]
missing_host_seq=[i_seq for i_seq in range(10,51) if str(i_seq) not in existing_host_seq]
print('\n'.join(missing_host_seq))
