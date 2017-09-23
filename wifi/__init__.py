import network
from wifi.aplist import aplist
from wifi.connect import connect
from wifi.smartconfig import smartconfig



def smartconfig():
    html = """<!DOCTYPE html>
    <html>
        <head> <title>ESP8266 Smart Config</title> </head>
        <body> <h1>ESP8266 Smart Config</h1>
                <table border="1"> <tr><th>SSID</th><th>Value</th></tr> %s </table>
        </body>
    </html>
    """

    import socket
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print('listening on', addr)
    sta_if = network.WLAN(network.STA_IF)
    ap_scan = sta_if.scan()
    
    while True:
        cl, addr = s.accept()
        print('client connected from', addr)
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
        rows = ['<tr><td>%s</td><td>%d</td></tr>' % (bytes.decode(i[0]), bytes.decode(i[1])) for i in ap_scan]
        response = html % '\n'.join(rows)
        cl.send(response)
        cl.close()        
