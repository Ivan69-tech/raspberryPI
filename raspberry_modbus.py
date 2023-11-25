from pyModbusTCP.server import ModbusServer


server = ModbusServer(host = "192.168.10.90", port = 502, no_block=True)
server.start()
while True :
  pass
