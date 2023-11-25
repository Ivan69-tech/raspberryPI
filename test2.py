#!/bin/python

from pyModbusTCP.server import ModbusServer
from pyModbusTCP.client import ModbusClient
import time
from random import randint
import multiprocessing as mp

def StartServer(Port):
        server = ModbusServer(host = "localhost", port = Port, no_block=True)
        server.start()
        while True :
            pass

def WriteData(Port):
    c = ModbusClient(host="localhost", port=Port, unit_id=1,auto_open=True)
    while True :
        a = randint(0,10)
        c.write_single_register(1, a)
        print(f"Ecriture de {a} sur le registre 1")
        time.sleep(2)
       
def ReadData(Port):
    c = ModbusClient(host="localhost", port=Port, unit_id=1,auto_open=True)
    while True :
       print(c.read_holding_registers(1))
       time.sleep(2)

if __name__ == "__main__" :
  p = mp.Process(target = StartServer, args=(502,))
  p.start()
  p1 = mp.Process(target = WriteData, args=(502,))
  p1.start()
  p2 = mp.Process(target = ReadData, args=(502,))
  p2.start()
 