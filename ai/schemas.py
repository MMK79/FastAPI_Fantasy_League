"""Pydantic Schemas"""

# BaseModel object that contains the validation logic
from pydantic import BaseModel


# Defines input values
class FantasyAcquisitionFeatures(BaseModel):
    waiver_value_tier: int
    fantasy_regular_season_weeks_remaining: int
    league_budget_pct_remaining: int


# Defines output values
class PredictionOutput(BaseModel):
    winning_bid_10th_percentile: float
    winning_bid_50th_percentile: float
    winning_bid_90th_percentile: float
