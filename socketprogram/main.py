import socket
print(type(socket))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname('prosenjit-das.herokuapp.com')
print(ip)
port = 80
address = (ip, port)
connect = client.connect(address)