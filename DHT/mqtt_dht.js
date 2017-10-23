[
    {
        "id": "6fe402cf.7e39dc",
        "type": "mqtt in",
        "z": "afdb9cdd.4814c",
        "name": "",
        "topic": "esp2/sensor",
        "qos": "0",
        "broker": "c6ab789d.5ca2f8",
        "x": 190,
        "y": 140,
        "wires": [
            [
                "7f21aa7c.646214"
            ]
        ]
    },
    {
        "id": "7f21aa7c.646214",
        "type": "json",
        "z": "afdb9cdd.4814c",
        "name": "",
        "pretty": false,
        "x": 290,
        "y": 180,
        "wires": [
            [
                "b935c751.d846e8",
                "e6354a85.2aa198",
                "162fb528.786bcb"
            ]
        ]
    },
    {
        "id": "7a5c771f.0213e8",
        "type": "ui_gauge",
        "z": "afdb9cdd.4814c",
        "name": "",
        "group": "ddf9385a.2644e8",
        "order": 0,
        "width": 0,
        "height": 0,
        "gtype": "gage",
        "title": "Gauge",
        "label": "",
        "format": "{{'%.1f'|sprintf:value}}°C",
        "min": "10",
        "max": "60",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "x": 570,
        "y": 140,
        "wires": []
    },
    {
        "id": "a5577d7.0cf968",
        "type": "ui_gauge",
        "z": "afdb9cdd.4814c",
        "name": "",
        "group": "ddf9385a.2644e8",
        "order": 0,
        "width": 0,
        "height": 0,
        "gtype": "gage",
        "title": "Gauge",
        "label": "",
        "format": "{{'%.1f'|sprintf:value}}%",
        "min": 0,
        "max": "100",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "x": 570,
        "y": 220,
        "wires": []
    },
    {
        "id": "b935c751.d846e8",
        "type": "change",
        "z": "afdb9cdd.4814c",
        "name": "temperature",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "payload.temperature",
                "tot": "msg"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 430,
        "y": 140,
        "wires": [
            [
                "7a5c771f.0213e8"
            ]
        ]
    },
    {
        "id": "e6354a85.2aa198",
        "type": "change",
        "z": "afdb9cdd.4814c",
        "name": "humidity",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "payload.humidity",
                "tot": "msg"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 420,
        "y": 220,
        "wires": [
            [
                "a5577d7.0cf968"
            ]
        ]
    },
    {
        "id": "162fb528.786bcb",
        "type": "debug",
        "z": "afdb9cdd.4814c",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 420,
        "y": 80,
        "wires": []
    },
    {
        "id": "c6ab789d.5ca2f8",
        "type": "mqtt-broker",
        "z": "",
        "broker": "192.168.0.107",
        "port": "1883",
        "clientid": "",
        "usetls": false,
        "compatmode": true,
        "keepalive": "60",
        "cleansession": true,
        "willTopic": "",
        "willQos": "0",
        "willPayload": "",
        "birthTopic": "",
        "birthQos": "0",
        "birthPayload": ""
    },
    {
        "id": "ddf9385a.2644e8",
        "type": "ui_group",
        "z": "",
        "name": "ESP-01",
        "tab": "bbc75cb6.1440f",
        "disp": true,
        "width": "6"
    },
    {
        "id": "bbc75cb6.1440f",
        "type": "ui_tab",
        "z": "",
        "name": "Mushroom",
        "icon": "dashboard"
    }
]
