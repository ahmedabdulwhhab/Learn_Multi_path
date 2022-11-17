#!/usr/bin/env python
#multi controller
#clear && ryu-manager ./sdn/ryu-controller/muzixing/ryu/ryu/app/multipath.py  --observe-links --verbose --ofp-tcp-listen-port 6633
#clear && ryu-manager ./sdn/ryu-controller/ah_learn_ryu_00/ryu_multipath.py --observe-links --ofp-tcp-listen-port 6633

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.term import makeTerm

if '__main__' == __name__:
    net = Mininet(controller=RemoteController)

    c0 = net.addController('c0', port=6633)


    sc1 = net.addSwitch('sc1')
    sc2 = net.addSwitch('sc2')
    sc3 = net.addSwitch('sc3')
    sc4 = net.addSwitch('sc4')
    
    
    sp11 = net.addSwitch('sp11')
    sp12 = net.addSwitch('sp12')
    sp13 = net.addSwitch('sp13')
    sp14 = net.addSwitch('sp14')
    
    sp21 = net.addSwitch('sp21')
    sp22 = net.addSwitch('sp22')
    sp23 = net.addSwitch('sp23')
    sp24 = net.addSwitch('sp24')
    
    sp31 = net.addSwitch('sp31')
    sp32 = net.addSwitch('sp32')
    sp33 = net.addSwitch('sp33')
    sp34 = net.addSwitch('sp34')
    
    sp41 = net.addSwitch('sp41')
    sp42 = net.addSwitch('sp42')
    sp43 = net.addSwitch('sp43')
    sp44 = net.addSwitch('sp44')

    h1 = net.addHost('h1',mac='00:00:01:00:00:00')
    h2 = net.addHost('h2',mac='00:00:02:00:00:00')
    h3 = net.addHost('h3',mac='00:00:03:00:00:00')
    h4 = net.addHost('h4',mac='00:00:04:00:00:00')

    h5 = net.addHost('h5',mac='00:00:11:00:00:00')
    h6 = net.addHost('h6',mac='00:00:12:00:00:00')
    h7 = net.addHost('h7',mac='00:00:13:00:00:00')
    h8 = net.addHost('h8',mac='00:00:14:00:00:00')
    h9 = net.addHost('h9',mac='00:00:15:00:00:00')
    
    
    h10 = net.addHost('h10',mac='00:00:17:00:00:00')
    h11 = net.addHost('h11',mac='00:00:18:00:00:00')
    h12 = net.addHost('h12',mac='00:00:19:00:00:00')
    h13 = net.addHost('h13',mac='00:00:20:00:00:00')
    h14 = net.addHost('h14',mac='00:00:21:00:00:00')
    h15 = net.addHost('h15',mac='00:00:22:00:00:00')
    h16 = net.addHost('h16',mac='00:00:23:00:00:00')


    net.addLink(sc1, sp11)
    net.addLink(sc1, sp21)
    net.addLink(sc1, sp31)
    net.addLink(sc1, sp41)

    net.addLink(sc2, sp11)
    net.addLink(sc2, sp21)
    net.addLink(sc2, sp31)
    net.addLink(sc2, sp41)  

    net.addLink(sc3, sp12)
    net.addLink(sc3, sp22)
    net.addLink(sc3, sp32)
    net.addLink(sc3, sp42)

    net.addLink(sc4, sp12)
    net.addLink(sc4, sp22)
    net.addLink(sc4, sp32)
    net.addLink(sc4, sp42)

    
    net.addLink(sp11, sp13)      
    net.addLink(sp11, sp14)

    net.addLink(sp12, sp13)      
    net.addLink(sp12, sp14)    
    
    net.addLink(sp21, sp23)      
    net.addLink(sp21, sp24)

    net.addLink(sp22, sp23)      
    net.addLink(sp22, sp24)    

    net.addLink(sp31, sp33)      
    net.addLink(sp31, sp34)

    net.addLink(sp32, sp33)      
    net.addLink(sp32, sp34)    
    
    net.addLink(sp41, sp43)      
    net.addLink(sp41, sp44)
                  
    net.addLink(sp42, sp43)      
    net.addLink(sp42, sp44)

    
    net.addLink(h1, sp13)  
    net.addLink(h2, sp13)  

    net.addLink(h3, sp14)  
    net.addLink(h4, sp14)  

    net.addLink(h5, sp23)  
    net.addLink(h6, sp23)  

    net.addLink(h7, sp24)  
    net.addLink(h8, sp24) 
    
    net.addLink(h9, sp33)    
    net.addLink(h10, sp33) 
    
    net.addLink(h11, sp34)    
    net.addLink(h12, sp34) 
    
    net.addLink(h13, sp43)     
    net.addLink(h14, sp43) 
    
    net.addLink(h15, sp44)  
    net.addLink(h16, sp44)  

    net.build()
    c0.start()
    sc1.start([c0])
    sc2.start([c0])
    sc3.start([c0])
    sc4.start([c0])
    sp11.start([c0])
    sp12.start([c0])
    sp13.start([c0])
    sp14.start([c0])
    sp21.start([c0])
    sp22.start([c0])
    sp23.start([c0])
    sp24.start([c0])
    sp31.start([c0])
    sp32.start([c0])
    sp33.start([c0])
    sp34.start([c0])
    sp41.start([c0])
    sp42.start([c0])
    sp43.start([c0])
    sp44.start([c0])


    #net.startTerms()

    CLI(net)

    net.stop()
