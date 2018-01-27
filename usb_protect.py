import os,getpass,time,win32con 
from win32api import GetLogicalDriveStrings
from win32file import GetDriveType
import winsound
import datetime

def sound():
        for i in range(1,40):
                winsound.Beep(1000,1000)
                
def takephoto():
        import cv2 
        user_name=getpass.getuser()
        x=time.time()
        x=str(x)
        #x.replace(" ","")
        p2="{}.jpg".format(x)
        print p2
        camera = cv2.VideoCapture(0)
        time.sleep(1)
        return_value,image = camera.read()
        cv2.imwrite(p2,image)
        camera.release()
        cv2.destroyAllWindows()

time.sleep(1)
while True:
   try:
      drive_types=(win32con.DRIVE_REMOVABLE,)
      ret = list()
      drives_str = GetLogicalDriveStrings()
      drives = [item for item in drives_str.split("\x00") if item]
      for drive in drives:
         if GetDriveType(drive) in drive_types:
            ret.append(drive)
      
      item1=ret[0]
   except:
       time.sleep(3)
       continue
   if os.path.exists(item1):
           takephoto()
           break;
sound()      
                  
