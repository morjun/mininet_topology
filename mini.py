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
    h1 = net.addHost('h1', ip='10.0.1.2')
    h2 = net.addHost('h2', ip='10.0.2.2')
    
    # 스위치 추가
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    # 링크 추가 (여기서 대역폭이나 지연 시간 설정 가능)
    net.addLink(h1, s1, bw=17, delay='17ms', loss=4, intfName1='h1-eth0')
    net.addLink(h1, s2, bw=17, delay='100ms', loss = 1, intfName1='h1-eth1')
    net.addLink(h2, s2, bw=17, delay='100ms', loss = 1, intfName1='h2-eth0')
    net.addLink(h2, s1, bw=17, delay='17ms', loss = 4, intfName1='h2-eth1')

    # net.addLink(s1, s2, bw=5, delay='10ms')

    net.start()

    # 각 호스트에서 인터페이스 설정
    # h1에서 h1-eth1에 대한 추가 IP 할당
    h1.cmd('ifconfig h1-eth1 10.0.3.2 netmask 255.255.255.0')

    # h2에서 h2-eth1에 대한 추가 IP 할당
    h2.cmd('ifconfig h2-eth1 10.0.4.2 netmask 255.255.255.0')

    # h1에서 h2로 패킷을 보낼 때 어느 인터페이스를 사용할지 선택
    h1.cmd('ip route add 10.0.2.0/24 dev h1-eth0')  # s1을 통해서 h2에 패킷 전송
    # h1.cmd('ip route add 10.0.2.0/24 dev h1-eth1')  # s2를 통해서 h2에 패킷 전송 (이 줄을 선택하면 s2 사용)

    # h2에서 h1로 패킷을 보낼 때 어느 인터페이스를 사용할지 선택
    h2.cmd('ip route add 10.0.1.0/24 dev h2-eth0')  # s1을 통해서 h1에 패킷 전송
    # h2.cmd('ip route add 10.0.1.0/24 dev h2-eth1')  # s2를 통해서 h1에 패킷 전송 (이 줄을 선택하면 s2 사용)

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
