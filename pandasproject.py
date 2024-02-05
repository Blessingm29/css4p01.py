#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:59:49 2024

@author: blessingmkhonazi
"""

"""
This is my pandas file for the project
"""

import pandas as pd
df = pd.read_csv("movie_dataset.csv")
print (df)


#removing the additional index column
df = pd.read_csv("movie_dataset.csv", index_col = 0)
print (df)

#replacing empty values with mean () using the fillna function
x = df["Revenue (Millions)"].mean()
df["Revenue (Millions)"].fillna(x, inplace = True)

x = df["Metascore"].mean()
df["Metascore"].fillna(x, inplace = True)
print (df)

#question1: sort the data in ascendind/descending order
pd = df.sort_values(by=['Rating'], ascending=False)
print (pd)
"""The Dark Knight"""

#question2: calculating the mean
pd = df["Revenue (Millions)"].mean()
print(pd)
"""82.95637614678898"""

#question3: calculating the mean for 2015 and 2017, filter out dates for 2015 and 2017
Revenue_2015_2017 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

pd = Revenue_2015_2017['Revenue (Millions)'].mean()
print(pd)
"""68.06402328198025"""

#question4: count how many times 2016 appears on year column
pd = df['Year'].value_counts()[2016]
print(pd)
"""297"""

#question5: count how many times Christopher Nolan appears on diector column
pd = df['Director'].value_counts()['Christopher Nolan']
print(pd)
"""5"""

#question6: filter out data
print(df[df['Rating']>=8.0])
"""78 rows"""


#question7:filter movies dierected by Nolan
films_by_nolan = df[df['Director'] == 'Christopher Nolan']
# calculate median
pd = films_by_nolan['Rating'].median()
print(pd)
"""8.6"""

#question8:  calculate average rating for each year
pd = df.groupby('Year')['Rating'].mean()

highest_year = pd.idxmax()
print(highest_year)
"""2007"""

#question9:count films released in 2006-2016
year_counts = df['Year'].value_counts()
count_2006 = year_counts.get(2006,0)
print(count_2006)

count_2016 = year_counts.get(2016,0)
print(count_2016)

#(new-old)/old*100
pd = (count_2016 - count_2006)/ count_2006 *100
print(pd)
"""575.0"""


#question11:
Genres = df[['Genre']].copy()
print(Genres)

# Split text into a list
# Then sum of unique genres...
Genres['Genre'] = Genres['Genre'].str.split(',')

# Convert list into multiple rows
Genres = Genres.explode('Genre')
print(Genres)

Genres_unique = Genres.drop_duplicates()
print(len(Genres_unique))
"""20"""

#question 10
Actors = df[['Actors']].copy()
print(Actors)

# Split text into a list
# Then sum of unique actors...
Actors['Actors'] = Actors['Actors'].str.split(',')

# Convert list into multiple rows
Actors = Actors.explode('Actors')
print(Actors)
#Actors_unique = Actors['Actors'].unique() # some 1986 unique actors hmmmmm
#print(Actors_unique)

Actors['count'] = 1 # lets get count by actor

grouped = Actors.groupby('Actors') #defined a wee function to use later

Actors_feat_count = grouped['count'].count()
print(Actors_feat_count.info()).astype(float)
# Christian Bale and Mark Wahlberg - MW is answer

#Do a correlation of the numerical features, what insights can you deduce? 
#Mention at least 5 insights.
#And what advice can you give directors to produce better movies?

# What correlation??
# Pearson, spearmann, etc.??
# Say pearson for now

"""
Numerical columns:
Year
Runtime_Minutes
Rating
Votes
Revenue_Millions
Metascore  
"""

df.head(10)
df.tail(10) # alternative to R head() and tail() functions

corr = df.corr(method = 'pearson') # don't specify cols makes it run corr for all numerical cols
print(corr) # okay so now how do I get a p value???
