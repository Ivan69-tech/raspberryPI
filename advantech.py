from pyModbusTCP.client import ModbusClient
import time

c = ModbusClient(host="192.168.10.1", port=502, unit_id=1,auto_open=True)

#c = ModbusClient(host="localhost", port=9700, unit_id=1,auto_open=True)


print(c.open())

def decimalToBinary(n): 
  return bin(n).replace("0b", "") 


while True :
  PA = c.read_input_registers(0x2102)  # CN1 PB
  BinPA = decimalToBinary(PA[0])
  print(f"{PA} Binary : {BinPA}")
  time.sleep(3)
   

# PB = c.read_holding_registers(0x2101)  # CN1 PB
# PC = c.read_holding_registers(0x2102)  # CN1 PC

# print(f"{0x4f:0>8b}")