from collections import defaultdict

def template(seq, region, env):
    return f'host{seq}-1001.{region}.{env}.internal.example.com'

print("================== Solving Question 1 ==================")
input_csv_path= str(input("Enter the input csv path (Leave blank for choosing input.csv in current dir): ") or "./input.csv")
data=[]
with open(input_csv_path,'r') as f:
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


print("================== Solving Question 2 ==================")
i_region=str(input("Enter the interested region in dataset (Leave blank for choosing 'use1' region): ") or "use1")
i_env = str(input("Enter the interested environment in dataset (Leave blank for choosing 'prod' environment): ") or "prod")
existing_host_seq=[i.split('-')[0][4:] for i in data if (i.split('.')[1]==i_region and i.split('.')[2]==i_env)]
missing_host_seq=[template(i_seq,i_region,i_env) for i_seq in range(10,51) if str(i_seq) not in existing_host_seq]
print(f"Unused hostnames in environment {i_env} of region {i_region}")
print('\n'.join(missing_host_seq))
