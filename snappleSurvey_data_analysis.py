# HIDDEN
from datascience import *
%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
import math
import numpy as np
from scipy import stats

table = Table.read_table('snapple_data')
table = table.drop(['•ÈÀV1','V2','V3','V4','V5','V6','V7','V8','V9','V10'])
table = table.relabel('Q2','Age')
table = table.relabel('Q5','City')
old_table = table
table = table.take(np.arange(1,len(table.rows)))
table = table.select('Age')

lst = []
flag = 0
def throw_nan(a):
    for i in range(0,len(a.rows)):
        if type(a['Age'][i]) is str:
            lst.append(i)
            
    return 
throw_nan(table)
lst = np.array(lst)
table = table.take(lst)


def str_to_num(a):
    return int(a)
table['Age'][195] = '17'
table['Age'][266] = '19'
table['Age'][472] = '51'

table['Age'] = table.apply(str_to_num,'Age')

#age distribution of people in the survey
#table.hist(bins = np.arange(15,80,1),normed = True)


table1 = Table([['0-20','21-30','31-40','41-50','51-60'],[1,2,3,4,5]],['Age brackets','percentage'])
table1
first = 0
second =0
third = 0
fourth = 0
fifth = 0
for i in range(0,len(table.rows)):
    if table['Age'][i]<20:
        first+=1
    elif table['Age'][i]<30:
        second+=1
    elif table['Age'][i]<40:
        third+=1
    elif table['Age'][i]<50:
        fourth+=1
    elif table['Age'][i]<60:
        fifth+=1

lst1 = [
first/len(table.rows),
second/len(table.rows), third/len(table.rows),
fourth/len(table.rows),
fifth/len(table.rows),
]
table1['percentage'] = lst1
# age bracket breakdown 
#table1.barh('Age brackets')

#old_table.select(['Age','Taste-Arizona','Taste - Snapple'])
#table2 = old_table.take(lst).select(['Age','Taste-Arizona','Taste - Snapple'])
table2 = table2.take(np.arange(1,len(table2.rows)))
table2['Age'][195] = '17'
table2['Age'][266] = '19'
table2['Age'][472] = '51'
table2['Age'] =table2.apply(str_to_num,'Age')

table2
# Category 1: 0 to 20
table_temp = table2.where(table2['Age']<21)
table_temp
snapple = 0
arizona = 0
table_temp
for i in range(0,len(table_temp.rows)):
       if type(table_temp['Taste-Arizona'][i]) is float:
            snapple+=1
       else:
            arizona+=1
print("0-20 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)

# Category 1: 21 to 30
table_temp = table2.where(table2['Age']<31)
table_temp = table_temp.where(table_temp['Age']>20)
table_temp
snapple = 0
arizona = 0
table_temp
for i in range(0,len(table_temp.rows)):
       if type(table_temp['Taste-Arizona'][i]) is float:
            snapple+=1
       else:
            arizona+=1
print("21-30 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)

# Category 1: 31 to 40
table_temp = table2.where(table2['Age']<41)
table_temp = table_temp.where(table_temp['Age']>30)
table_temp
snapple = 0
arizona = 0
table_temp
for i in range(0,len(table_temp.rows)):
       if type(table_temp['Taste-Arizona'][i]) is float:
            snapple+=1
       else:
            arizona+=1
print("31-40 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)

# Category 1:41 to 50
table_temp = table2.where(table2['Age']<51)
table_temp = table_temp.where(table_temp['Age']>40)
table_temp
snapple = 0
arizona = 0
table_temp
for i in range(0,len(table_temp.rows)):
       if type(table_temp['Taste-Arizona'][i]) is float:
            snapple+=1
       else:
            arizona+=1
print("41-50 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)

# Category 1:51 to 60
table_temp = table2.where(table2['Age']<61)
table_temp = table_temp.where(table_temp['Age']>50)
table_temp
snapple = 0
arizona = 0
table_temp
for i in range(0,len(table_temp.rows)):
       if type(table_temp['Taste-Arizona'][i]) is float:
            snapple+=1
       else:
            arizona+=1
print("51-60 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)
