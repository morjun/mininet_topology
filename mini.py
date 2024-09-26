from mininet.net import Mininet
from mininet.node import Controller, OVSController
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.cli import CLI

def myNetwork():
    net = Mininet(controller=OVSController, link=TCLink)
    
    # 컨트롤러 추가
    net.addController('c0')
    
    # 호스트 추가
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')
    
    # 스위치 추가
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    # 링크 추가 (여기서 대역폭이나 지연 시간 설정 가능)
    net.addLink(h1, s1, bw=10, delay='5ms')
    net.addLink(h2, s2, bw=10, delay='5ms')
    net.addLink(s1, s2, bw=5, delay='10ms')

    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
