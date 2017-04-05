import argparse
import socket
import sys


def listen(listen_ip, listen_port, broadcast_ip, broadcast_port):
    """Listen for incoming UDP wake on lan packets at `listen_ip`:`listen_port`,
    and redirect these packets to `broadcast_ip`:`broadcast_port`.

    :listen_ip: the IP to use to listen to incoming connections
    :listen_port: the port to use to listen to incoming connections
    :broadcast_ip: the broadcast IP of the local network
    :broadcast_port: the port to broadcast the wake on lan packet to
    """

    # define socket to listen for incoming connections, and bind
    try:
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        listen_socket.bind((listen_ip, listen_port))
    except socket.error as e:
        print 'Socket error while trying to listen for incoming connections:'
        print e
        sys.exit()

    # define socket to broadcast to, and enable as broadcast socket
    try:
        broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    except socket.error as e:
        print 'Socket error while trying to enable broadcast socket:'
        print e
        sys.exit()

    print 'Listening on %s:%i, rebroadcasting to %s:%i' % \
        (listen_ip, listen_port, broadcast_ip, broadcast_port)

    # listen to incoming packets forever
    while True:
        data, addr = listen_socket.recvfrom(1024)

        # check if incoming packet is a wake on lan packet, so check if it
        # starts with ff:ff:ff:ff:ff:ff
        if [ord(n) for n in data[:6]] == [255] * 6:
            print 'Received magic packet from %s, rebroadcasted' % addr[0]
            broadcast_socket.sendto(data, (broadcast_ip, broadcast_port))


if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('--listen-ip',
                        help='IP to listen for incoming packets '
                             '(default: \'\', all incoming connections)',
                        default='',
                        type=str)
    parser.add_argument('--listen-port',
                        help='Port to listen for incoming packets '
                             '(default: 10000)',
                        default=10000,
                        type=int)
    parser.add_argument('--broadcast-ip',
                        help='Broadcast IP of local network '
                             '(default: \'192.168.1.255\')',
                        default='192.168.1.255',
                        type=str)
    parser.add_argument('--broadcast-port',
                        help='Broadcast port on local network '
                             '(default: 9)',
                        default=9,
                        type=int)
    args = parser.parse_args()

    try:
        listen(args.listen_ip,
               args.listen_port,
               args.broadcast_ip,
               args.broadcast_port)
    except KeyboardInterrupt:
        exit
