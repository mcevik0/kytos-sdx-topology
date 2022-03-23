#!/usr/bin/python
"""

Changing to use two controller for the SDX environment

SAX will be one switch and it will have its own controller
TENET will be one switch and it will have its own controller
AmLight will have multiple switches and it will have its own controller

Custom topology for AmLight/AMPATH
@author: Italo Valcy <italo@amlight.net>
@author: Renata Frez <renata.frez@rnp.br>

"""
import sys
import mininet.clean as Cleanup
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.node import OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel


def custom_topo(amlight_ctlr, sax_ctlr, tenet_ctlr):
    """ Create AmLight network for tests """
    # net = Mininet(topo=None, build=False)
    net = Mininet(topo=None, build=False, controller=RemoteController, switch=OVSSwitch)

    # ********************************************** TENET OXP - Start ************************************************
    TenetController = net.addController('tenet_ctrl', controller=RemoteController, ip=tenet_ctlr, port=6653)
    TenetController.start()
    # ************************************************ TENET OXP - End ************************************************

    # ************************************************ SAX OXP - Start ************************************************
    SaxController = net.addController('sax_ctrl', controller=RemoteController, ip=sax_ctlr, port=6653)
    SaxController.start()
    # ************************************************ SAX OXP - End ************************************************

    # ******************************************** AmLight OXP - Start **********************************************
    AmLightController = net.addController('amlight_ctrl', controller=RemoteController, ip=amlight_ctlr, port=6653)
    AmLightController.start()
    # ********************************************* AmLight OXP - End ************************************************
    net.build()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')  # for CLI output
    #amlight_ctlr = sys.argv[1] if len(sys.argv) > 1 else '172.31.13.114'
    amlight_ctlr = sys.argv[1] if len(sys.argv) > 1 else '3.218.56.104'
    #sax_ctlr = sys.argv[2] if len(sys.argv) > 2 else '172.31.6.170'
    sax_ctlr = sys.argv[2] if len(sys.argv) > 2 else '3.219.254.70'
    #tenet_ctlr = sys.argv[3] if len(sys.argv) > 3 else '172.31.14.86'
    tenet_ctlr = sys.argv[3] if len(sys.argv) > 3 else '23.20.21.212'
    custom_topo(amlight_ctlr, sax_ctlr, tenet_ctlr)
    Cleanup.cleanup()
