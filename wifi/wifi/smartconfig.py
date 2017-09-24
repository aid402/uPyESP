def smartconfig():
    html = """<!DOCTYPE html>
    <html>
        <head> <title>ESP8266 Smart Config</title> </head>
        <body> <h1 style="color:White;background-color:DodgerBlue">ESP8266 Smart Config</h1>
                <table border="1"> <tr><th>SSID</th><th>channel</th><th>signal</th></tr> %s </table>
        </body>
    </html>
    """
    form = """<form action="/connect" method="post">
    <div>
        <label for="SSID">SSID:</label>
        <input type="text" id="ssid" name="ssid">
    </div>
    <div>
        <label for="password">password:</label>
        <input type="text" id="password" name="password">
    </div>
    <div class="button">
        <button type="submit">Connect</button>
    </div>
    </form>
    """
 
    import socket
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    import network
    print('listening on', addr)
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    ap_scan = sta_if.scan()
    
    while True:
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        print(str(request))
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
        rows = ['<tr><td>%s</td><td>%d</td><td>%d</td></tr>' % (bytes.decode(i[0]), i[2], i[3]) for i in ap_scan]
        response = html % '\n'.join(rows)
        response = response% '\n'.join(form)
        cl.send(response)
        cl.close()
