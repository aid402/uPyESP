import apname,network
sta_if = network.WLAN(network.STA_IF)
ap_stock=apname.stock()

def main():
    if not sta_if.isconnected():
        ap_scan = sta_if.scan()
        for i in ap_scan:
            ap_i = i[0].decode('utf-8')
            for p in ap_stock:
                if ap_i == p[0]:
                    print('connecting to network...')
                    sta_if.active(True)
                    sta_if.connect(p[0], p[1])
                    while not sta_if.isconnected():
                        pass
                    break
            if sta_if.isconnected():
                print('network config :', sta_if.ifconfig())
                break
        if not sta_if.isconnected():
            led=machine.Pin(2,machine.Pin.OUT)
            led=off()
    else:
        print('network is connected:', sta_if.ifconfig())
