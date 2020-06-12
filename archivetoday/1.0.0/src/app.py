import time
import json
import socket
import asyncio
import requests
import archiveis

from walkoff_app_sdk.app_base import AppBase

class ArchiveToday(AppBase):
    __version__ = "1.0.0"
    app_name = "archivetoday"  

    def __init__(self, redis, logger, console_logger=None):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        self.headers = {"Content-Type": "application/json"}
        super().__init__(redis, logger, console_logger)


    async def archive_target(self, target, data):
        archive_url = archiveis.capture("target")
        return archive_url

# Run the actual thing after we've checked params
def run(request):
    action = request.get_json() 
    print(action)
    print(type(action))
    authorization_key = action.get("authorization")
    current_execution_id = action.get("execution_id")
	
    if action and "name" in action and "app_name" in action:
        asyncio.run(ArchiveToday.run(action), debug=True)
        return f'Attempting to execute function {action["name"]} in app {action["app_name"]}' 
    else:
        return f'Invalid action'

if __name__ == "__main__":
    asyncio.run(ArchiveToday.run(), debug=True)
