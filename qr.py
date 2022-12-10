#Author: Fernando Valenzuela
#Date created: 15.10.2022.22:14 UTC - 4
#Description: Create a script that generates QR codes from a list of books
import qrcode
##read from a file
file = open('Catalogo.txt', 'r')
##read line by line
##path for the QR codes
for line in file:
    ##print line
    print(line)
    ##create qrcode
    img = qrcode.make(line)
    ##save qrcode
    img.save(line+'.png')
    