import sys
from Scripts.server_handling import *
from Scripts.default_handler import *

handlers = {
    "startall": start_servers,
    "stopall": stop_servers
}

input_argument = sys.argv[1]
action_handler = handlers.get(input_argument, default_handler)
action_handler()
