import optparse
from socket import *


def get_options():
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify the ports to scan, separated by a comma')
    (options, args) = parser.parse_args()
    target_host = options.tgtHost
    target_ports = str(options.tgtPort).split(', ')
    if (None == target_host) | (None == target_ports[0]):
        print(parser.usage)
        exit(0)
    return target_host, target_ports


def scan_port(target, port):
    try:
        conn_socket = socket(AF_INET, SOCK_STREAM)
        conn_socket.connect((target, port))
        conn_socket.send('HelloWorld')
        results = conn_socket.recv(2048)
        print('    Found open port: ' + str(port))
        print('    Port information: ' + results)
        conn_socket.close()
    except:
        print('    Timeout, socket closed.')


def create_connection(host, ports):
    try:
        target_name = gethostbyname(host)
    except:
        print('Unable to resolve ' + host + ': Unknown host.')
        return
    try:
        target_ip = gethostbyaddr(target_name)
        print('Scanning target: ' + target_ip[0])
    except:
        print('Scanning target: ' + target_name)
    setdefaulttimeout(2)
    for port in ports:
        print('  Scanning ' + host + ' on port ' + port + ': ')
        scan_port(host, int(port))


def main():
    parser = optparse.OptionParser(usage='%prog -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify the ports to scan, separated by a comma')
    (options, args) = parser.parse_args()
    target_host = options.tgtHost
    target_ports = str(options.tgtPort).split(', ')
    if (target_host == None) | (None == target_ports[0]):
        print(parser.usage)
        exit(0)
    create_connection(target_host, target_ports)


if __name__ == '__main__':
    main()
