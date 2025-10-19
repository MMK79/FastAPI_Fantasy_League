* Data App: a web application displaying your data science models, graphs, chart, and spreadsheets
	* Streamlit: Open source Python library data app which help you create colorful and interactive web apps
		* You can host this on web hosting platforms or Streamlit Community Cloud

# Engaging Users with Interactive Visualizations
* Types of analytics products:
	* Tabular reports: presents rows and columns of data in a spreadsheet format $\rightarrow$ provides a detailed view of data
	* Visualizations: charts, graphs, maps and other images that gives context and color to the data
		* Communicate ideas that are hard to see in spreadsheet
* Streamlit supports both tabular data and visualization
	* provides built-in widgets: application controls such as sliders and select boxes that allow user to filter and interact with the data in real time
	* Streamlit follow design principle of [Promoting Forward Progress](https://blog.streamlit.io/just-build-it-streamlit-opinionated-framework/#intentional-design)
	* `streamlit run your_script.py` you can generate an app using this command
* [`nflverse`](https://github.com/nflverse): rich set of open source libraries and data files containing NFL data
	* [`nfl_data_py`](https://github.com/nflverse/nfl_data_py): Python library to interact with data

# Creating Your Streamlit App
![[Streamlit-App-Architecture|center|1000]]
* Streamlit app will include an entrypoint file (`streamlit_football_app.py`)
	* entrypoint file to set initial configuration and create the page navigation
	* `st.settion_state`: mechanism to share information between pages in the application
	* `st.navigation`: make a multi-page app with a shared navigation bar
* to run Streamlit App: `streamlit run filename.py`

## Creating the Team Rosters Page
* Will call the SportsWorldCentral API $\xrightarrow{\text{then}}$ manipulate the data using pandas $\xrightarrow{\text{then}}$ display the pandas DataFrame

## Create the Team Stats Page
* Reuse data that was stored in SessionState $\xrightarrow{\text{then}}$ loads data from nfl_data_py $\xrightarrow{\text{then}}$ manipulate data (custom columns + total_tds (calculated + created) + join tables) $\xrightarrow{\text{then}}$ display chart

# Deploy Streamlit
* [Prep and deploy your app on Community Cloud - Streamlit Docs](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app)
* [Deployment tutorials - Streamlit Docs](https://docs.streamlit.io/deploy/tutorials)
# Additional Resources
* [Streamlit documentation](https://docs.streamlit.io/)[Streamlit API cheat sheet - Streamlit Docs](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)
* [Streamlit API cheat sheet - Streamlit Docs](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)
* [Streamlit for Data Science: Create interactive data apps in Python : Richards, Tyler, Treuille, Adrien: Amazon.de: Books](https://www.amazon.de/Streamlit-Data-Science-Create-interactive/dp/180324822X)
* [Get started with Streamlit - Streamlit Docs](https://docs.streamlit.io/get-started)
* [GitHub - streamlit/streamlit: Streamlit — A faster way to build and share data apps.](https://github.com/streamlit/streamlit)
* [Chart elements - Streamlit Docs](https://docs.streamlit.io/develop/api-reference/charts)
* [Streamlit • A faster way to build and share data apps](https://streamlit.io/)
* [Streamlit Crash Course: From Zero to Data App - YouTube](https://www.youtube.com/watch?v=d7fnzDQ5qM8)
* [GitHub - joeyagreco/leeger: Instant stats for any fantasy football league.](https://github.com/joeyagreco/leeger)
* [OpenDota API](https://docs.opendota.com/)
* [GitHub - nflverse/nfl\_data\_py: Python code for working with NFL play by play data.](https://github.com/nflverse/nfl_data_py)