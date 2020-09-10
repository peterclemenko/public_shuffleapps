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

        cmd = (['wappalyzer' ])
       
        cmd.append(target)
        '''if batchSize != "":
            cmd.append("--batch-size=" + batchSize)

        if delay != "":
            cmd.append("--delay=" + delay)

        if maxdepth != "":
            cmd.append("--max-depth=" + maxdepth)

        if maxurls != "":
            cmd.append("--max-urls=" + maxurls)

        if maxwait != "":
            cmd.append("--max-wait=" + maxwait)

        if recursive == True:
            cmd.append("--recursive")

        if useragent != "":
            cmd.append("--user-agent=" + useragent)

        if htmlmaxcols != "":
            cmd.append"--html-max-cols=" + htmlmaxcols)

        if htmlmaxrows != "":
            cmd.append("--html-max-rows=" + htmlmaxrows)'''

        self.logger.info(cmd) 

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
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


if __name__ == "__main__":
    asyncio.run(Wappalyzer.run(), debug=True)
