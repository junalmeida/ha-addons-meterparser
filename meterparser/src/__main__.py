from app.mqtt import Mqtt
from app.service import Service
import sys
import signal
import argparse
import logging
_LOGGER = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument('--token', required=True)
known_args, unknown_args = parser.parse_known_args()
token = known_args.token

if not token or token == "":
    _LOGGER.error("No token provided. Exiting...")
    sys.exit(1)

mqtt = Mqtt(token)
service = Service(mqtt.cameras)
def signal_handler(sig, frame):
    print('Exiting...')
    mqtt.mqtt_stop()
    sys.exit(0)

def run():
    service.start()
    mqtt.mqtt_start() # locks the execution

signal.signal(signal.SIGINT, signal_handler)
run()