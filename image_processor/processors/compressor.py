import io
from PIL import Image

FORMAT_COMPRESS_CONFIG = {
    "JPEG": {
        "quality": 75,
        "optimize": True,
        "progressive": True,
    },
    "PNG" : {
        "optimize": True,
        "compress_level": 9,
    },

    "WEBP": {
        "quality": 75,
        "method": 6,
    }
}

def compress_img(image: Image.Image):

    img = Image.open(image)
    input_format = img.format

    if input_format is None:
        raise ValueError("The format image could not be detected.")

    config = FORMAT_COMPRESS_CONFIG.get(input_format)
    if not config:
        raise ValueError("Unsupported compression format.")
    

    if input_format == "JPEG":
        img = img.convert('RGB')

    buffer = io.BytesIO()
    img.save(buffer, format=input_format, **config)
    buffer.seek(0)

    return buffer
