from socket import *
import os
import sys
import struct
import time
import select

ICMP_ECHO_REQUEST = 8

def checksum(data):
    csum = 0
    countTo = (len(data) // 2) * 2
    count = 0
    while count < countTo:
        # In Python 3, data[...] returns an int, so no need for ord()
        thisVal = data[count+1] * 256 + data[count]
        csum = csum + thisVal
        csum = csum & 0xffffffff
        count += 2
    if countTo < len(data):
        csum = csum + data[-1]
        csum = csum & 0xffffffff
    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum & 0xffff
    # Swap bytes
    answer = (answer >> 8) | ((answer & 0xff) << 8)
    return answer

def receiveOnePing(mySocket, ID, timeout, destAddr):
    timeLeft = timeout
    while True:
        startedSelect = time.time()
        whatReady = select.select([mySocket], [], [], timeLeft)
        howLongInSelect = time.time() - startedSelect
        if whatReady[0] == []:  # Timeout
            return "Request timed out."
        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)
        # The IP header is the first 20 bytes; ICMP header starts at byte 20.
        icmpHeader = recPacket[20:28]
        icmpType, icmpCode, icmpChecksum, icmpID, icmpSequence = struct.unpack("bbHHh", icmpHeader)
        # Verify this is our ping reply (by matching the ID)
        if icmpID == ID:
            timeSent = struct.unpack("d", recPacket[28:28 + struct.calcsize("d")])[0]
            return timeReceived - timeSent
        timeLeft = timeLeft - howLongInSelect
        if timeLeft <= 0:
            return "Request timed out."

def sendOnePing(mySocket, destAddr, ID):
    # Header: type (8), code (8), checksum (16), id (16), sequence (16)
    myChecksum = 0
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack("d", time.time())
    myChecksum = checksum(header + data)
    if sys.platform == 'darwin':
        myChecksum = htons(myChecksum) & 0xffff
    else:
        myChecksum = htons(myChecksum)
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    packet = header + data
    mySocket.sendto(packet, (destAddr, 1))

def doOnePing(destAddr, timeout):
    icmp = getprotobyname("icmp")
    mySocket = socket(AF_INET, SOCK_RAW, icmp)
    myID = os.getpid() & 0xFFFF
    sendOnePing(mySocket, destAddr, myID)
    delay = receiveOnePing(mySocket, myID, timeout, destAddr)
    mySocket.close()
    return delay

def ping(host, timeout=1):
    dest = gethostbyname(host)
    print("Pinging " + dest + " using Python:", flush=True)
    print("", flush=True)
    while True:
        delay = doOnePing(dest, timeout)
        # Print and flush immediately so that output is written to file
        print(delay, flush=True)
        time.sleep(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py <hostname>")
        sys.exit(1)
    host = sys.argv[1]
    ping(host)
