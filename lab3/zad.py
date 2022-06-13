import os, sys, optparse

LOGFILE="setupapi.dev.log"
KEYWORDS='[Device Install (Hardware initiated)'
KEYWORD2='USBSTOR'

with open(LOGFILE, "r") as in_file:
    for line in in_file:
        if KEYWORDS in line and KEYWORD2 in line:
            line_data=line.split("#")
            serial_number=line_data[2]
            dev_info=line_data[1].split("&")
            print(f"Serial number:{serial_number}")
            print(f"Vendor Id: {dev_info[1]}")
            print(f"Product ID: {dev_info[2]}")
            print(f"Revision: {dev_info[3]}")
            print(next(in_file).split("start")[1].strip())
            print("\n")