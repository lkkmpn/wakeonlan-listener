# wakeonlan-listener

`wakeonlan-listener` is a simple Python 2.7 listener for wake on lan packets. It
was written to allow people to boot their computer from outside their local
network, since most routers don't allow opening ports to the broadcast IP (the
IP where wake on lan packets are sent to).

`wakeonlan-listener` works by listening to wake on lan packets (on a port that
can be opened to outside connections, hosted on for example a Raspberry Pi), and
then rebroadcasting them to the broadcast IP (from inside the local network).

## Setup

This project doesn't depend on any other packages. Just download `listener.py`
and place it anywhere.

`wakeonlan-listener` can be run from the command line using the following
command:

    $ python listener.py [options]

All of the options are optional. Possible options are:

* `-h`/`--help`: show all options
* `--listen-ip`: IP to listen for incoming packets (default: `''`, all incoming
connections)
* `--listen-port`: Port to listen for incoming packets (default: `10000`)
* `--broadcast-ip`: Broadcast IP of local network (default: `'192.168.1.255'`,
change this depending on your local network configuration)
* `--broadcast-port`: Broadcast port on local network (default: `9`, default
wake on lan port)

## License

This project is licensed under the MIT License, see the [LICENSE](LICENSE) file
for details.