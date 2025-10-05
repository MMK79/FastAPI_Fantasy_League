# SportsWorldCentral (SWC) Fantasy Football API Documentation

This is a portfolio project base on "Hands-on API For Data Scientists" Book, which I developed a SportsWorldCentral API. This is a way to accessing data from fantasy footaball we Book, which I developed a SportsWorldCentral API. This is a way to accessing data from fantasy footaball website, www.sportsworldcentral.com
## Table of Contents

- [Getting Started](#getting-started)
- [Analytics](#analytics)   
- [Player](#player) 
- [Scoring](#scoring)   
- [Membership](#membership) 
- [Example Code](#example-code) 
- [Software Development Kit (SDK)](#software-development-kitsdk) 
- [API Components](#api-components)
- [Python Files and Their Functionality](#python-files-and-their-functionality)

## Getting Started
Since all of the data is public, the SWC API doesn't require any authentication.  All of the the following data is available using GET endpoints that return  JSON data. 

### Analytics
Get information about the health of the API and counts of leagues, teams,  and players. 

### Player
You can get a list of all NFL players, or search for an individual player  by player_id. 

### Scoring
You can get a list of NFL player performances, including the fantasy points they  scored using SWC league scoring. 

### Membership
Get information about all the SWC fantasy football leagues and the teams in them. 
## Example Code
Here is some Python example code for accessing the health check endpoint: 

```
import httpx
HEALTH_CHECK_ENDPOINT = "/"
with httpx.Client(base_url=self.swc_base_url) as client:
response = client.get(self.HEALTH_CHECK_ENDPOINT)
print(response.json())
``` 
## Software Development Kit (SDK)

## API Components
* Database
	* SQLite at this Stage
* Database Classes
	* SQLAlchemy
		* Python database toolkit + ORM
		* Jobs of SQLAlchemy:
			* Provide query access to database using Python, without using SQL query
			* It populates Python objects with the data from the source database without requiring any conversion of data types. 
				* Keep consistency between Python objects type and database objects
				* Support variety of databases
				* Same Python code for different database
				* Create queries as prepared statements Which Combat SQL injection
	* Handle Querying the Databases + Storing the Data
* API Controller
	* With FastAPI
	* Handle all of the API processing + other functions
* Data Transfer and Validation
	* Ensure that the API requests and responses have valid data + conform to their definitions
	* Pytest
		* Python Testing Library
		* Create Unit Test with it
			* Verify the parts of your code
		* Regression Test

	* FastAPI: Web framework to build the API
		* FastAPI CLI: Command-line interface for FastAPI
			* `main.py`: FastAPI file that defines routes and controls API
			* `test_main.py`: The pytest file for the FastAPI program
	* HTTPX: HTTP client for Python
	* Pydantic: Validation Library
		* `schemas.py`: Define the Pydantic classes that validates data sent to the API
	* #Uvicorn: Web server to run the API
    * Swagger UI: Interactive FastAPI documentation, available through `/docs` URL
    * Redoc: FastAPI documentation, available through `/redoc` URL
    * OpenAPI Specification (OAS) file: help Swagger and Redoc to generate documentation and other things, available through `/openapi.json` URL

## Python Files and Their Functionality
* `crud.py`: Helper function to query the database
	* Contains Query Functions
	* CRUD $\overset{Stands For}{=}$ Create, Write, Update, Delete
* `database.py`: Configures SQLAlchemy to use the SQLite database
	* Tasks that get perform in this file:
		* Create a database connection which points to SQLite database + has a correct setting
		* Create a parent class so You use to define the python table classes
* `models.py`: Defines the SQLAlchemy classes related to the database tables 
	* Python representation of your database data.
	* Tasks that get perform in this file:
		* Define SQLAlchemy classes to store information from database tables.
		* Describe the relationship between these tables so the Python code can access the related tables.
* `test_crud.py`: The PyTest file to unit-test your SQLAlchemy files
* `schema.py`: Pydantic classes define the structure of the data that the consumer will receive in their API responses
* `main.py`: FastAPI, tie together all the files that you have created till now!
* `test_main.py`: Unit-test the FastAPI without need to lunch it
