from pyModbusTCP.server import ModbusServer, DataBank
from random import randint
import multiprocessing as mp
from pyModbusTCP.client import ModbusClient
import time

server = ModbusServer(host = "localhost", port = 502, no_block=True)
D = DataBank()

try :
  print("Start server")
  server.start()
  print("server is online")
  while True :
    D.set_holding_registers(40001,[randint(0,10)])
    print(D.get_holding_registers(40001))
    time.sleep(2)

  
except Exception as error :
  print(error)
  print("shutdown server")
  server.stop()
  print("server is offline")


