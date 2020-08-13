import time
import json
import socket
import asyncio
import requests
import subprocess

from walkoff_app_sdk.app_base import AppBase

class Wappalyzer(AppBase):
    __version__ = "1.0.0"
    app_name = "Wappalyzer"    # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):
        """
        Each app should have this __init__ to set up Redis and logging.
        :param redis:
        :param logger:
        :param console_logger:
        """
        self.headers = {"Content-Type": "application/json"}
        super().__init__(redis, logger, console_logger)


    async def analyze_target(self, target, batchSize, delay, maxdepth, maxurls, maxwait, recursive, useragent, htmlmaxcols, htmlmaxrows):

        cmd = "wappalyzer"
        if batchSize != "":
            cmd = cmd + " --batch-size=" + batchSize

        if delay != "":
            cmd = cmd + " --delay=" + delay

        if maxdepth != "":
            cmd = cmd + " --max-depth=" + maxdepth

        if maxurls != "":
            cmd = cmd + " --max-urls=" + maxurls

        if maxwait != "":
            cmd = cmd + " --max-wait=" + maxwait

        if recursive == True:
            cmd = cmd + " --recursive"

        if useragent != "":
            cmd = cmd + " --user-agent=" + useragent

        if htmlmaxcols != "":
            cmd = cmd + " --html-max-cols=" + htmlmaxcols

        if htmlmaxrows != "":
            cmd = cmd + " --html-max-rows=" + htmlmaxrows

        cmd = cmd + " " + target
        
        p = subprocess.Popen("wappalyzer", stdout=subprocess.PIPE, shell=True)
        
        (output, err) = p.communicate()
        p_status = p.wait()

        """
        Returns log of what was wappalyzed
        """
        message = f"target {target} has been wappalyzed"

        # This logs to the docker logs
        self.logger.info(message)
        return output

if __name__ == "__main__":
    asyncio.run(Wappalyzer.run(), debug=True)
