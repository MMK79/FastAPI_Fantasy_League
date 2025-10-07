"""Pydantic Schemas"""
# Implemented Data Transfer Object which is a Software Design Pattern -> will be used to send data to the API consumer

# form the responses to the API endpoints
from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import date


class Performance(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    performance_id: int
    player_id: int
    week_number: str
    fantasy_points: float
    last_changed_date: date


# Secondary Schema for teams, extend the base schema and add relational data
class PlayerBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    player_id: int
    gsis_id: str
    first_name: str
    last_name: str
    position: str
    last_changed_date: date


# use in /v0/palyers/ endpoint and /v0/palyers/{player_id}/ endpoint
class Player(PlayerBase):
    # model_config purpose is to map databaase tables
    model_config = ConfigDict(from_attributes=True)
    # Secondary use of Performance Schema
    performances: List[Performance] = []


# Primary Schema
class TeamBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    league_id: int
    team_id: int
    team_name: str
    last_changed_date: date


class Team(TeamBase):
    model_config = ConfigDict(from_attributes=True)
    # Secondary use of PlayerBase Schema, which is a limited -> Player is the bigger one, which contain the performances too!
    players: List[PlayerBase] = []


class League(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    league_id: int
    league_name: str
    scoring_type: str
    last_changed_date: date
    # Secondary use of TeamBase Schema
    teams: List[TeamBase] = []


class Counts(BaseModel):
    # don't have model_config because it does not directly map to any database table
    league_count: int
    team_count: int
    player_count: int
