import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--token', required=True)
parser.add_argument('--debug', required=False)
known_args, unknown_args = parser.parse_known_args()
token = known_args.token

logging.basicConfig(level=logging.DEBUG if known_args.debug else logging.INFO, format='[%(asctime)s] %(levelname)s: [%(name)s] %(message)s', datefmt='%H:%M:%S')
_LOGGER = logging.getLogger(__name__)

from app.mqtt import Mqtt
from app.service import Service
import sys
import signal



if not token or token == "":
    _LOGGER.error("No token provided. Exiting...")
    sys.exit(1)
_LOGGER.info("Meterparser started")

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