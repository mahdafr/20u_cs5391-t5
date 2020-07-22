#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.cli import CLI

class part1_topo(Topo):
    
    def build(self):
        switch1 = self.addSwitch('s1')
        for i in range(4):                           # add link to each host
            h = self.addHost('h' + str(i+1))
            self.addLink(h,switch1)

topos = {'part1' : part1_topo}

if __name__ == '__main__':
    t = part1_topo()
    net = Mininet (topo=t)
    net.start()
    CLI(net)
#    net.stop()
