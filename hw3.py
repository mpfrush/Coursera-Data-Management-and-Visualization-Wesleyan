# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 2015

@author: violetgirl
"""
import pandas as pd

# load gapminder dataset
data = pd.read_csv('gapminder.csv',low_memory=False)
# lower-case all DataFrame column names
data.columns = map(str.lower, data.columns)
# bug fix for display formats to avoid run time errors
pd.set_option('display.float_format', lambda x:'%f'%x)

# setting variables to be numeric
data['suicideper100th'] = data['suicideper100th'].convert_objects(convert_numeric=True)
data['breastcancerper100th'] = data['breastcancerper100th'].convert_objects(convert_numeric=True)
data['hivrate'] = data['hivrate'].convert_objects(convert_numeric=True)
data['employrate'] = data['employrate'].convert_objects(convert_numeric=True)

# display summary statistics about the data
print("Statistics for a Suicide Rate")
print(data['suicideper100th'].describe())

# subset data for a high suicide rate based on summary statistics
sub = data[(data['suicideper100th']>12)]
#make a copy of my new subsetted data
sub_copy = sub.copy()


# BREAST CANCER RATE
# frequency and percentage distritions for a number of breast cancer cases with a high suicide rate
# include the count of missing data and group the variables in 4 groups by number of 
# breast cancer cases (1-23, 24-46, 47-69, 70-92)
bc_max=sub_copy['breastcancerper100th'].max() # maximum of breast cancer cases
# group the data in 4 groups by number of breast cancer cases and record it into new variable bcgroup4
sub_copy['bcgroup4']=pd.cut(sub_copy.breastcancerper100th,[0*bc_max,0.25*bc_max,0.5*bc_max,0.75*bc_max,1*bc_max])
# frequency for 4 groups of breast cancer cases with a high suicide rate
bc=sub_copy['bcgroup4'].value_counts(sort=False,dropna=False)
# percentage for 4 groups of breast cancer cases with a high suicide rate
pbc=sub_copy['bcgroup4'].value_counts(sort=False,dropna=False,normalize=True)*100

# cumulative frequency and cumulative percentage for 4 groups of breast cancer cases with a high suicide rate
bc1=[] # Cumulative Frequency
pbc1=[] # Cumulative Percentage
cf=0
cp=0
for freq in bc:
    cf=cf+freq
    bc1.append(cf)    
    pf=cf*100/len(sub_copy)
    pbc1.append(pf)

print('Number of Breast Cancer Cases with a High Suicide Rate')
fmt1 = '%10s %9s %9s %12s %13s'
fmt2 = '%9s %9.d %10.2f %9.d %13.2f'
print(fmt1 % ('# of Cases','Freq.','Percent','Cum. Freq.','Cum. Percent'))
for i, (key, var1, var2, var3, var4) in enumerate(zip(bc.keys(),bc,pbc,bc1,pbc1)):
    print(fmt2 % (key, var1, var2, var3, var4))


# HIV RATE
# frequency and percentage distritions for HIV rate with a high suicide rate
# include the count of missing data and group the variables in 4 groups by quartile function
# group the data in 4 groups and record it into new variable hcgroup4
sub_copy['hcgroup4']=pd.qcut(sub_copy.hivrate,4,labels=["0% tile","25% tile","50% tile","75% tile"])
# frequency for 4 groups of HIV rate with a high suicide rate
hc = sub_copy['hcgroup4'].value_counts(sort=False,dropna=False)
# percentage for 4 groups of HIV rate with a high suicide rate
phc = sub_copy['hcgroup4'].value_counts(sort=False,dropna=False,normalize=True)*100

# cumulative frequency and cumulative percentage for 4 groups of HIV rate with a high suicide rate
hc1=[] # Cumulative Frequency
phc1=[] # Cumulative Percentage
cf=0
cp=0
for freq in hc:
    cf=cf+freq
    hc1.append(cf)    
    pf=cf*100/len(sub_copy)
    phc1.append(pf)

print('HIV Rate with a High Suicide Rate')
print(fmt1 % ('Rate','Freq.','Percent','Cum. Freq.','Cum. Percent'))
for i, (key, var1, var2, var3, var4) in enumerate(zip(hc.keys(),hc,phc,hc1,phc1)):
    print(fmt2 % (key, var1, var2, var3, var4))

# EMPLOYMENT RATE
# frequency and percentage distritions for employment rate with a high suicide rate
# include the count of missing data and group the variables in 5 groups by 
# group the data in 5 groups and record it into new variable ecgroup4
def ecgroup4 (row):
    if row['employrate'] >= 32 and row['employrate'] < 51:
        return 1
    elif row['employrate'] >= 51 and row['employrate'] < 59:
        return 2
    elif row['employrate'] >= 59 and row['employrate'] < 65:
        return 3
    elif row['employrate'] >= 65 and row['employrate'] < 84:
        return 4
    else:
        return 5 # record for NAN values

sub_copy['ecgroup4'] = sub_copy.apply(lambda row:  ecgroup4 (row), axis=1)        

# frequency for 5 groups of employment rate with a high suicide rate
ec = sub_copy['ecgroup4'].value_counts(sort=False,dropna=False)
# percentage for 5 groups of employment rate with a high suicide rate
pec = sub_copy['ecgroup4'].value_counts(sort=False,dropna=False,normalize=True)*100

# cumulative frequency and cumulative percentage for 5 groups of employment rate with a high suicide rate
ec1=[] # Cumulative Frequency
pec1=[] # Cumulative Percentage
cf=0
cp=0
for freq in ec:
    cf=cf+freq
    ec1.append(cf)    
    pf=cf*100/len(sub_copy)
    pec1.append(pf)

print('Employment Rate with a High Suicide Rate')
print(fmt1 % ('Rate','Freq.','Percent','Cum. Freq.','Cum. Percent'))
for i, (key, var1, var2, var3, var4) in enumerate(zip(ec.keys(),ec,pec,ec1,pec1)):
    print(fmt2 % (key, var1, var2, var3, var4)) 

# END