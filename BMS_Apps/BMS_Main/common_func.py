from PIL import Image
import base64
import random
import string
import os

# This function is used for save base64 image and create thumbnail 1300*13000
def base64ConvertArea(file_src, file_name, file_type, file_format):
    try:
        if file_format == 'img':
            imgdata = base64.b64decode(file_src)
            with open(f'static/image/{file_name}{file_type}', 'wb') as f:
                f.write(imgdata)
                image = Image.open(f'static/image/{file_name}{file_type}')
                if image.mode in ["RGBA", "P"]:
                    image = image.convert("RGB")
                image.thumbnail((1300, 1300))
                image.save(f'static/image/{file_name}{file_type}')
                width, height = image.size
                return f"static/image/{file_name}{file_type}", width, height
        else:
            mp3data = base64.b64decode(file_src)
            with open(f'static/audio/{file_name}{file_type}', 'wb') as f:
                f.write(mp3data)
            return f"static/audio/{file_name}{file_type}"

    except Exception as e:
        return None

# This function is used to generate 6 character random string 
def id_generator(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

# This function is used for remove given path images
def removeOldFile(on,off,file_type):
    try:
        if file_type=="img":
            on_img_path = on
            off_img_path = off
            on_img_name = os.path.basename(os.path.normpath(on_img_path))
            off_img_name = os.path.basename(os.path.normpath(off_img_path))
            on_fileStatus = os.path.isfile(f'static/image/{on_img_name}')
            off_fileStatus = os.path.isfile(f'static/image/{off_img_name}')
            if on_fileStatus == True:           
                os.remove(f'static/image/{on_img_name}')
            if off_fileStatus == True:
                os.remove(f'static/image/{off_img_name}')
        else:
            mp3path = on
            mp3_name = os.path.basename(os.path.normpath(mp3path))
            mp3_fileStatus = os.path.isfile(f'static/audio/{mp3_name}')
            if mp3_fileStatus == True:           
                os.remove(f'static/audio/{mp3_name}')
    except Exception:
        return None
