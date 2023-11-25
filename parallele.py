import multiprocessing as mp
import time
from pyModbusTCP.client import ModbusClient


class BMS :

  def __init__(self, Port) :
    self.c = ModbusClient(host="localhost", port=Port, unit_id=1,auto_open=True)
    if self.c.open():
      print("succeed to connect to BMS")
    else :
      print("failed to connect to BMS")
    return

  def Watchdog(self) :
    w = 0
    while True :
      if self.c.write_single_register(44000, w) :
        print("write watchdog %s to BMS" % (w))
      else :
        print("fail to write watchdog %s to BMS" % (w))
      w += 1
      time.sleep(1)
      if w == 100 :
        w = 0

        
  def StartBMS(self) :
    if self.c.write_single_register(44002, 1) :
      print("Start BMS command succeed")
    else :
      print("fail to start BMS")
  
  def RackPrecharge(self) :
    if self.c.write_single_register(44002, 2) :
      print("Precharge command succeed")
    else :
      print("fail to send precharge command")

# if __name__ == "__main__" :
#   B = BMS(10002)
#   B.StartBMS()
#   time.sleep(4)
#   p = mp.Process(target = B.Watchdog)
#   p.start()
#   time.sleep(4)
#   B.RackPrecharge()