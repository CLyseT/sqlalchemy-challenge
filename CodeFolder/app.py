#Dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)
       
session = Session(engine)


#Flask Setup

app = Flask(__name__)

@app.route("/")
def welcome():
    """All Available API Routes"""
    return(f"All Available API Routes<br/><br/>"

           f"/api/v1.0/precipitation<br/>"
           f"/api/v1.0/station<br/>"
           f"/api/v1.0/tobs<br/>"
           f"/api/v1.0/start<br/>"
           f"/api/v1.0/start/end<br/>"
           )

@app.route("/api/v1.0/precipitation")
def precipitation():
     #Database Setup
     engine = create_engine("sqlite:///hawaii.sqlite")

     Base = automap_base()
     Base.prepare(engine, reflect=True)
     
     Measurement = Base.classes.measurement
     
     session = Session(engine)
     data = session.query(Measurement).all()

     all_precipitation = []
     
     for precipitation in data:
         precipitation_dict = {}
         precipitation_dict["date"] = precipitation.date
         precipitation_dict["prcp"] = precipitation.prcp
         all_precipitation.append(precipitation_dict)
     
     session.close() 

     return jsonify(all_precipitation)

@app.route("/api/v1.0/station")
def station():
     #Return a JSON list of station
     engine = create_engine("sqlite:///hawaii.sqlite")

     Base = automap_base()
     Base.prepare(engine, reflect=True)

     Measurement = Base.classes.measurement

     session = Session(engine)
     data_two = session.query(Measurement.station).all()

     all_stations = list(np.ravel(data_two))

     session.close()

     return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
     engine = create_engine("sqlite:///hawaii.sqlite")

     Base = automap_base()
     Base.prepare(engine, reflect=True)

     Measurement = Base.classes.measurement
     session = Session(engine)

     #Filter by the most active station for the last year
     year_data = session.query(Measurement.date, Measurement.tobs).\
         filter(Measurement.station == 'USC00519281').\
         filter(Measurement.date >= '2016-08-23').all()

     #Return a JSON list of temperature observation for the previous year
     temp_list = []

     for tobs in year_data:
         tobs_dict = {}
         tobs_dict["date"] = tobs.date
         tobs_dict["tobs"] = tobs.tobs
         temp_list.append(tobs_dict)
     
     session.close()
    
     return jsonify(temp_list)

@app.route("/api/v1.0/start")
def start(start):
     engine = create_engine("sqlite:///hawaii.sqlite")

     Base = automap_base()
     Base.prepare(engine, reflect=True)  

     Measurement = Base.classes.measurement
     session = Session(engine)

     #Set Start and End Dates
     start_date = session.query(func.min(Measurement.date)).first()[0]
     end_date = session.query(func.max(Measurement.date)).first()[0]
     
     #Set parameters
     if start >= start_date:
        new_temp = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start)
        
     if start <= end_date:
        new_temp = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date <= end_date).all()[0]

        return (f"Minimum Temp: {new_temp[0]}<br/>"
                        f"Average Temp: {new_temp[1]}<br/>"
                        f"Maximum Temp: {new_temp[2]}"
        )
     else:
        return jsonify (f"ERROR: The start date you entered was not found")

@app.route("/api/v1.0/start/end")
def start_end(start, end):
     engine = create_engine("sqlite:///hawaii.sqlite")

     Base = automap_base()
     Base.prepare(engine, reflect=True)   

     Measurement = Base.classes.measurement
     session = Session(engine)

     #Set Start and End Dates
     start_date = session.query(func.min(Measurement.date)).first()[0]
     end_date = session.query(func.max(Measurement.date)).first()[0]
     
     #Set parameters
     if start >= start_date:
        new_temp = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start)

     if end <= end_date:
        new_temp = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date <= end)
        
        return (f"Minimum Temp: {new_temp[0]}<br/>"
                        f"Average Temp: {new_temp[1]}<br/>"
                        f"Maximum Temp: {new_temp[2]}"
        )
     else:
        return jsonify (f"ERROR: The start date and end date you entered were not found")

if __name__ == '__main__':
    app.run(debug=True)
