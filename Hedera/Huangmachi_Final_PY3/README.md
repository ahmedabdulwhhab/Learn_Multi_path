## Hedera
# Python 3 on ubuntu 20.04

Hedera is a SDN-based traffic schduling application implementating "Hedera", see the paper "Hedera: dynamic flow scheduling for data center networks" by Mohammad Al-Fares. Initially, network traffic is routed with ECMP. Once the speed of any flow in the switch exceeds 10% of the bandwidth of the link, routing path will be calculated and installed by the Ryu controller to reschedule the flow to other light loading path.
It includes a set of Ryu applications collecting basic network information, such as topology and free bandwidth of links. Fortunately, our application supports load balancing based on dynamic traffic information.

The detailed information of the modules is shown below:

* Fattree4 and Fattree8 are topology modules;

* Network Awareness is the module for collecting network information;

* Network Monitor is the module for collecting traffic information;

* DemandEstimation is the module for estimating flow demand;

* Hedera is the main module of the application;

* Setting is the module including common setting.

We make use of networkx's data structure to store topology. Meanwhile, we also utilize networkx's built-in algorithm to calculate shortest paths.


### Prerequisites

The following softwares should have been installed in your machine.
* Mininet: git clone git://github.com/mininet/mininet; mininet/util/install.sh -a
* Ryu: git clone git://github.com/osrg/ryu.git; cd ryu; pip install .
* Networkx: pip install networkx


### Download

Download files into Ryu directory, for instance, 'ryu/ryu/app/Hedera' is OK.


### Make some change

To register parsing parameters, you NEED to add the following code into the end of ryu/ryu/flags.py.

    CONF.register_cli_opts([
        # k_shortest_forwarding
        cfg.IntOpt('k_paths', default=4, help='number of candidate paths of KSP.'),
        cfg.StrOpt('weight', default='bw', help='weight type of computing shortest path.'),
        cfg.IntOpt('fanout', default=4, help='switch fanout number.')])


### Reinstall Ryu

You must reinstall Ryu, so that you can run the new code. In the top directory of Ryu project:

    sudo python3 setup.py install


### Start

Note: Before doing the experiment, you should change the controller's IP address from '192.168.56.101' to your own machine's eth0 IP address in the fattree.py module in each application, because '192.168.56.101' is my computer's eth0 IP address (Try 'ifconfig' in your Ubuntu to find out the eth0's IP address). Otherwise, the switches can't connect to the controller.

Firstly, start up the network. An example is shown below:
	$ sudo git clone https://github.com/ahmedabdulwhhab/Learn_Multi_path
	https://github.com/ahmedabdulwhhab/Learn_Multi_path/tree/main/Hedera/Huangmachi_Final_PY3
	$ cd Learn_Multi_path/Hedera/Huangmachi_Final_PY3
    $ sudo mn -c && sudo python3 fattree4.py

And then, go into the top directory of Ryu, and run the application. You are suggested to add arguments when starting Ryu. An example is shown below:

    $ cd ryu
    $ sudo ryu-manager Hedera.py    /home/ubuntu/sdn/sources/flowmanager/flowmanager.py  --k_paths=4 --weight=hop --fanout=4 --observe-links --ofp-tcp-listen-port 6633

or:

    $ sudo ryu-manager Hedera.py    /home/ubuntu/sdn/sources/flowmanager/flowmanager.py  --k_paths=16 --weight=hop --fanout=8 --observe-links --ofp-tcp-listen-port 6633

NOTE: After these, we should wait for the network to complete the initiation for several seconds, because LLDP needs some time to discovery the network topology. We can't operate the network until 'Get network topology' is printed in the terminal of the Ryu controller, otherwise, some error will occur. It may be about 10 seconds for fattree4, and a little longer for fattree8.

After that, test the correctness of Hedera:

    mininet> pingall
    mininet> iperf

If you want to show the collected information, you can set the parameters in setting.py. Also, you can change the setting as you like, such as the discovery period and monitor period. After that, you can see the information shown in the terminal.


### Authors

Brought to you by Huang MaChi (Chongqing University of Posts and Telecommunications, Chongqing, China.) and Li Cheng (Beijing University of Posts and Telecommunications. www.muzixing.com).

If you have any question, email me at huangmachi@foxmail.com. Don't forget to STAR this repository!

Enjoy it!
