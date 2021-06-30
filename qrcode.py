#Gerador de QRCode

import pyqrcode
import png

from pyqrcode import QRCode

QRstr = "......."  '''<----COLOQUE A URL AQUI'''

url = pyqrcode.create(QRstr)
url.png("..\qrcode.png",scale=8)