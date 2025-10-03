# API Components
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


# Python Files and Their Functionality
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
