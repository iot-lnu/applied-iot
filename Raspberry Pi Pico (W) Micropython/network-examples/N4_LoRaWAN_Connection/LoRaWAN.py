import time
import binascii
from machine import UART

# https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/lorawan/ASR650X%20AT%20Command%20Introduction-20190605.pdf

class lora:

  def __init__(self, debug=False):
    self._serial = UART(0, 115200)  # use RPI PICO GP0 and GP1
    self.debug = debug
    self.init()

  def Init(self, serial, RX, TX):
    self._serial = serial
    self._serial.begin(115200, serial.SERIAL_8N1, RX, TX)
    self._serial.flush()

  def checkDeviceConnect(self):
    restr = ""
    self.writeCMD("AT+CGMI?\r\n")
    restr = self.getResponse()
    if "OK" not in restr:
      return False
    else:
      return True

  def checkJoinStatus(self):
    restr = ""
    self.writeCMD("AT+CSTATUS?\r\n")
    restr = self.getResponse()
    if restr.find("+CSTATUS:") != -1:
      if restr.find("08") != -1: # or restr.find("07") != -1 or restr.find("08") != -1:
        return True
      else:
        return False
    else:
      return False

  def waitMsg(self, t):
    restr = ""
    start = round(time.time() * 1000)
    while True:
      if (round(time.time() * 1000) - start) < t:
        res = self._serial.readline()
        if res:
          if len(res) > 0:
            restr += str(res)
      else:
        break
    return restr

  def writeCMD(self, command):
    self._serial.write(command)
    time.sleep(0.1)

  def sendMsg(self, data, confirm=1, nbtrials=1):

    cmd = f"AT+DTRX={confirm},{nbtrials},{len(data)},{data}\r\n"
    if self.debug:
      print("SENT", cmd)
    self.writeCMD(cmd)
    self.getResponse()

  def setSpreadingFactor(self, sf):

    cmd = f"AT+CDATARATE={sf}\r\n"
    self.writeCMD(cmd)
    self.getResponse()

  def receiveMsg(self):
    restr = self.getResponse()
    if restr.find("OK+RECV:") != -1 and restr.find("02,00,00") == -1:
      data = restr[restr.find("OK+RECV:") + 17:-2]
      return self.decodeMsg(data)
    else:
      return ""

  def configOTTA(self, device_eui, app_eui, app_key, ul_dl_mode):
    self.writeCMD("AT+CJOINMODE=0\r\n")
    self.getResponse()
    self.writeCMD("AT+CDEVEUI=" + device_eui + "\r\n")
    self.getResponse()
    self.writeCMD("AT+CAPPEUI=" + app_eui + "\r\n")
    self.getResponse()
    self.writeCMD("AT+CAPPKEY=" + app_key + "\r\n")
    self.getResponse()
    self.writeCMD("AT+CULDLMODE=" + ul_dl_mode + "\r\n")
    self.getResponse()

  def configABP(self, device_addr, app_skey, net_skey, ul_dl_mode):
    self.writeCMD("AT+CJOINMODE=1\r\n")
    self.getResponse()
    self.writeCMD("AT+CDEVADDR=" + device_addr + "\r\n")
    self.getResponse()
    self.writeCMD("AT+CAPPSKEY=" + app_skey + "\r\n")
    self.getResponse()
    self.writeCMD("AT+CNWKSKEY=" + net_skey + "\r\n")
    self.getResponse()
    self.writeCMD("AT+CULDLMODE=" + ul_dl_mode + "\r\n")
    self.getResponse()

  def setClass(self, mode):
    self.writeCMD("AT+CCLASS=" + mode + "\r\n")

  def setRxWindow(self, freq):
    self.writeCMD("AT+CRXP=0,0," + freq + "\r\n")

  def setFreqMask(self, mask):
    self.writeCMD("AT+CFREQBANDMASK=" + mask + "\r\n")

  def startJoin(self):
    self.writeCMD("AT+CJOIN=1,0,10,8\r\n")

  def decodeMsg(self, hexEncoded):
    if len(hexEncoded) % 2 == 0:
      buf = hexEncoded
      tempbuf = [None] * len(hexEncoded)
      i = 0
      loop = 2
      while loop < len(hexEncoded) + 1:
        tmpstr = buf[loop - 2:loop]
        tempbuf[i] = chr(int(tmpstr, 16))
        i += 1
        loop += 2
      return "".join(tempbuf)
    else:
      return hexEncoded

  def getResponse(self):

    time.sleep(0.05)
    restr = self.waitMsg(200)
    if self.debug:
      print(restr)

    return restr

  def init(self):
    while not self.checkDeviceConnect():
      pass
    if self.debug:
      print("Module Connected")

    self.writeCMD("AT+CRESTORE\r\n")

    # Disable Log Information
    self.writeCMD("AT+ILOGLVL=1\r\n")

    self.writeCMD("AT+CSAVE\r\n")

    self.writeCMD("AT+IREBOOT=0\r\n")

    time.sleep(1)

    while not self.checkDeviceConnect():
      pass

  def configure(self, devui, appeui, appkey):
    print("Module Config...")
    self.configOTTA(devui,  # Device EUI
                    appeui,  # APP EUI
                    appkey,  # APP KEY
                    "2"  # Upload Download Mode
                    )

    # Set Class Mode
    self.setClass("2")
    self.writeCMD("AT+CWORKMODE=2\r\n")

    self.setSpreadingFactor("5")

    # LoRaWAN868
    self.setRxWindow("869525000")

    self.setFreqMask("0001")
