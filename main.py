"""
Author: github.com/Ariocodes
This code turns any link or text into a QR Code
"""

import qrcode
img = qrcode.make('LINK OR TEXT')
img.save("FILENAME.png")
img.show()
