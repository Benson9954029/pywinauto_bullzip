from pywinauto.application import Application
import pywinauto
import time
app = Application().start(r"Setup_BullzipPDFPrinter_11_11_0_2804_PRO_EXP.exe")
time.sleep(1)
Properties = pywinauto.Desktop(backend='uia')['選擇安裝語言']
time.sleep(1)
Properties['確定'].click()
Properties = pywinauto.Desktop(backend='uia')['Bullzip PDF Printer 安裝程式']
#Properties.click()
Properties['我同意(A)RadioButton'].click()
Properties['下一步(N)'].click()
time.sleep(1)

