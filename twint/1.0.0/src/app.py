import time
import json
import socket
import asyncio
import requests
import subprocess

from walkoff_app_sdk.app_base import AppBase

class Twint(AppBase):
    __version__ = "1.0.0"
    app_name = "Twint"  

    def __init__(self, redis, logger, console_logger=None):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        self.headers = {"Content-Type": "application/json"}
        super().__init__(redis, logger, console_logger)


    async def get_user_tweets(self, target, data):
   
        cmd = "twint -u " + target
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        
        (output, err) = p.communicate()
        p_status = p.wait()

        """
        Returns log of what was wappalyzed
        """
        message = f"target {target} has been wappalyzed with command {cmd}"

        # This logs to the docker logs
        self.logger.info(message)
        return output

# Run the actual thing after we've checked params
def run(request):
    action = request.get_json() 
    print(action)
    print(type(action))
    authorization_key = action.get("authorization")
    current_execution_id = action.get("execution_id")
	
    if action and "name" in action and "app_name" in action:
        asyncio.run(Twint.run(action), debug=True)
        return f'Attempting to execute function {action["name"]} in app {action["app_name"]}' 
    else:
        return f'Invalid action'

if __name__ == "__main__":
    asyncio.run(Twint.run(), debug=True)
