import argparse
import socket
import struct

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--all-groups", action="store_true")
parser.add_argument("-g", "--group", default="224.0.0.1")
parser.add_argument("-p", "--port", default=5007)
parser.add_argument("-t", "--ttl", default=2)
args = parser.parse_args()
print("listening on:")
if args.all_groups:
  print(f"group: ALL")
else:    
  print(f"group: {args.group}")
print(f"port: {args.port}")
print(f"ttl: {args.ttl}")
print("press ^C to exit")
MCAST_GRP = args.group
MCAST_PORT = args.port
IS_ALL_GROUPS = args.all_groups

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if IS_ALL_GROUPS:
    # on this port, receives ALL multicast groups
    sock.bind(('', MCAST_PORT))
else:
    # on this port, listen ONLY to MCAST_GRP
    sock.bind((MCAST_GRP, MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
  print (sock.recv(10240))