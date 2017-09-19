import aplist,network

def connect():
    from machine import Pin
    led = Pin(2,Pin.OUT,value=0)
    sta_if = network.WLAN(network.STA_IF)
    ap_stock = aplist.stock()
    if not sta_if.isconnected():
        ap_scan = sta_if.scan()
        for i in ap_scan:
            ap_i = bytes.decode(i[0])
            for p in ap_stock:
                if ap_i == p[0]:
                    sta_if.active(True)
                    sta_if.connect(p[0], p[1])
                    while not sta_if.isconnected():
                        pass
                    break
            if sta_if.isconnected():
                led.value(1)
                return sta_if.ifconfig()[0]
                break
    else:
        led.value(1)
        return sta_if.ifconfig()[0]

def smartconfig():
    html = """<!DOCTYPE html>
    <html>
        <head> <title>ESP8266 Pins</title> </head>
        <body> <h1>ESP8266 Pins</h1>
            <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
        </body>
    </html>
    """

    import socket
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print('listening on', addr)

    while True:
        cl, addr = s.accept()
        print('client connected from', addr)
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
        rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
        response = html % '\n'.join(rows)
        cl.send(response)
        cl.close()
