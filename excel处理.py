import pandas as pd
df = pd.read_excel(io=r'code.xls')
df.columns = ['错误列','专业名','院校名','投档计划数','最低位次']
df = df.drop(['错误列'], axis=1)
df['985 211'] = None
df['最高分专业'] = None
df['最低分专业'] = None

df211 = pd.read_csv('211.csv',header=None)#header=0不行
list211 = df211[0].to_list()
df985 = pd.read_csv('985.csv',header=None)#header=0不行
list985 = df985[0].to_list()

set_name = set()
len_set = 0

for index,row in df.iterrows():
    set_name.add(row['院校名'])
    if len(set_name) != len_set:
        row['最高分专业'] = '是'
        len_set = len(set_name)

    for name in list211:
        if name in row['院校名']:
            row['985 211'] = '211'
            break
    for name in list985:
        if name in row['院校名']:
            row['985 211'] = '985 '+row['985 211']
            break

df = df[::-1]
set_name = set()
for index,row in df.iterrows():
    set_name.add(row['院校名'])
    if len(set_name) != len_set:
        row['最低分专业'] = '是'
        len_set = len(set_name)
df = df[::-1]

df.to_excel('code_2336.xlsx')
print(1)
