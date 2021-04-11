import cv2
import pyzbar.pyzbar as pyzbar
import time


def zbar(img):
  t1 = time.time()
  decodedObjects = pyzbar.decode(img)
  print("{:.4f}".format(time.time()-t1))
  print(decodedObjects if len(decodedObjects[0].data) > 0 else "NO Qrcode found")

def opencv(img):
  qrDecoder = cv2.QRCodeDetector()
  t1 = time.time()
  data,bbox,rectifiedImage = qrDecoder.detectAndDecode(img)
  print("Time taken : {:.4f}".format(time.time()-t1))
  print(data if len(data)>0 else "NO Qrcode found")

img = cv2.imread("image/test1.jpg")

print("For Zbar : ")
zbar(img)
print()
print("---")
print()
print("For Opencv : ")
opencv(img)
