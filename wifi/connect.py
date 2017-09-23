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
            else:
                return NULL
    else:
        led.value(1)
        return sta_if.ifconfig()[0]
