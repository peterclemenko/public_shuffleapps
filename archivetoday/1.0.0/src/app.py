import time
import json
import socket
import asyncio
import requests
import archiveis

from walkoff_app_sdk.app_base import AppBase

class ArchiveToday(AppBase):
    __version__ = "1.0.0"
    app_name = "Archive.today"    # this needs to match "name" in api.yaml

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
        #archive_url = archiveis.capture("target")
#        return archive_url
        """
        Returns log of what was archived
        """
        message = f"target {target} has been archived"

        # This logs to the docker logs
        self.logger.info(message)
         return target


    async def hello_world(self):
        """
        Returns Hello World from the hostname the action is run on
        :return: Hello World from your hostname
        """
        message = f"Hello World from {socket.gethostname()} in workflow {self.current_execution_id}!"

        # This logs to the docker logs
        self.logger.info(message)

        return message

if __name__ == "__main__":
    asyncio.run(ArchiveToday.run(), debug=True)
