import argparse
import socket
from socket import *
def connScan(tgtHost, tgtPort):
  try:
    connSkt = socket(AF_INET, SOCK_STREAM)
    connSkt.connect((tgtHost, tgtPort))
    connSkt.send('ViolentPython\r\n')
    results = connSkt.recv(100)
    print('  [+] %d/tcp open ' %tgtPort)
    print('  [+] '+str(results))
    connSkt.close()
  except:
    print('  [-] %d/tcp closed ' %tgtPort)
def portScan(tgtHost, tgtPorts):
  try:
    tgtIP = gethostbyname(tgtHost)
  except:
    print('[-] Cannot resolve %s: Unknown host' %tgtHost)
    return
  try:
    tgtName = gethostbyaddress(tgtIP)
    print('[+] Scan results for: '+tgtName[0])
  except:
    print('[+] Scan results for: '+tgtIP)
  setdefaulttimeout(1)
  for tgtPort in tgtPorts:
    connScan(tgtHost, int(tgtPort))
def main():
  parser = argparse.ArgumentParser(usage='portScan.py '\
    +'-H <target host> -p <target port>')
  parser.add_argument('-H', dest='tgtHost', type=str,\
    help='specify target host')
  parser.add_argument('-p', dest='tgtPorts', type=str,\
    help='specify target port[s] separated by commas')
  args = parser.parse_args()
  tgtHost = args.tgtHost
  tgtPorts = str(args.tgtPorts).split(', ')
  if (tgtHost == None) | (tgtPorts == None):
    print(parser.usage)
    exit(0)
  portScan(tgtHost, tgtPorts)
if __name__ == "__main__":
  main()
