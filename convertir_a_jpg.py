# 🔧 Script para convertir imágenes a formato JPG válido desde /img
# Debe colocarse en el mismo directorio raíz donde está la carpeta img/

from PIL import Image
import os

# Ruta de la carpeta con las imágenes
folder = "img"

# Recorre todos los archivos de la carpeta img/
for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    try:
        # Intenta abrir la imagen
        with Image.open(filepath) as im:
            rgb_im = im.convert("RGB")
            new_name = os.path.splitext(filename)[0] + ".jpg"
            new_path = os.path.join(folder, new_name)
            rgb_im.save(new_path, "JPEG")
            print(f"✅ Convertido: {filename} → {new_name}")
            if not filename.endswith(".jpg"):
                os.remove(filepath)
                print(f"🗑️ Borrado original: {filename}")
    except Exception as e:
        print(f"❌ Error al convertir {filename}: {e}")

print("\n✔️ Todas las imágenes procesadas.")
