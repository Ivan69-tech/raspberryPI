from pyModbusTCP.server import ModbusServer


server = ModbusServer(host = "localhost", port = 502, no_block=True)
server.start()
while True :
  pass
