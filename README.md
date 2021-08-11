# sqlalchemy-challenge

Final codes can be found in the CodeFolder.

The following will provide the cell numbers for each requests.

# Climate Analysis and Exploration
- Use SQLAlchemy create_engine to connect to your sqlite database: Cell 431
- Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement: Cell 432
- Link Python to the database by creating an SQLAlchemy session: Cells 433 - 439

# Precipitation Analysis
- Start by finding the most recent date in the data set: Cell 441
- Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. Note you do not pass in the date as a variable to your query: Cell 442
- Select only the date and prcp values: Cell 443
- Load the query results into a Pandas DataFrame and set the index to the date column: Cell 444
- Sort the DataFrame values by date: Cell 447
- Plot the results using the DataFrame plot method: Cell 448
- Use Pandas to print the summary statistics for the precipitation data: Cell 449

# Station Analysis
- Design a query to calculate the total number of stations in the dataset: Cell 450
- Design a query to find the most active stations (i.e. which stations have the most rows?): Cell 452 
- List the stations and observation counts in descending order: Cell 462
- Which station id has the highest number of observations? Station 7, USC00519281, is the most active station
- Using the most active station id, calculate the lowest, highest, and average temperature: Cell 463
- Design a query to retrieve the last 12 months of temperature observation data (TOBS): Cell 464
- Filter by the station with the highest number of observations: Cell 464
- Query the last 12 months of temperature observation data for this station: Cell 464
- Plot the results as a histogram with bins=12: Cell 466

# Climate App
- corrsponding codes can be found in app.py file
