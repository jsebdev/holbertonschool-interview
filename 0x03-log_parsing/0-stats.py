#!/usr/bin/env python3
import sys
import signal
import time


def printStatus(statusCodes):
    status = [(k, statusCodes[k]) for k in statusCodes.keys()]
    status.sort(key=lambda x: x[0])
    for (st, times) in status:
        print("{}: {}".format(st, times))


def printStats(totalSize, statusCodes):
    print("File size: {:d}".format(totalSize))
    printStatus(statusCodes)


if __name__ == '__main__':
    try:
        lineCounter = 0
        totalSize = 0
        statusCodes = {}
        for line in sys.stdin:
            line = line.split()
            totalSize = totalSize + int(line[8])
            statusCodes[line[7]] = statusCodes[line[7]] + \
                1 if line[7] in statusCodes else 1
            lineCounter = lineCounter + 1
            print(lineCounter)
            if lineCounter % 4 == 0:
                printStats(totalSize, statusCodes)
    except(KeyboardInterrupt, SystemExit):
        printStats(totalSize, statusCodes)
        raise