from PIL import Image
import os


histogramdict = {}
	  

      
      
for i in range (1,1000):
        p1 = str(i)+".jpg"
        photo = "D:\imageprj\image.vary.jpg\%s"%(p1)
        if os.path.isfile(photo):
             spec_photo = Image.open(photo)
             histogramdict[photo] = spec_photo.histogram()
          
        else:
             continue
file = open ('histodict.txt','w')
file.write(str(histogramdict))
print ("HTTP/1.0 200 OK\n");
print ("Content-Type: text/html\n\n\n");