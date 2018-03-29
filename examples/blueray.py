#!/usr/bin/env python2.7
from itachip2ir import iTach, device


def bluerayTest():
    itach = iTach("Tester iTach ip2ir", "192.168.1.12")
    blueray = device("Blueray Player", itach)
    blueray.set_command("toggle_power", "sendir,1:3,1,40192,1,1,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,529,96,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,528,96,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,553,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,554,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,554,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,554,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,49,23,49,23,49,4000")
    blueray.send_commands("toggle_power", 3)


if __name__ == "__main__":
    bluerayTest()
