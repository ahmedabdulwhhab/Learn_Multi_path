#sudo mn --custom ./fat_tree_topo.py --topo=mytopo --controller=remote,ip=127.0.0.1,port=6633

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class MyTopo(Topo):

    def __init__(self):
        super(MyTopo,self).__init__()

        k=4
        pod=k
        Layer_1 = (pod//2)**2
        Layer_2 = pod*pod//2
        Layer_3 = Layer_2

        L1= []
        L2 = []
        L3 = []

        for i in range(Layer_1):
            L1_sw = self.addSwitch('L1{}'.format(i+1))
            L1.append(L1_sw)

        for i in range(Layer_2):
            L2_sw = self.addSwitch('L2{}'.format(Layer_1+i + 1))
            L2.append(L2_sw)

        for i in range(Layer_3):
            L3_sw = self.addSwitch('L3{}'.format(Layer_1+Layer_2+i + 1))
            L3.append(L3_sw)

        for i in range(Layer_1):
            L1_sw=L1[i]
            start=i%(pod//2)
            for j in range(pod):
                self.addLink(L1_sw,L2[start+j*(pod//2)])

            for i in range(Layer_3):
                for j in range(2):
                    my_host = self.addHost('h{}'.format(i*2+j+1))
                    self.addLink(L3[i],my_host)
topos = {"mytopo":(lambda :MyTopo())}

#def main():
 #   setLogLevel( 'info' )
  #  topo = Topo1()
    
  #  net = Mininet(topo=topo, link=TCLink)
    
   # net.start()
    #CLI(net)
    #net.stop()
    
#if __name__ == '__main__':
  #  main()

