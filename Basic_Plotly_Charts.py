import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import webbrowser
import requests
import io

###### Example 1: Income vs age of people in a scatter plot ######
age_array=np.random.randint(25,55,60)
income_array=np.random.randint(300000,700000,60)

# First we will create an empty figure using go.Figure()
fig=go.Figure()

# Next we will create a scatter plot by using the add_trace function and use the go.scatter() function within it
# In go.Scatter we define the x-axis data, y-axis data and define the mode as markers with color of the marker as blue
fig.add_trace(go.Scatter(x=age_array, y=income_array, mode='markers', marker=dict(color='blue')))

# Here we update these values under function attributes such as title,xaxis_title and yaxis_title
fig.update_layout(title='Economic Survey', xaxis_title='Age', yaxis_title='Income')
# Display the figure
fig.write_html("plot.html")
webbrowser.open("plot.html")

###### Example 2: Sales of bicycles from Jan to August last year using a line chart ######

# Define an array containing numberofbicyclessold  
numberofbicyclessold_array=[50,100,40,150,160,70,60,45]
# Define an array containing months
months_array=["Jan","Feb","Mar","April","May","June","July","August"]

##First we will create an empty figure using go.Figure()
fig=go.Figure()

# Next we will create a line plot by using the add_trace function and use the go.scatter() function within it
# In go.Scatter we define the x-axis data,y-axis data and define the mode as lines with color of the marker as green
fig.add_trace(go.Scatter(x=months_array, y=numberofbicyclessold_array, mode='lines', marker=dict(color='green')))

# Here we update these values under function attributes such as title,xaxis_title and yaxis_title
fig.update_layout(title='Bicycle Sales', xaxis_title='Months', yaxis_title='Number of Bicycles Sold')
# Display the figure
fig.write_html("plot.html")
webbrowser.open("plot.html")

###### Example 3: Average pass percentage of classes from grade 6 to grade 10 ######

# Define an array containing scores of students 
score_array=[80,90,56,88,95]
# Define an array containing Grade names  
grade_array=['Grade 6','Grade 7','Grade 8','Grade 9','Grade 10']

# Use plotly express bar chart function px.bar.Provide input data, x and y axis variable, and title of the chart.
# This will give average pass percentage per class
fig = px.bar( x=grade_array, y=score_array, title='Pass Percentage of Classes') 
fig.write_html("plot.html")
webbrowser.open("plot.html")

###### Example 4: Distribution of heights of 200 people using a histogram ######

#Here we will concentrate on heights which are 160 and the standard deviation is 11
heights_array = np.random.normal(160, 11, 200)
## Use plotly express histogram chart function px.histogram.Provide input data x to the histogram
fig = px.histogram(x=heights_array,title="Distribution of Heights")
fig.write_html("plot.html")
webbrowser.open("plot.html")

###### Example 5: Crime statistics of US cities with a bubble chart ######

#Create a dictionary having city,numberofcrimes and year as 3 keys
crime_details = {
    'City' : ['Chicago', 'Chicago', 'Austin', 'Austin','Seattle','Seattle'],
    'Numberofcrimes' : [1000, 1200, 400, 700,350,1500],
    'Year' : ['2007', '2008', '2007', '2008','2007','2008'],
}
  
# Create a Dataframe object with the dictionary
df = pd.DataFrame(crime_details)
  
# Group the number of crimes by city and find the total number of crimes per city
bub_data = df.groupby('City')['Numberofcrimes'].sum().reset_index()

## Bubble chart using px.scatter function with x ,y and size varibles defined.Title defined as Crime Statistics
fig = px.scatter(bub_data, x="City", y="Numberofcrimes", size="Numberofcrimes",
                 hover_name="City", title='Crime Statistics', size_max=60)
fig.write_html("plot.html")
webbrowser.open("plot.html")

###### Example 6: Monthly expenditure of a family ######

# Random Data
exp_percent= [20, 50, 10,8,12]
house_holdcategories = ['Grocery', 'Rent', 'School Fees','Transport','Savings']

# Use px.pie function to create the chart. Input dataset. 
# Values parameter will set values associated to the sector. 'exp_percent' feature is passed to it.
# labels for the sector are passed to the `house hold categoris` parameter.
fig = px.pie(values=exp_percent, names=house_holdcategories, title='Household Expenditure')
fig.write_html("plot.html")
webbrowser.open("plot.html")

### Example 7: Sunburst Chart ######

# Create a dictionary having a set of people represented by a character array and the parents of these
# characters represented in another array and the values are the values associated to the vectors.
data = dict(
    character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

fig = px.sunburst(
    data,
    names='character',
    parents='parent',
    values='value',
    title="Family chart"
)
fig.write_html("plot.html")
webbrowser.open("plot.html")

###### Practice Exercises: Apply your Plotly Skills to an Airline Dataset ######

# URL of the CSV file
URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv'

# Send GET request to the URL
response = requests.get(URL)

# Raise error if the request failed
response.raise_for_status()

# Read the CSV data into a pandas DataFrame
airline_data = pd.read_csv(io.BytesIO(response.content),
                           encoding="ISO-8859-1",
                           dtype={
                               'Div1Airport': str,
                               'Div1TailNum': str,
                               'Div2Airport': str,
                               'Div2TailNum': str
                           })

# Preview the first 5 lines of the loaded data 
print(airline_data.head())

# Shape of the data
print(airline_data.shape)

# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data = airline_data.sample(n=500, random_state=42)
print(data.shape)

# Scatter plot to represent departure time changes with respect to airport distance
# Title as Distance vs Departure Time.
# x-axis label should be Distance
# y-axis label should be DepTime
# Distance column data from the flight delay dataset should be considered in x-axis
# DepTime column data from the flight delay dataset should be considered in y-axis
# Scatter plot markers should be of red color
fig=go.Figure()
fig.add_trace(go.Scatter(x=data.Distance, y=data.DepTime, mode='markers', marker=dict(color='red')))
fig.update_layout(title='Distance vs Departure Time', xaxis_title='Distance', yaxis_title='DeptTime')
fig.write_html("plot.html")
webbrowser.open("plot.html")

# Line plot to extract average monthly arrival delay time and see how it changes over the year.
# Title as Month vs Average Flight Delay Time.
# x-axis label should be Month
# y-axis label should be ArrDelay
# A new dataframe line_data should be created which consists of 2 columns average arrival delay time per month and month from the dataset
# Month column data from the line_data dataframe should be considered in x-axis
# ArrDelay column data from the line_data dataframeshould be considered in y-axis
# Plotted line in the line plot should be of green color
line_data = data.groupby('Month')['ArrDelay'].mean().reset_index()
fig=go.Figure()
fig.add_trace(go.Scatter(x=line_data.Month, y=line_data.ArrDelay, mode='lines', marker=dict(color='green')))
fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')
fig.write_html("plot.html")
webbrowser.open("plot.html")

# Bar chart to extract number of flights that goes to a destination
# Title as Total number of flights to the destination state
# x-axis label should be DestState
# y-axis label should be Flights
# Create a new dataframe called bar_data which contains 2 columns DestState and Flights.
# Here flights indicate total number of flights in each combination.
bar_data = data.groupby('DestState')['Flights'].sum().reset_index()
fig = px.bar(x=bar_data.DestState, y=bar_data.Flights, title='Total number of flights to the destination state split')
fig.update_layout(xaxis_title='DestState', yaxis_title='Flights') 
fig.write_html("plot.html")
webbrowser.open("plot.html")

# Distribution of arrival delay using a histogram
# Title as Distribution of Arrival Delay
# x-axis label should be ArrDelay
# y-axis will show the count of arrival delay
fig = px.histogram(x=data.ArrDelay,title="Distribution of Arrival Delay")
fig.update_layout(xaxis_title='ArrDelay', yaxis_title='Flights') 
fig.write_html("plot.html")
webbrowser.open("plot.html")

# Bubble plot to represent number of flights as per reporting airline
# Title as Reporting Airline vs Number of Flights.
# x-axis label should be Reporting_Airline
# y-axis label should be Flights
# size of the bubble should be Flights indicating number of flights
# Name of the hover tooltip to reporting_airline using hover_name parameter.
bub_data = data.groupby('Reporting_Airline')['Flights'].sum().reset_index()
fig = px.scatter(bub_data, x="Reporting_Airline", y="Flights", size="Flights",
                 hover_name="Reporting_Airline", title='Reporting Airline vs Number of Flights', size_max=60)
fig.write_html("plot.html")
webbrowser.open("plot.html")

# Pie Chart with the proportion of Flights by Distance Group (Flights indicated by numbers)
# Title as Flight propotion by Distance Group
# Values should be Flights
# Names should be DistanceGroup
pie_data = data.groupby('DistanceGroup')['Flights'].sum().reset_index()
fig = px.pie(values=pie_data.Flights, names=pie_data.DistanceGroup, title='Flight propotion by Distance Group')
fig.write_html("plot.html")
webbrowser.open("plot.html")

# SunBurst Chart with the hierarchical view in the order of month and destination state holding value of number of flights
# Define hierarchy of sectors from root to leaves in path parameter. Here, we go from Month to DestStateName feature.
# Set sector values in values parameter. Here, we can pass in Flights feature.
# Title as Flight Distribution Hierarchy

fig = px.sunburst(data, path = ['Month', 'DestStateName'],
    values='Flights', title="Flight Distribution Hierarchy")
fig.write_html("plot.html")
webbrowser.open("plot.html")






