import streamlit as st
import swc_simple_client as swc
import pandas as pd
import logging

# reference to logging file that is created in enterypoint file
logger = logging.getLogger(__name__)

# will be printed at the type of the page
st.header("SportsWorldCentral Data App")
st.subheader("Team Rosters Page")

# retrive base_url variable from session state
base_url = st.session_state["base_url"]

# we wrapp all the page within try...except so if anything happens we log it and show the error
try:
    # call api and store the httpx.response in a variable
    team_api_response = swc.call_api_endpoint(base_url, swc.LIST_TEAMS_ENDPOINT)
    # check if the api call was successful or not, then proceed
    if team_api_response.status_code == 200:
        # convert JSON data from the API to Python representation of the data, it does not return json
        team_data = team_api_response.json()
        # convert to DataFrame
        teams_df = pd.DataFrame.from_dict(team_data)
        # get the unique values, convert them to string, then sort them
        unique_leagues = teams_df["league_id"].unique()
        unique_leagues = sorted(unique_leagues.astype(str))

        # stores the unique list of leagues in session_state object so that all pages can use them
        if "unique_leagues" not in st.session_state:
            st.session_state["unique_leagues"] = unique_leagues

        # Create a select box in navigation bar to select league_id value
        selected_league = st.sidebar.selectbox("Pick league ID", unique_leagues)
        st.sidebar.divider()
        st.sidebar.subheader(":blue[Data sources]")
        st.sidebar.text("SportsWorldCentral")

        # reformat the nested JSON data into rows and columns
        # create a new variable with a different column order
        flat_team_df = pd.json_normalize(
            team_data, "players", ["team_id", "team_name", "league_id"]
        )
        column_order = [
            "league_id",
            "team_id",
            "team_name",
            "position",
            "player_id",
            "gsis_id",
            "first_name",
            "last_name",
        ]
        flat_team_df_ordered = flat_team_df[column_order]

        if "flat_team_df_ordered" not in st.session_state:
            st.session_state["flat_team_df_ordered"] = flat_team_df_ordered

        display_df = flat_team_df_ordered.drop(columns=["team_id", "player_id"])
        display_df["league_id"] = display_df["league_id"].astype(str)
        # Create a filter DataFrame that contains only the values matching selected_league
        display_df = display_df[display_df["league_id"] == selected_league]
        # Built-in DataFrame() function to display the filtered DataFrame on the page
        st.dataframe(display_df, hide_index=True)
    else:
        # if api call is not 200 return an error
        logger.error(
            f"Error encountered: {team_api_response.status_code} {team_api_response.text}"
        )
        st.write("Error encountered while accessing data source.")

# general exeception handling block -> if anything goes wrong we will be here
except Exception as e:
    logger.error(f"Exception encountered: {str(e)}")
    st.write(f"An unexpected error occurred.")
