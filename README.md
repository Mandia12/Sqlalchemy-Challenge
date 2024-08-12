# SqlAlchemy Climate Analysis and Flask API

## Overview

This project involves analyzing climate data from a SQLite database and creating a Flask web application to display the results. The analysis focuses on precipitation patterns and temperature observations from various weather stations in Hawaii. The project is divided into two main components:

1. **Climate Analysis**: Conducted in a Jupyter Notebook to explore precipitation and station data.
2. **Flask API**: A web application that serves the results of the analysis through various routes.

## Features

### Climate Analysis

- **Precipitation Analysis**:
  - Utilizes SQLAlchemy to connect Python to the `hawaii.sqlite` database.
  - Queries precipitation data for the last 12 months.
  - Visualizes the results using Pandas DataFrames and Matplotlib, with a bar graph representing precipitation over time.

- **Station Analysis**:
  - Retrieves temperature observation data for the most active station over the last 12 months.
  - Organizes the data into a Pandas DataFrame.
  - Creates a histogram to display the distribution of temperature observations.

### Flask Web Application

- **Home Page**:
  - Provides an overview of available routes.

- **Precipitation Route**:
  - Displays a JSON representation of the queried precipitation data.

- **Stations Route**:
  - Lists all weather stations and their information.

- **Temperature Observations (tobs) Route**:
  - Presents temperature observations for the most active station over the last 12 months.

- **Dynamic Routes**:
  - Allows users to input start and/or end dates in the "YYYY-MM-DD" format to retrieve temperature observations for the specified period.

## Tools and Technologies

- **Python**: For data analysis and backend development.
- **SQLAlchemy**: For database connection and querying.
- **SQLite**: For storing and managing climate data.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For data visualization.
- **Flask**: For creating the web application.

## How to Use

1. **Clone the repository** to your local machine.
2. **Navigate to the project directory** and open `Climate.ipynb` to explore the climate data analysis.
3. **Run the Flask app** by executing `App.py`:
   - Access the home page at `http://127.0.0.1:5000/`.
   - Explore the different routes to view precipitation data, station information, and temperature observations.
   - Use dynamic routes to filter data by specific dates.


This file contains code that creates a flask app, with static and dynamic routes. The app consists of home, precipitation, stations, and tobs(temperature observation) pages. Each page contains results from queries created to extract specific data from the same hawaii.sqlite file. The dynamic routes allow for inputs in "YYYY-MM-DD" format for start and/or end dates, which results in all tobs data from the given start date to either the end of the records or the given end date.

