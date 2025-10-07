import os

# get environment variables from the Python environment
from dotenv import load_dotenv
from typing import Optional

# loads external variables from a .env file or the operating system
load_dotenv()


class SWCConfing:
    """
    Configuration class containing arguments for the SDK client.
    Contains configuration for the base URL and progressive backoff.
    """

    # use to access API
    swc_base_url: str
    # determines if SDK should retry the call or not
    swc_backoff: bool
    # the max number of seceonds the SDK should keep trying an API call before stopping
    swc_backoff_max_time: int
    # set format for the bulk files
    swc_bulk_file_format: str

    # when you create an instance from this class, set the class variables from the parameters the user passes in.
    # + default values set here
    def __init__(
        self,
        swc_base_url: Optional[str] = None,
        backoff: bool = True,
        backoff_max_time: int = 30,
        bulk_file_format: str = "csv",
    ):
        """
        Constructor for configuration class.
        Contains initilization values to overwrite default.
        Args:
            swc_base_url (optional):
                The base URL to use for all the API calls. Pass this in or set in environment variable.
            swc_backoff:
                A boolean that determines if the SDK should retry the call using backoff when errors occur.
            swc_backoff_max_time:
                The max number of seconds the SDK should keep trying an API call before stopping.
            swc_bulk_file_format:
                If bulk files should be in csv or parquet format.
        """
        self.swc_base_url = swc_base_url or os.getenv("SWC_API_BASE_URL")
        print(f"SWC_API_BASE_URL in SWCConfig init: {self.swc_base_url}")

        if not self.swc_base_url:
            raise ValueError(
                "Base URL is required. Set SWC_API_BASE_URL environment variable."
            )

        self.swc_backoff = backoff
        self.swc_backoff_max_time = backoff_max_time
        self.swc_bulk_file_format = bulk_file_format

    # log the content of the class -> if you don't create it a default one will get created which will have less useful information
    def __str__(self):
        """Stringify function to return contents of confing object for logging"""
        return f"{self.swc_base_url} {self.swc_backoff} {self.swc_backoff_max_time} {self.swc_bulk_file_format}"
