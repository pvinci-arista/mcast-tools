import argparse
import socket

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--group", default="224.0.0.1")
parser.add_argument("-p", "--port", default=5007)
parser.add_argument("-t", "--ttl", default=2)
args = parser.parse_args()

MCAST_GRP = args.group
MCAST_PORT = args.port
# regarding socket.IP_MULTICAST_TTL
# ---------------------------------
# for all packets sent, after two hops on the network the packet will not 
# be re-sent/broadcast (see https://www.tldp.org/HOWTO/Multicast-HOWTO-6.html)
MULTICAST_TTL = args.ttl

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

# For Python 3, change next line to 'sock.sendto(b"robot", ...' to avoid the
# "bytes-like object is required" msg (https://stackoverflow.com/a/42612820)
print(f"PKT SENT -- MCAST_GRP:{MCAST_GRP} MCAST_PORT:{MCAST_PORT}  MULTICAST_TTL:{MULTICAST_TTL}")
sock.sendto(f"PKT SENT -- MCAST_GRP:{MCAST_GRP} MCAST_PORT:{MCAST_PORT}  MULTICAST_TTL:{MULTICAST_TTL}".encode(), (MCAST_GRP, MCAST_PORT))