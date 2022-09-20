# 16. *Install and import suitable package and create barcode in blue color
from barcode import EAN13

number = '738947829267'

mycode = EAN13(number)

mycode.save("mycode2")