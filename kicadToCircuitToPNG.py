# coding: utf-8
import requests
import re
import zipfile
import shutil

archivo = "/home/saran/Documentos/electronica/kicad/freeleds-planos/gerbers/gerbers.zip"

s = requests.Session()
s.get('https://circuitpeople.com')
files = {"FileUpload1": open(archivo,'rb')}
r1 = s.post("https://circuitpeople.com/UploadHandler.ashx",files=files)
zip=zipfile.ZipFile(archivo)
nombres = [i.orig_filename for i in zip.filelist]
for nombre in nombres:
    payload = {"name":nombre,"dpi":"600"}
    r = s.get("https://circuitpeople.com/UploadImage.ashx",params=payload)
    print(r.url)
    with open(nombre+".png", 'wb') as f:
        r.raw.decode_content = True
        for chunk in r.iter_content():
            f.write(chunk)
        f.close()
    r.close()
s.close()

