
import os
from PIL import Image

# Directorio de las fotos
directory = "./photos"
directory_new = f"{directory}_fixed"

# Crea el directorio donde se guardaran las fotos , si no existe 
try: 
    if not os.path.exists(directory_new):
        os.mkdir(directory_new)
except Exception as e:
    print(f"Error al crear el directorio: {e}")

# Listando las fotos  en el directorio
photos=os.listdir(directory)

for photo in photos:
    try:
        # Separando y guardando el nombre y la extensión de cada foto
        photo_name,photo_extension = os.path.splitext(photo)
        # crear un objeto imagen 
        photo = Image.open(f"./{directory}/{photo}")
        # rotando la foto
        photo.rotate(-90)
        # redimensionando
        size = (1200,900) # tamaño de prueba
        photo.thumbnail(size)
        # Guardar la imagen con el cambio de extensión 
        photo.save(f"{directory_new}/{photo_name}.png")
    except Exception as e:
        print(f"Error al procesar la imagen {e}")

    # Fuentes: 
    # https://www.toolify.ai/es/ai-news-es/manipulacin-de-imgenes-en-python-con-pillow-1149800#:~:text=Una%20vez%20que%20tenemos%20las,"from%20PIL%20import%20Image".
    # https://www.freecodecamp.org/espanol/news/como-crear-un-directorio-con-python/