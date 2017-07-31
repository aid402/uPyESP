import machine,os,sys,network
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    aplist = sta_if.scan()
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('LP_wireles', '1871157210')
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig())
