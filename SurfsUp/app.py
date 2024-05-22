# Import the dependencies.
from flask import Flask, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt


#################################################
# Database Setup
#################################################

# Create engine for hawaii.sqlite
engine = create_engine('sqlite:///Resources/hawaii.sqlite')

# reflect an existing database into a new model
base = automap_base()

# reflect the tables
base.prepare(autoload_with=engine)

# Save references to each table
stat = base.classes.station
meas = base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################

# Create an app
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# Define a function that creates a home page listing all available routes
@app.route("/")
def home():
    print("Server received request for 'Home' page...")

    return """ 
    <h1>Welcome to my Honolulu Climate API Project!</h1>
    <h3>The available routes are: <br/><h3>

    <ul>
    <li> Precipitation Data: <a href = "/api/v1.0/precipitation"> /api/v1.0/precipitation </a> </li>
    <li> Station Data: <a href = '/api/v1.0/stations'> /api/v1.0/stations </a> </li>
    <li> Temperature Data: <a href = '/api/v1.0/tobs'> /api/v1.0/tobs </a> </li>
    <li> To find minimum, average, and maximum temperatures for a specific date range, use '/api/v1.0/start/end' replacing 'start' and 'end' with dates in this format 'YYYY-MM-DD'. If no 'end' date is entered, it will collect data from the start date to the last record. </li>
    </ul>

"""

# Create a function that defines a page returning precipitation data for the last 12 months
# with dates as keys and precipitation as the values
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'Precipitation' page...")

    # Find the date 12 months before the last record
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query for data of the last 12 months
    results = session.query(meas.date, meas.prcp).filter(meas.date >= query_date).all()
    
    # Create dictionary from data
    prcp_dict = {date: prcp for date, prcp in results}

    # Return the dictionary with dates as keys and prcp as values    
    return prcp_dict


# Define a function that creates a 'stations' page returning a list of the stations
@app.route('/api/v1.0/stations')
def stations():
    print("Server received request for 'Stations' page...")

    # Query for the list of stations
    stations = session.query(stat.station).all()

    # Convert list of tuples to normal list
    station_list = list(np.ravel(stations))

    # Return the jsonified list
    return jsonify(station_list)


# Create a 'tobs' page returning dates and tobs data for the last 12 months of the most active station
@app.route('/api/v1.0/tobs')
def tobs():

    # The code below was used to find the most recent record date for the most active station
    # session.query(meas.date).filter(meas.station == 'USC00519281').order_by(meas.date.desc()).first()

    # Find the date 12 months before the most recent record for the most active station
    active_last_12 = dt.date(2017, 8, 18) - dt.timedelta(days=365)

    # Query to collect date and tobs data for the previous year for the most active station
    active_records = session.query(meas.date, meas.tobs).filter((meas.station == 'USC00519281') & (meas.date >= active_last_12)).all()
    
    # Create dictionary from data
    tobs_dict = {date: tobs for date, tobs in active_records}

    # Return dictionary
    return tobs_dict


# Define a function to create a page with minimun, average, and maximum temperature from a chosen date range
@app.route("/api/v1.0/<start>/")
@app.route("/api/v1.0/<start>/<end>")
def find_temps(start = None, end = None):

    # Store min, avg, and max temperatures into variable
    sel = [func.min(meas.tobs), func.avg(meas.tobs), func.max(meas.tobs)]

    # Check if there was an end date input
    if end == None:

        # If there is no end date, query for data from given start date to last record
        start_data = session.query(*sel).\
            filter(meas.date >= start).all()
        
        # Convert list of tuples to normal list
        start_list = list(np.ravel(start_data))

        # Return jsonified list
        return jsonify(start_list)

    # If both start and end dates were given
    else:

        # Query for data from given start date to given end date
        date_range = session.query(*sel).\
            filter(meas.date >= start).\
            filter(meas.date <= end).all()
        
        # Convert list of tuples to normal list
        date_range_list = list(np.ravel(date_range))

        # Return jsonified list
        return jsonify(date_range_list)


# Close session
session.close()

# Define main branch
if __name__ == '__main__':
    app.run(debug=True)
