import os
import requests
import sys
import time
import logging
_LOGGER = logging.getLogger(__name__)

supervisor_api = "http://supervisor/%s"


def supervisor(param: str):
    while True:
        try:
            _LOGGER.debug("Connecting to supervisor...")    
            supervisor_auth = {
                "Authorization": "Bearer %s" % os.environ['SUPERVISOR_TOKEN']
            }

            result = requests.get(supervisor_api % (
                "services/" + param), headers=supervisor_auth)
            result_json = result.json()
            return result_json["data"] if "data" in result_json else None

        except Exception as e:
            _LOGGER.error("Could not connect to supervisor: %s. Retry in 5 secs." % e)
            time.sleep(5)
def version() -> str:
    try:
        if "SUPERVISOR_TOKEN" in os.environ:
            supervisor_auth = {
                "Authorization": "Bearer %s" % os.environ['SUPERVISOR_TOKEN']
            }

            result = requests.get(supervisor_api % ("addons/self/info"), headers=supervisor_auth)
            result_json = result.json()
            result_json = result_json["data"] if "data" in result_json else result_json
            return result_json["version"] if "version" in result_json else "0.0.0.0"
        else:
            return "0.0.0.0"
    except Exception as e:
        _LOGGER.error("Could not connect to supervisor: %s" % e)
        return "0.0.0.0"

def hostname() -> str:
    try:
        if "SUPERVISOR_TOKEN" in os.environ:
            supervisor_auth = {
                "Authorization": "Bearer %s" % os.environ['SUPERVISOR_TOKEN']
            }

            result = requests.get(supervisor_api % ("addons/self/info"), headers=supervisor_auth)
            result_json = result.json()
            result_json = result_json["data"] if "data" in result_json else result_json
            return result_json["hostname"] if "hostname" in result_json else "unknown"
        else:
            return "unknown"
    except Exception as e:
        _LOGGER.error("Could not connect to supervisor: %s" % e)
        return "unknown"        