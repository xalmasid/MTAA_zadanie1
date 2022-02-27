import socketserver
import sipfullproxy as sfp
import socket


def main():
    print("Spusta sa server")
    PORT = 5060
    HOST = "0.0.0.0"
    ip = socket.gethostbyname(socket.gethostname())
    print(f"IP: {ip}:{PORT}")

    sfp.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ip, PORT)
    sfp.topvia = "Via: SIP/2.0/UDP %s:%d" % (ip, PORT)
    s = socketserver.UDPServer((HOST, PORT), sfp.UDPHandler)
    s.serve_forever()


if __name__ == '__main__':
    main()
