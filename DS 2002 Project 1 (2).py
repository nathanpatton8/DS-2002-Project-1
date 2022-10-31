#!/usr/bin/env python
# coding: utf-8

# # Project 1 

# ## Instructions

# The Goal of this project is to demonstrate (1) an understanding of and (2) competence of
# implementing and using basic data science systems rooted in SQL and other data sources like
# flat files (CSV), Open Data and other relational and data sources as well as APIs and data
# transformation. 
# 
# For this project you will use GitHub to store and manage your code.
# This will be due on Oct 31st at 11:59 PM. Submit it to Git, copy the invite /link to me.
# 
# ETL data processor
# 1. Deliverable: Author a segment of an ETL pipeline that will ingest or process raw data.
# You must also submit a URL to a GitHub repository for your solution. In python you’ll
# need to know how to open files, iterate files, pattern match and output files.
# 2. Benchmarks:
# i. Your data processor should be able to ingest a pre-defined data source and
# perform at least three of these operations:
#     1. Fetch / download / retrieve a remote data file by URL (API call like we did
#     in class), or ingest a local file that you have downloaded from
#     somewhere…like in a CSV format. Suggestions for remote data sources
#     are listed at the end of this document on our Github page as we went
#     through in class.
#     2. Convert the general format and data structure of the data source (from
#     JSON to CSV, from CSV to JSON, from JSON into a SQL database table,
#     etc. I want the option to convert any source to any target. So, if I get a
#     CSV as an input, I want the user to choose an output)
#     3. Modify the number of columns from the source to the destination,
#     reducing or adding columns so that you transform it with something
#     else…you can make up whatever it is…like date changes…or mash up
#     two columns…it’s up to you.
#     4. The converted (new) file should be written to disk (local file) or written to a
#     SQL database like SQL Lite
#     5. Generate a brief summary of the data file ingestion after it has processed
#     and output it to the user including:
#         1. Number of records
#         2. Number of columns
# ii. The processor should produce informative errors should it be unable to complete
# an operation. (Try / Catch with error messages, not file exists…just pick any
# error.)
# 
# 3. Grading:
# i.Successful build of the solution that I can run and replicate your results 10
# ii.Functionality that meets all benchmarks – 10 points
# iii.Creativity / Innovation / Quality – 2 points 
# iv. Documentation – Describes how to use the data processor and the elements
# that make it operational – 3 points 
# 
# Publicly-available datasets:
# •	https://www.kaggle.com/datasets
# •	https://data.world/
# •	https://www.data.gov/
# •	https://opendata.charlottesville.org/
# You can Choose/find data from anywhere you like…these are just suggestions.
# Publicly-available APIs:
# • https://docs.github.com/en/rest
# • https://developer.twitter.com/en/docs/twitter-api
# • HUGE LIST: https://github.com/public-apis/public-apis 

# ## Code

# In[142]:


# import statements (Directions: Click the "Run" button at the top of the program for the needed import statements)
import json
import csv
import requests
import pandas as pd


# In[143]:


# Taking user input for the zipcode (Directions: 1) Click "Run" 2) Enter a 5-digit integer zipcode 3) Click the enter key
zipcode = input()


# In[144]:


# Displaying the zipcode Ticker (Directions: Click "Run" to make sure the zipcode is the one you entered)
zipcode


# In[146]:


# Creating a header (Directions: Click "Run" so that the header can be built)
header_var = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


# In[147]:


# Fetching remote data file by url from api (Directions: 1) Click "Run" to pull a url from the Ticket Master API and create a JSON data variable
url = 'https://app.ticketmaster.com/discovery/v2/events.json?apikey=hFlpdwoseKzCByGogzG3JfCoNGcMYlc5'
query_str = {"postalCode": zipcode}
response = requests.request("GET", url, headers = header_var, params = query_str)
data = response.json()
data


# In[148]:


# Displaying the events occuring at the inputed zipcode (Directions: Click "Run" to build the "events" variable which contains all the events on Ticket Master occuring at that zipcode)
events = data['_embedded']['events']
events


# In[149]:


# Narrowing down the events by name with informative error message if operation is not possible (Directions: Click "Run" to get all the names of the events occuring at your inputed zipcode)
event_names = []
for i in range(0, len(events)):
    try:
        event_names.append(events[i]['name'])
    except IndexError:
        raise IndexError("ID is not properly defined for this zipcode. Please input a new zipcode and try again.")
event_names


# In[150]:


# Narrowing down events by date with informative error message if operation is not possible (Directions: Click "Run" to get all the dates of the events occuring at your inputed zipcode)
event_date = []
for i in range(0, len(events)):
    try:
        event_date.append(events[i]['dates']['start']['localDate'])
    except IndexError:
        raise IndexError("ID is not properly defined for this zipcode. Please input a new zipcode and try again.")
event_date


# In[151]:


# Narrowing down events by id with informative error message if operation is not possible (Directions: Click "Run" to get all the ID's of the events occuring at your inputed zipcode)
event_id = []
for i in range(0, len(events)):
    try:
        event_id.append(events[i]['id'])
    except IndexError:
        raise IndexError("ID is not properly defined for this zipcode. Please input a new zipcode and try again.")
event_id


# In[152]:


# Creating the dictionary with just event name, id, and date (Directions: Click "Run" to build a dictionary containing the desired event information)
dictionary = {"Name": event_names,
              "ID": event_id,
              "Date": event_date}
dictionary


# In[153]:


# Converting dictionary to a proper JSON string (Directions: Click "Run" to convert the previosuly made dictionary to a proper JSON string that can later be read into a Dataframe)
json_data = json.dumps(dictionary)
json_data


# In[154]:


# Loading the JSON into a Dataframe (Directions: Click "Run" to read the proper JSON string into a DataFrame)
df = pd.read_json(json_data)
df


# In[155]:


# Converting df to a CSV and writing it to a local file (Directions: Click "Run" to convert the DataFrame to a CSV and save that as a local file called "out.csv")
df.to_csv('out.csv', index=False)  

