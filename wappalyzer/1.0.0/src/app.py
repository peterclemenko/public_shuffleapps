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



    async def analyze_target(self, code, shuffle_input):
        process = subprocess.Popen(code, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        stdout = process.communicate()
        item = ""
        if len(stdout[0]) > 0:
            print("Succesfully ran bash!")
            item = stdout[0]
        else:
            print("FAILED to run bash!")
            item = stdout[1]
    
        try:
            ret = item.decode("utf-8")
            return ret 
        except:
            return item

        return item

"""
    async def analyze_target(self, target, batchSize, delay, maxdepth, maxurls, maxwait, recursive, useragent, htmlmaxcols, htmlmaxrows):

     
        code = "wappalyzer " + target
        self.logger.info(code)
        process = subprocess.Popen(code, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        stdout = process.communicate()
        item = ""
        if len(stdout[0]) > 0:
            print("Succesfully ran bash!")
            item = stdout[0]
        else:
            print("FAILED to run bash!")
            item = stdout[1]
    
        try:
            ret = item.decode("utf-8")
            self.logger.info(ret)
            return ret 
        except:
            return item

        return item

"""
if __name__ == "__main__":
    asyncio.run(Wappalyzer.run(), debug=True)
