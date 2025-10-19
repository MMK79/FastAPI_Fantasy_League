import os
from typing import Optional, Type, List
from pydantic import BaseModel, Field
from langchain_core.callbacks import CallbackManagerForToolRun

# LangChain libraries for defining tools and toolkit
from langchain_core.tools import BaseTool, BaseToolkit

# if the swcpy SDK has been installed in the environment or not
try:
    from swcpy import SWCClient
    from swcpy import SWCConfig
    from swcpy.swc_client import League, Team

except ImportError:
    raise ImportError("swcpy is not installed. Please intall it")

# Instantiates the SDK
config = SWCConfig(backoff=False)
local_swc_client = SWCClient(config)


# For each of the SDK function -> create an instance of Pydantic BasesModel class for input values + instance of the LangChain BaseTool class to call the SDK
# This tool accept no parameter, so we create an empty object
class HealthCheckInput(BaseModel):
    pass


# Information will be used by model to decide when to use this tool
class HealthCheckTool(BaseTool):
    name: str = "HealthCheck"
    description: str = (
        "useful to check if the API is running before you make other calls"
    )
    # args_schema define what inputs are expected -> model use this to send input to the tool
    args_schema: Type[HealthCheckInput] = HealthCheckInput
    return_direct: bool = False

    def _run(self, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Use the tool to check if the API is running."""
        health_check_response = local_swc_client.get_health_check()
        return health_check_response.text


# Contain details that will get use by the model
class LeaguesInput(BaseModel):
    league_name: Optional[str] = Field(
        default=None, description="league name. Leave blank or None to get all leagues."
    )


# This tool call the list_leauge() function from the sdk
class ListLeaguesTool(BaseTool):
    name: str = "ListLeagues"
    description: str = (
        "get a list of leagues from SportsWorldCentral."
        "Leagues contain teams if they are present."
    )
    args_schema: Type[LeaguesInput] = LeaguesInput
    return_direct: bool = False

    def _run(
        self,
        league_name: Optional[str] = None,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> List[League]:
        """Use the tool to get a list of leagues from SportsWorldCentral."""
        # Call the API with league_name, which could be None
        list_leagues_response = local_swc_client.list_leagues(league_name=league_name)
        return list_leagues_response


# BaseToolKit object = representation of all the tools that will be provide to an agent


class TeamsInput(BaseModel):
    team_name: Optional[str] = Field(
        default=None,
        description="Name of the team to serach for. Leave blank or None to get all teams.",
    )
    league_id: Optional[int] = Field(
        default=None,
        description=(
            "League ID from a league. You must provide a numerical League ID."
            "Filter teams from a specific league."
        ),
    )


class ListTeamsTool(BaseTool):
    name: str = "ListTeams"
    description: str = (
        "Get a list of teams from SportsWorldCentral. Teams contain players."
        "if they are present. Optionally proivde a numerical League ID to filter teams from a specific league."
    )
    args_schema: Type[TeamsInput] = TeamsInput
    return_direct: bool = False

    def _run(
        self,
        team_name: Optional[str] = None,
        league_id: Optional[int] = None,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> List[Team]:
        """Use the tool to get a list of teams from SportsWorldCentral."""
        list_teams_response = local_swc_client.list_teams(
            team_name=team_name, league_id=league_id
        )
        return list_teams_response


class SportsWorldCentralToolkit(BaseToolkit):
    # return list of the tools in toolkit
    def get_tools(self) -> List[BaseTool]:
        """Return the list of tools in the toolkit."""
        # instantiates the tools and returns them in a list
        return [HealthCheckTool(), ListLeaguesTool(), ListTeamsTool()]
