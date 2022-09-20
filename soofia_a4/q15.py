# 15. *Install and import suitable package and create QR Code in red color


# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
  
  
# String which represents the QR code
s = "www.geeksforgeeks.org"
  
# Generate QR code
url = pyqrcode.create(s)
  
# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8, background="white", module_color="#FF0000")
  
# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)