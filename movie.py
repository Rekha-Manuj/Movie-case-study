# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 09:05:17 2021

@author: REKHA
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
    
movies=pd.read_csv('Movie+Assignment+Data.csv')
movies.head()
movies.info() #column wise info
movies.describe() # summary of the numeric columns

movies["Gross"]=movies["Gross"]/1000000 # reduce to smaller values
movies["budget"]=movies["budget"]/1000000
movies

movies["profit"]=movies["Gross"]-movies["budget"] #Calculate the profit in a new column
movies

movies=movies.sort_values(by="profit",ascending=False) # sort the column profit
movies["profit"]

movies.iloc[:10,:] #top 10 movies which gives me high profit

sns.jointplot("budget","profit",movies) # plot the graph
plt

movies[movies["profit"]<0]

movies["MetaCritic"]=movies["MetaCritic"]/10 #MetaCritic data converted to 10 from 100
movies["Avg_rating"]=(movies["IMDb_rating"]+movies["MetaCritic"])/2 # avg of IMDB and Metacritic

df=movies[["Title","IMDb_rating","MetaCritic","Avg_rating"]]
df=df.loc[abs(df["IMDb_rating"]-df["MetaCritic"]<0.5)]

df=df.sort_values(by="Avg_rating",ascending=False)
UniversalAcclaim=df.loc[df["Avg_rating"]>=8] #Avg_rating >=8
UniversalAcclaim

# Problem Statement 1 : Three lead actors with high facebook likes
group=movies.pivot_table(values=["actor_1_facebook_likes","actor_2_facebook_likes","actor_3_facebook_likes"],aggfunc="sum",index=["actor_1_name","actor_2_name","actor_3_name"])
group


#create a new column and Find the total facebook likes of all the three actors and sort

group["Total Likes"]=group["actor_1_facebook_likes"]+group["actor_2_facebook_likes"]+group["actor_3_facebook_likes"]
group.sort_values(by="Total Likes",ascending=False,inplace=True) #inplace is uesd to sort the column and store it in the same column
group=group.head() #top five, combination of three actors
group

# Problem Statement 2 : Find the most popular trios from the three actors who has high facebook likes
# Facebook likes of one actor should not be less than the other two actors

j=0
for i in group["Total Likes"]:
   temp=sorted([group.loc[j,"actor_1_facebook_likes"],group.loc[j,"actor_2_facebook_likes"],group.loc[j,"actor_3_facebook_likes"]])
   if temp[0]>=temp[1]/2 and temp[0]>=temp[2]/2 and temp[1]>=temp[2]/2:
       print(sorted([group.loc[j,"actor_1_name"],group.loc[j,"actor_2_name"],group.loc[j,"actor_3_name"]]))
   j=j+1
    

#Runtime histogram/density plot

plt.hist(movies["Runtime"])
plt.show()


#R rated movies
(continue from 1:24:55)
