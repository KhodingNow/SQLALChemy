import socket

def discover_open_ports(target_host, port_range):
    open_ports = []

    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt

        result = sock.connect_ex((target_host, port))

        if result == 0:
            open_ports.append(port)

        sock.close()

    return open_ports


if __name__ == '__main__':

    target_host = 'example.com'
    port_range = range(1, 1024)  # A range of ports to scan

    open_ports = discover_open_ports(target_host, port_range)

    if open_ports:
        print('Open ports:')
        for port in open_ports:
            print(port)

    else:
        print('No open ports found.')

