import argparse
from socket import *
from threading import *
screenLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
  try:
    connSkt = socket(AF_INET, SOCK_STREAM)
    connSkt.connect((tgtHost, tgtPort))
    connSkt.send('ViolentPython\r\n')
    results = connSkt.recv(100)
    screenLock.acquire()
    print('  [+] %d/tcp open ' %tgtPort)
    print('  [+] '+str(results))
  except:
    screenLock.acquire()
    print('  [-] %d/tcp closed' %tgtPort)
  finally:
    screenLock.release()
    connSkt.close()
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
    t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
    t.start()
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
