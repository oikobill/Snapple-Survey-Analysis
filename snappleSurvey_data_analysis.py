# HIDDEN
from datascience import *
%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
import math
import numpy as np
from scipy import stats

#table = Table.read_table('snapple_data')
table = table.drop(['•ÈÀV1','V2','V3','V4','V5','V6','V7','V8','V9','V10'])
table = table.relabel('Q2','Age')
table = table.relabel('Q5','City')
original_table = table
array = table['Age']
old_table = table
table = table.take(np.arange(1,len(table.rows)))
old_table['Age'][203] = '17'
old_table['Age'][274] = '19'
old_table['Age'][480] = '51'
old_table['Age'][815] = '55'
old_table['Age'][1404] = '51'
old_table['Age'][1429] = '21'
table = Table([[]],['Age'])
table['Age'] = old_table['Age']


lst = []
def throw_nan(a):
    for i in range(0,len(a.rows)):
        if type(a['Age'][i]) is str:
            lst.append(i)
            
    return 
throw_nan(table)
table = table.take(lst)
table = table.take(np.arange(1,len(table.rows)))


def str_to_num(a):
    return int(a)
table['Age'] = table.apply(str_to_num,'Age')

#age distribution of people in the survey
table.hist(bins = np.arange(15,80,1),normed = True)


table1 = Table([['15-20','21-30','31-40','41-50','51-60'],[1,2,3,4,5]],['Age brackets','percentage'])
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
table1.barh('Age brackets')

old_table = old_table.relabel('Q52_1_1','Taste-Arizona')
old_table =old_table.relabel('Q52_1_2','Taste-Snapple')
old_tabe = old_table.relabel('Q52_1_3','Taste-N/O')

lst = []
def throw_nan(a):
    for i in range(0,len(a.rows)):
        if type(a['Age'][i]) is str:
            lst.append(i)
            
    return 
throw_nan(old_table)
old_table = old_table.take(lst)
old_table = old_table.take(np.arange(1,len(table.rows)-1))

table2 = old_table.select(['Age','Taste-Arizona','Taste-Snapple'])
table2 = table2.take(np.arange(1,len(table2.rows)))
table2['Age'] =table2.apply(str_to_num,'Age')


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
print("TASTE RANKINGS")
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

#table3 = old_table.relabel('Q52_2_1','Health-Arizona')

old_table = old_table.relabel('Q52_2_1','Health-Arizona')
old_table = old_table.relabel('Q52_2_2','Health-Snapple')
old_table = old_table.relabel('Q52_2_3','Health-N/O')

print("HEALTHINESS RANKINGS")

table3 = old_table
table3 = table3.select(['Age','Health-Snapple','Health-N/O','Health-Arizona'])
table3 = table3.take(np.arange(1,len(table3.rows)))
table2 = table2.take(np.arange(1,len(table2.rows)))
table3['Age'][195] = '17'
table3['Age'][266] = '19'
table3['Age'][472] = '51'
table3['Age'] = table3.apply(str_to_num,'Age')
# Category 1: 0 to 20
table_temp = table3.where(table3['Age']<21)
table_temp
snapple = 0
arizona = 0
no = 0
table_temp
for i in range(0,len(table_temp.rows)):
       if type(table_temp['Health-Arizona'][i]) is float and type(table_temp['Health-Snapple'][i]) is float:
            no+=1
       elif type(table_temp['Health-Snapple'][i]) is float:
            arizona+=1
       else:
            snapple+=1

print("0-20 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)
print("No Opinion:", no)

# Category 1: 21 to 30
table_temp = table3.where(table3['Age']<31)
table_temp = table_temp.where(table_temp['Age']>20)
table_temp
snapple = 0
arizona = 0
no = 0
table_temp
for i in range(0,len(table_temp.rows)):
       if type(table_temp['Health-Arizona'][i]) is float and type(table_temp['Health-Snapple'][i]) is float:
            no+=1
       elif type(table_temp['Health-Snapple'][i]) is float:
            arizona+=1
       else:
            snapple+=1
print("21-30 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)
print("No Opinion:", no)


# Category 1: 31 to 40
table_temp = table3.where(table3['Age']<41)
table_temp = table_temp.where(table_temp['Age']>30)
table_temp
snapple = 0
arizona = 0
no = 0
table_temp
for i in range(0,len(table_temp.rows)):
       if type(table_temp['Health-Arizona'][i]) is float and type(table_temp['Health-Snapple'][i]) is float:
            no+=1
       elif type(table_temp['Health-Snapple'][i]) is float:
            arizona+=1
       else:
            snapple+=1
print("31-40 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)
print("No Opinion:", no)

# Category 1:41 to 50
table_temp = table3.where(table3['Age']<51)
table_temp = table_temp.where(table_temp['Age']>40)
table_temp
snapple = 0
arizona = 0
no = 0
table_temp
for i in range(0,len(table_temp.rows)):
      if type(table_temp['Health-Arizona'][i]) is float and type(table_temp['Health-Snapple'][i]) is float:
            no+=1
      elif type(table_temp['Health-Snapple'][i]) is float:
            arizona+=1
      else:
            snapple+=1
print("41-50 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)
print("No Opinion:", no)

# Category 1:51 to 60
table_temp = table3.where(table3['Age']<61)
table_temp = table_temp.where(table_temp['Age']>50)
table_temp
snapple = 0
arizona = 0
no = 0
table_temp
for i in range(0,len(table_temp.rows)):
      if type(table_temp['Health-Arizona'][i]) is float and type(table_temp['Health-Snapple'][i]) is float:
            no+=1
      elif type(table_temp['Health-Snapple'][i]) is float:
            arizona+=1
      else:
            snapple+=1
print("51-60 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)
print("No Opinion:", no)

old_table = old_table.relabel('Q52_3_1','Brand-Arizona')
old_table = old_table.relabel('Q52_3_2','Brand-Snapple')
old_table = old_table.relabel('Q52_3_3','Brand-N/O')

######## Brand Image 
print("BRAND IMAGE")

table4 = old_table
table4 = table4.select(['Age','Brand-Snapple','Brand-N/O','Brand-Arizona'])
table4 = table4.take(np.arange(1,len(table4.rows)))

table4['Age'][195] = '17'
table4['Age'][266] = '19'
table4['Age'][472] = '51'
table4['Age'] = table4.apply(str_to_num,'Age')
# Category 1: 0 to 20
table_temp = table4.where(table4['Age']<21)
table_temp
snapple = 0
arizona = 0
no = 0
table_temp
for i in range(0,len(table_temp.rows)):
       if type(table_temp['Brand-Arizona'][i]) is float and type(table_temp['Brand-Snapple'][i]) is float:
            no+=1
       elif type(table_temp['Brand-Snapple'][i]) is float:
            arizona+=1
       else:
            snapple+=1

print("0-20 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)
print("No Opinion:", no)

# Category 1: 21 to 30
table_temp = table4.where(table4['Age']<31)
table_temp = table_temp.where(table_temp['Age']>20)
table_temp
snapple = 0
arizona = 0
no = 0
table_temp
for i in range(0,len(table_temp.rows)):
       if type(table_temp['Brand-Arizona'][i]) is float and type(table_temp['Brand-Snapple'][i]) is float:
            no+=1
       elif type(table_temp['Brand-Snapple'][i]) is float:
            arizona+=1
       else:
            snapple+=1
print("21-30 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)
print("No Opinion:", no)


# Category 1: 31 to 40
table_temp = table4.where(table3['Age']<41)
table_temp = table_temp.where(table_temp['Age']>30)
table_temp
snapple = 0
arizona = 0
no = 0
table_temp
for i in range(0,len(table_temp.rows)):
       if type(table_temp['Brand-Arizona'][i]) is float and type(table_temp['Brand-Snapple'][i]) is float:
            no+=1
       elif type(table_temp['Brand-Snapple'][i]) is float:
            arizona+=1
       else:
            snapple+=1
print("31-40 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)
print("No Opinion:", no)

# Category 1:41 to 50
table_temp = table4.where(table4['Age']<51)
table_temp = table_temp.where(table_temp['Age']>40)
table_temp
snapple = 0
arizona = 0
no = 0
table_temp
for i in range(0,len(table_temp.rows)):
      if type(table_temp['Brand-Arizona'][i]) is float and type(table_temp['Brand-Snapple'][i]) is float:
            no+=1
      elif type(table_temp['Brand-Snapple'][i]) is float:
            arizona+=1
      else:
            snapple+=1
print("41-50 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)
print("No Opinion:", no)

# Category 1:51 to 60
table_temp = table4.where(table4['Age']<61)
table_temp = table_temp.where(table_temp['Age']>50)
table_temp
snapple = 0
arizona = 0
no = 0
table_temp
for i in range(0,len(table_temp.rows)):
      if type(table_temp['Brand-Arizona'][i]) is float and type(table_temp['Brand-Snapple'][i]) is float:
            no+=1
      elif type(table_temp['Brand-Snapple'][i]) is float:
            arizona+=1
      else:
            snapple+=1
print("51-60 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)
print("No Opinion:", no)

#Overall 
old_table = old_table.relabel('Q52_4_1','Overall-Arizona')
old_table = old_table.relabel('Q52_4_2','Overall-Snapple')
old_table = old_table.relabel('Q52_4_3','Overall-N/O')

######## Overall Image 
print("OVERALL RANKING")

table5 = old_table
table5 = table5.select(['Age','Overall-Snapple','Overall-N/O','Overall-Arizona'])
table5 = table5.take(np.arange(1,len(table5.rows)))

table5['Age'][195] = '17'
table5['Age'][266] = '19'
table5['Age'][472] = '51'
table5['Age'] = table5.apply(str_to_num,'Age')
# Category 1: 0 to 20
table_temp = table5.where(table5['Age']<21)
table_temp
snapple = 0
arizona = 0
no = 0
table_temp
for i in range(0,len(table_temp.rows)):
       if type(table_temp['Overall-Arizona'][i]) is float and type(table_temp['Overall-Snapple'][i]) is float:
            no+=1
       elif type(table_temp['Overall-Snapple'][i]) is float:
            arizona+=1
       else:
            snapple+=1

print("0-20 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)
print("No Opinion:", no)

# Category 1: 21 to 30
table_temp = table5.where(table5['Age']<31)
table_temp = table_temp.where(table_temp['Age']>20)
table_temp
snapple = 0
arizona = 0
no = 0
table_temp
for i in range(0,len(table_temp.rows)):
       if type(table_temp['Overall-Arizona'][i]) is float and type(table_temp['Overall-Snapple'][i]) is float:
            no+=1
       elif type(table_temp['Overall-Snapple'][i]) is float:
            arizona+=1
       else:
            snapple+=1
print("21-30 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)
print("No Opinion:", no)


# Category 1: 31 to 40
table_temp = table5.where(table5['Age']<41)
table_temp = table_temp.where(table_temp['Age']>30)
table_temp
snapple = 0
arizona = 0
no = 0
table_temp
for i in range(0,len(table_temp.rows)):
       if type(table_temp['Overall-Arizona'][i]) is float and type(table_temp['Overall-Snapple'][i]) is float:
            no+=1
       elif type(table_temp['Overall-Snapple'][i]) is float:
            arizona+=1
       else:
            snapple+=1
print("31-40 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)
print("No Opinion:", no)

# Category 1:41 to 50
table_temp = table5.where(table5['Age']<51)
table_temp = table_temp.where(table_temp['Age']>40)
table_temp
snapple = 0
arizona = 0
no = 0
table_temp
for i in range(0,len(table_temp.rows)):
      if type(table_temp['Overall-Arizona'][i]) is float and type(table_temp['Overall-Snapple'][i]) is float:
            no+=1
      elif type(table_temp['Overall-Snapple'][i]) is float:
            arizona+=1
      else:
            snapple+=1
print("41-50 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)
print("No Opinion:", no)

# Category 1:51 to 60
table_temp = table5.where(table5['Age']<61)
table_temp = table_temp.where(table_temp['Age']>50)
table_temp
snapple = 0
arizona = 0
no = 0
table_temp
for i in range(0,len(table_temp.rows)):
      if type(table_temp['Overall-Arizona'][i]) is float and type(table_temp['Overall-Snapple'][i]) is float:
            no+=1
      elif type(table_temp['Overall-Snapple'][i]) is float:
            arizona+=1
      else:
            snapple+=1
print("51-60 age range")           
print("Arizona lovers:",arizona)
print("Snapple lovers:", snapple)
print("No Opinion:", no)

# examining correlation 
# everything is expressedin terms of percentages of how many people chose snapple 
#over the total number of people who responded
import matplotlib.pyplot as plt

health = [0.35,0.33,0.26,0.25,0.27]
overall = [0.29,0.34,0.36,0.40,0.34]
taste = [0.64,0.66,0.79,0.87,0.85]
brand = [0.35,0.43,0.42,0.44,0.34]


np.corrcoef([health,overall,taste,brand])
print("Overall performance of the drink has to do mainly with health(it shows the hight(although negative) correlation)-.848")
plt.scatter(health,overall)
plt.scatter(health,overall)
# comment on graph
print("The least healthy it is perceived, the more popular it is.")


plt.scatter(brand,overall)
plt.scatter(taste,overall)