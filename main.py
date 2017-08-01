import machine,os,sys,network,time
sta_if = network.WLAN(network.STA_IF)
ap_stock = [('LP_wireless','1871157210')] #My APs
if not sta_if.isconnected():
    ap_scan = sta_if.scan()
    for i in ap_scan:
        ap = str(i[0].'utf-8')
        for p in ap_stock:
            if ap == ap_stock[p][0]:
                print('connecting to network...')
                sta_if.active(True)
                sta_if.connect(ap_stock[p][0], ap_stock[p][1])
                while not sta_if.isconnected():
                    pass
                break
        if sta_if.isconnected():
            print('network config:', sta_if.ifconfig())
            break
    if not sta_if.isconnected():
        print('STATION is not connect. Please connect by your self นะครับ')
else:
    print('network config:', sta_if.ifconfig())
