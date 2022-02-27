import socketserver
import sipfullproxy as sfp
import socket
import logging
import time


def main():
    print("Spusta sa server")
    PORT = 5060
    HOST = "0.0.0.0"
    ip = socket.gethostbyname(socket.gethostname())
    print(ip + ":" + str(PORT))
    logging.info('IP: ' + ip)

    sfp.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ip, PORT)
    sfp.topvia = "Via: SIP/2.0/UDP %s:%d" % (ip, PORT)
    s = socketserver.UDPServer((HOST, PORT), sfp.UDPHandler)
    s.serve_forever()


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='mtaa_proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("\n\t======PROXY SERVER=======\n" + "%a, %d %b %Y %H:%M:%S", time.localtime()))
    main()
