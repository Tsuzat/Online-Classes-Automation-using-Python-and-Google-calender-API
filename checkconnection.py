import socket

def is_connected(hostname = "one.one.one.one"):
    try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname(hostname)
        # connect to the host -- tells us if the host is actually
        # reachable
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    
    except:
        pass
    
    return False

if __name__ == "__main":
    is_connected()