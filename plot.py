# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:04:46 2019

@author: iamhe
"""
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

freeFormResponses = pd.read_csv('freeFormResponses.csv')
multipleChoice = pd.read_csv('multipleChoiceResponses.csv')
data = multipleChoice[1:]

data.head(3)
print(len(data)) #23859行
print(data.columns.values.tolist()) #50个问题
print(len(data.columns.values.tolist())) #395列

#问卷回答时间
responsesOnlyDuration = data['Time from Start to Finish (seconds)'].apply(lambda x: int(x)/60)
plt.figure(figsize=(15,10))
sns.distplot(responsesOnlyDuration,bins=5000,color='g').set(xlim=(0, 60))
plt.show()

#性别分布
sex = data['Q1'].value_counts()
colors = ['lightcoral','lightskyblue','gold','lightgreen']
explode = [0,0,0,0]
plt.figure(figsize=(10,10))
plt.pie(sex.values,explode=explode,labels=sex.index,autopct='%1.1f%%',colors=colors,shadow=True,startangle=50)
plt.show()

#年龄
age = data['Q2']
plt.figure(figsize=(15,10))
sns.countplot(y=age,palette="Set3")
plt.show()

#国家
country = data['Q3']
country = country.value_counts()
plt.figure(figsize=(15,15))
sns.barplot(x=country.values,y=country.index,palette="Set3")
plt.show()

from pyecharts import Map
map = Map("In which country do you currently reside?", width=1200, height=600)
map.add(
    "",
    country.index,
    country.values,
    maptype="world",
    is_visualmap=True,
    visual_range = [0,5000],
    visual_text_color="#000",
)
map.render("country.html")

#学历
degree = data['Q4']
plt.figure(figsize=(15,10))
sns.countplot(degree,palette="Set2")
plt.show()


#专业
major = data['Q5']
major = major.value_counts()
plt.figure(figsize=(12,10))
sns.barplot(x=major.values,y=major.index,palette="Set3")
plt.show()

#学历与专业
plt.figure(figsize=(15,8))
sns.countplot(y=data.Q5,hue=data.Q4,palette="Set3")
plt.show()

#职业
role = data['Q6']
role = role.value_counts()
plt.figure(figsize=(15,10))
sns.barplot(x=role.values,y=role.index,palette="Set3")
plt.show()

#工作领域
industry = data['Q7']
industry = industry.value_counts()
plt.figure(figsize=(15,10))
sns.barplot(x=industry.values,y=industry.index,palette="Set3")
plt.show()

#当前职业的工作时间,用0填充缺失值
time = data['Q8'].fillna(value='null').value_counts()
index = ['null','0-1','1-2','2-3','3-4','4-5','5-10','10-15','15-20','20-25','25-30','30+']    
plt.figure(figsize=(10,10))
sns.pointplot(time.index,time.values,order=index,color='k')
plt.show()  

#年薪，单位美元
compensation = data['Q9']
compensation = compensation.value_counts()
plt.figure(figsize=(15,10))
sns.barplot(x=compensation.values,y=compensation.index,palette="Set3")
plt.show()

#雇主是否将机器学习纳入业务范围
mlb = data['Q10']
mlb = mlb.value_counts()
plt.figure(figsize=(10,5))
sns.barplot(x=mlb.values,y=mlb.index,palette="Set3")
plt.show()

#工作中的主要活动
s = []
for i in range(1,8):
    s.append("Q11_Part_{}".format(i))
activities = data[s]
a = []
for i in range(len(activities)):
    for j in s:
        a.append(activities[j].iloc[i])

plt.figure(figsize=(10,5))
sns.countplot(y = a,palette="Set3")
plt.show()

#过去5年，最常用的IDE
s = []
for i in range(1,16):
    s.append("Q13_Part_{}".format(i))
Q13 = data[s]
ide = []
for i in range(len(Q13)):
    for j in s:
        ide.append(Q13[j].iloc[i])

plt.figure(figsize=(10,5))
sns.countplot(y = ide,palette="Set3")
plt.show()

#过去五年，最常使用的托管平台
s = []
for i in range(1,12):
    s.append("Q14_Part_{}".format(i))
Q14 = data[s]
hosted = []
for i in range(len(Q14)):
    for j in s:
        hosted.append(Q14[j].iloc[i])

plt.figure(figsize=(10,5))
sns.countplot(y = hosted,palette="Set3")
plt.show()

#过去5年，最常使用的云计算服务
s = []
for i in range(1,8):
    s.append("Q15_Part_{}".format(i))
Q15 = data[s]
cloud = []
for i in range(len(Q15)):
    for j in s:
        cloud.append(Q15[j].iloc[i])

plt.figure(figsize=(15,5))
sns.countplot(x = cloud,palette="Set3")
plt.show()

#最常使用的编程语言
s = []
for i in range(1,19):
    s.append("Q16_Part_{}".format(i))
Q16 = data[s]
lang = []
for i in range(len(Q16)):
    for j in s:
        lang.append(Q16[j].iloc[i])

plt.figure(figsize=(10,5))
sns.countplot(y = lang,palette="Set3")
plt.show()

#推荐数据科学家最该学习的一种编程语言
recommend = data['Q18'].value_counts()
plt.figure(figsize=(10,10))
sns.pointplot(recommend.index,recommend.values,linestyles=["-"],color='g')
plt.show()

#过去五年，最常使用的机器学习框架
s = []
for i in range(1,20):
    s.append("Q19_Part_{}".format(i))
Q19 = data[s]
frameworks = []
for i in range(len(Q19)):
    for j in s:
        frameworks.append(Q19[j].iloc[i])

plt.figure(figsize=(10,5))
sns.countplot(y = frameworks,palette="Set3")
plt.show()

#最常使用的机器学习一个库
package = data['Q20'].value_counts()
plt.figure(figsize=(18,10))
sns.pointplot(package.index,package.values,color='pink')
plt.show()

explode = []
for i in range(18):
    explode.append(0)
plt.figure(figsize=(10,10))
plt.pie(package.values,explode=explode,labels=package.index,autopct='%1.1f%%',shadow=True,startangle=50)
plt.show()

#过去5年，最常使用的数据可视化工具
s = []
for i in range(1,14):
    s.append("Q21_Part_{}".format(i))
Q21 = data[s]
visualization  = []
for i in range(len(Q21)):
    for j in s:
        visualization.append(Q21[j].iloc[i])
plt.figure(figsize=(10,5))
sns.countplot(y = visualization,palette="Set3")
plt.show()

#最常使用的数据可视化一个库
visualization = data['Q22'].value_counts()
plt.figure(figsize=(10,10))
sns.pointplot(visualization.index,visualization.values,color='r')
plt.show()
