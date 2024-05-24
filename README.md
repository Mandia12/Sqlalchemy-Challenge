# Sqlalchemy-Challenge

Description:

This project contains two main files name "Climate.ipynb" and "App.py". In both, Sqlalchemy was used to connect python to a sqlite file. Target queries were created and the data located was used to create plots or to input into routes in a flask app. 


Climate:

This file contains two different analyses. One is a precipiation analysis and the other is an analysis on stations. Using sqlalchemy to link python to a database, queries were created to find valuable information within the hawaii.sqlite file. From these queries, a bar graph created from pandas dataframes and matplotlib that shows the precipitaion data, specifically from last 12 months. To create the station analysis, the last 12 months of temperature observation data for the most station active station was queried, then organized as a pandas dataframe and lastly, a histogram was created from it.

App:

This file contains code that creates a flask app, with static and dynamic routes. The app consists of home, precipitation, stations, and tobs(temperature observation) pages. Each page contains results from queries created to extract specific data from the same hawaii.sqlite file. The dynamic routes allow for inputs in "YYYY-MM-DD" format for start and/or end dates, which results in all tobs data from the given start date to either the end of the records or the given end date.

