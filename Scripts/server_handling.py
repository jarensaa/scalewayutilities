import os


def start_servers():
    os.system("scw ps -a | grep stopped | cut -c1-8 | xargs scw --region=par1 start")
    os.system("scw ps -a | grep stopped | cut -c1-8 | xargs scw --region=ams1 start")


def stop_servers():
    os.system(
        "scw ps | grep ams1 | grep running | cut -c1-8 | xargs scw --region=ams1 stop")
    os.system(
        "scw ps | grep par1 | grep running | cut -c1-8 | xargs scw --region=par1 stop")
