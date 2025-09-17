from ipaddress import *
def task13_23559_1(): #718
    network = ip_network('102.162.200.51/255.255.255.0',0)
    for i in network:
        print(i)
        print('--')

def task13_19245_2(): #218.194.82.190 -> 21819482190
    network = ip_network('218.194.82.148/255.255.255.192',0)
    for i in network:
        print(i)
task13_19245_2()