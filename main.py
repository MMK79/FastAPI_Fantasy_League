"""FastAPI Program"""

from datetime import date
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal

# Variable with a description of the API
api_description = """
This API provides read-only access to info from the SportsWorldCentral (SWC) Fantasy Football API.
The endpoints are grouped into the following categories:

## Analytics
Get information about the health of the API and counts of leagues, teams, and players.

## Player
You can get a list of NFL players, or serach for an individual player by player_id.

## Scoring
You can get a list of NFL player performances, including the fantasy points they scored using SWC league scoring.

## Membership
Get information about all the SWC fantasy football leagues and the teams in them.
"""

# FastAPI class, handle most of the jobs that API need to handle
# FastAPI constructor with additional details added for OpenAPI Specification
app = FastAPI(
    # pass the variable to application constructor
    description=api_description,
    # give the app a title
    title="Sports World Central (SWC) Fantasy Football API",
    # give the app a version, 0 means that breaking changes can still occur, 0.1 means that is the first published minor version
    version="0.1",
)
# When running API through CLI with Uvicorn, you will reference main:app, referring to the app object in main.py


# Dependency, create database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# API Health Check
@app.get("/", tags=["analytics"])
async def root():
    return {"message": "API health check successful"}


@app.get("/v0/players/", response_model=list[schemas.Player], tags=["player"])
def read_players(
    skip: int = Query(
        0, description="The number of items to skip at the beginning of API call."
    ),
    limit: int = Query(
        100, description="The number of records to return after the skipped records."
    ),
    minimum_last_changed_date: Optional[date] = Query(
        None,
        description="The minimum date of change that you want to return records. Exclude any records changed before this.",
    ),
    first_name: Optional[str] = Query(
        None, description="The first name of the palyers to return"
    ),
    last_name: Optional[str] = Query(
        None, description="The last name of the players to return"
    ),
    # wrapping get_db function in Depends let the FastAPI handles the call for and gives the Session to your function
    db: Session = Depends(get_db),
):
    # if the match between data types in get_player() from crud.py and read_players definition which is list[schemas.Player] happens
    # then the FastAPI uses Pydantic to serialize the Python objects into a text JSON string and sends the response to the consumer
    players = crud.get_players(
        db,
        skip=skip,
        limit=limit,
        min_last_changed_date=minimum_last_changed_date,
        first_name=first_name,
        last_name=last_name,
    )
    return players


@app.get(
    # endpoint
    "/v0/players/{player_id}",
    # Type of response
    response_model=schemas.Player,
    # Improve summary of endpoint
    summary="Get one player using the Plyaer ID, which is internal to SWC",
    # Detailed description to help developers and AI use it correctly
    description="If you have an SWC Player ID of a player from another API call such as v0_get_players, you can call this API using the player ID",
    # Improved description of the response. Keep this under 300 characters to make ChatGPT happy.
    response_description="One NFL player",
    # custome operation_id to replace the auto-generated one.
    operation_id="v0_get_players_by_player_id",
    # tag to group endpoints into categories
    tags=["player"],
)
def read_player(player_id: int, db: Session = Depends(get_db)):
    player = crud.get_player(db, player_id=player_id)
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@app.get(
    "/v0/performances/", response_model=list[schemas.Performance], tags=["scoring"]
)
def read_performances(
    skip: int = 0,
    limit: int = 100,
    minimum_last_changed_date: Optional[date] = None,
    db: Session = Depends(get_db),
):
    performances = crud.get_performances(
        db, skip=skip, limit=limit, min_last_changed_date=minimum_last_changed_date
    )
    return performances


@app.get("/v0/leagues/{league_id}", response_model=schemas.League, tags=["membership"])
def read_league(league_id: int, db: Session = Depends(get_db)):
    league = crud.get_league(db, league_id=league_id)
    if league is None:
        raise HTTPException(status_code=404, detail="league not found")
    return league


@app.get("/v0/leagues/", response_model=list[schemas.League], tags=["membership"])
def read_leagues(
    skip: int = 0,
    limit: int = 100,
    minimum_last_changed_date: Optional[date] = None,
    league_name: Optional[str] = None,
    db: Session = Depends(get_db),
):
    leagues = crud.get_leagues(
        db,
        skip=skip,
        limit=limit,
        min_last_changed_date=minimum_last_changed_date,
        league_name=league_name,
    )
    return leagues


@app.get("/v0/teams/", response_model=list[schemas.Team], tags=["membership"])
def read_teams(
    skip: int = 0,
    limit: int = 100,
    minimum_last_changed_date: Optional[date] = None,
    team_name: Optional[str] = None,
    league_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    teams = crud.get_teams(
        db,
        skip=skip,
        limit=limit,
        min_last_changed_date=minimum_last_changed_date,
        team_name=team_name,
        league_id=league_id,
    )
    return teams


@app.get("/v0/counts/", response_model=schemas.Counts, tags=["analytics"])
def get_count(db: Session = Depends(get_db)):
    counts = schemas.Counts(
        league_count=crud.get_league_count(db),
        team_count=crud.get_team_count(db),
        player_count=crud.get_player_count(db),
    )
    return counts
