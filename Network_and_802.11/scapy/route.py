#!/usr/bin/env python

__author__ = "bt3"

from scapy.all import *

print conf.route

conf.route.add(host='192.168.118.2', gw='192.168.1.114')

print conf.route

conf.route.resync()

print conf.route