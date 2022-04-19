import server.serverInfo

serverInfo = server.serverInfo.ServerInfo()
serverInfo.product = "myProduct"
serverInfo.subProduct = "sub"
serverInfo.ip = "192.168.1.1"

serverInfo2 = server.serverInfo.ServerInfo()
serverInfo2.product = "product2"

print(serverInfo.product)
print(serverInfo2.product)

