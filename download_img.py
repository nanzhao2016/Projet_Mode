import urllib.request

"""
resource = urllib.request.urlopen("http://weneedfun.com/wp-content/uploads/2016/01/Pink-Flower-17.jpg")
output = open("C:/Users/OPEN/Documents/NanZHAO/Projet CIR Mode/file_test.jpg", "wb")
"""

resource = urllib.request.urlopen("https://cdn.pixabay.com/photo/2014/04/14/23/30/daisy-324403_960_720.jpg")
output = open("C:/Users/OPEN/Documents/NanZHAO/Projet CIR Mode/file_test3.jpg", "wb")
output.write(resource.read())
output.close()


