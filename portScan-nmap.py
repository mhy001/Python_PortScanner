import argparse
import nmap
from socket import *
def nmapScan(tgtHost, tgtPort):
  nm = nmap.PortScanner()
  nm.scan(tgtHost, tgtPort)
  try:
    tgtIP = gethostbyname(tgtHost)
  except:
    print('[-] Cannot resolve %s: Unknown host' %tgtHost)
  state = nm[tgtIP]['tcp'][int(tgtPort)]['state']
  print('[*] '+tgtHost+' tcp/'+tgtPort+' '+state)
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
  for tgtPort in tgtPorts:
    nmapScan(tgtHost, tgtPort)
if __name__ == "__main__":
  main()
