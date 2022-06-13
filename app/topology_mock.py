""" topology mock """


def topology_mock():
    """ return json data """
    return {
            "id": "urn:sdx:topology:amlight.net",
            "name": "AmLight-OXP",
            "version": 1,
            "model_version": "1.0.0",
            "timestamp": "2000-01-23T04:56:07Z",
            "links": [
                {
                    "id": "urn:sdx:link:amlight:B1:B2",
                    "name": "amlight_B1_B2",
                    "ports": [
                        "urn:sdx:port:amlight.net:B1:2",
                        "urn:sdx:port:amlight.net:B2:2",
                    ],
                    "type": "inter",
                    "bandwidth": 125000000,
                    "residual_bandwidth": 100,
                    "latency": 146582.15146899645,
                    "packet_loss": 59.621339166831824,
                    "availability": 56.37376656633328,
                    "status": "up",
                    "state": "enabled"
                },
                {
                    "id": "urn:sdx:link:amlight:A1:B1",
                    "name": "amlight_A1_B1",
                    "ports": [
                        "urn:sdx:port:amlight.net:A1:1",
                        "urn:sdx:port:amlight.net:B1:3",
                    ],
                    "type": "inter",
                    "bandwidth": 125000000,
                    "residual_bandwidth": 100,
                    "latency": 146582.15146899645,
                    "packet_loss": 59.621339166831824,
                    "availability": 56.37376656633328,
                    "status": "up",
                    "state": "enabled"
                },
                {
                    "id": "urn:sdx:link:amlight:A1:B2",
                    "name": "amlight_A1_B2",
                    "ports": [
                        "urn:sdx:port:amlight.net:A1:2",
                        "urn:sdx:port:amlight.net:B2:3",
                    ],
                    "type": "inter",
                    "bandwidth": 125000000,
                    "residual_bandwidth": 100,
                    "latency": 146582.15146899645,
                    "packet_loss": 59.621339166831824,
                    "availability": 56.37376656633328,
                    "status": "up",
                    "state": "enabled"
                },
                {
                    "id": "urn:sdx:link:nni:Miami:Sanpaolo",
                    "name": "nni_Miami_Sanpaolo",
                    "ports": [
                        "urn:sdx:port:amlight:B1:1",
                        "urn:sdx:port:sax:B1:1",
                    ],
                    "type": "inter",
                    "bandwidth": 125000000,
                    "residual_bandwidth": 100,
                    "latency": 146582.15146899645,
                    "packet_loss": 59.621339166831824,
                    "availability": 56.37376656633328,
                    "status": "up",
                    "state": "enabled"
                },
                {
                    "id": "urn:sdx:link:nni:BocaRaton:Fortaleza",
                    "name": "nni_BocaRaton_Fortaleza",
                    "ports": [
                        "urn:sdx:port:amlight.net:B2:1",
                        "urn:sdx:port:sax:B2:1",
                    ],
                    "type": "inter",
                    "bandwidth": 125000000,
                    "residual_bandwidth": 100,
                    "latency": 146582.15146899645,
                    "packet_loss": 59.621339166831824,
                    "availability": 56.37376656633328,
                    "status": "up",
                    "state": "enabled"
                }
            ],
            "nodes": [
                {
                    "id": "urn:sdx:node:amlight.net:B1",
                    "location": {
                        "address": "Miami",
                        "latitude": 25.75633040531146,
                        "longitude": -80.37676058477908
                    },
                    "name": "amlight_Novi01",
                    "ports": [
                        {
                            "id": "urn:sdx:port:amlight:B1:1",
                            "name": "Novi01_1",
                            "node": "urn:sdx:node:amlight.net:B1",
                            "type": "10GE",
                            "status": "up",
                            "state": "enabled"
                        },
                        {
                            "id": "urn:sdx:port:amlight.net:B1:2",
                            "name": "Novi01_2",
                            "node": "urn:sdx:node:amlight.net:B1",
                            "type": "10GE",
                            "status": "up",
                            "state": "enabled"
                        },
                        {
                            "id": "urn:sdx:port:amlight.net:B1:3",
                            "name": "Novi01_3",
                            "node": "urn:sdx:node:amlight.net:B1",
                            "type": "10GE",
                            "status": "up",
                            "state": "enabled"
                        }
                    ],
                },
                {
                    "id": "urn:sdx:node:amlight.net:B2",
                    "location": {
                        "address": "BocaRaton",
                        "latitude": 26.381437356374075,
                        "longitude": -80.10225977485742
                    },
                    "name": "amlight_Novi02",
                    "ports": [
                        {
                            "id": "urn:sdx:port:amlight.net:B2:1",
                            "name": "Novi02_1",
                            "node": "urn:sdx:node:amlight.net:B2",
                            "type": "10GE",
                            "status": "up",
                            "state": "enabled"
                        },
                        {
                            "id": "urn:sdx:port:amlight.net:B2:2",
                            "name": "Novi02_2",
                            "node": "urn:sdx:node:amlight.net:B2",
                            "type": "10GE",
                            "status": "up",
                            "state": "enabled"
                        },
                        {
                            "id": "urn:sdx:port:amlight.net:B2:3",
                            "name": "Novi02_3",
                            "node": "urn:sdx:node:amlight.net:B2",
                            "type": "10GE",
                            "status": "up",
                            "state": "enabled"
                        }
                    ],
                },
                {
                    "id": "urn:sdx:node:amlight.net:A1",
                    "location": {
                        "address": "redclara",
                        "latitude": 30.34943181039702,
                        "longitude": -81.66666016473143
                    },
                    "name": "amlight_Novi100",
                    "ports": [
                        {
                            "id": "urn:sdx:port:amlight.net:A1:1",
                            "name": "Novi100_1",
                            "node": "urn:sdx:node:amlight.net:A1",
                            "type": "10GE",
                            "status": "up",
                            "state": "enabled"
                        },
                        {
                            "id": "urn:sdx:port:amlight.net:A1:2",
                            "name": "Novi100_2",
                            "node": "urn:sdx:node:amlight.net:A1",
                            "type": "10GE",
                            "status": "up",
                            "state": "enabled"
                        }
                    ],
                }
            ],
        }
