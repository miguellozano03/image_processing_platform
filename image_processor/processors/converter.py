from PIL import Image
import io

CONVERT_OPTIONS = {
    "jpeg": "JPEG",
    "png":"PNG",
    "webp": "WEBP",
    "bmp": "BMP",
    "tiff": "TIFF"
}

def convert_img(image: Image.Image, output_key: str):
    output_format = CONVERT_OPTIONS.get(output_key.lower())

    if not output_format:
        raise ValueError("Format not supported")

    img = Image.open(image)

    if output_format == CONVERT_OPTIONS["jpeg"]:
        img = img.convert("RGB")

    buffer = io.BytesIO()
    img.save(buffer, format=output_format)
    buffer.seek(0)

    return buffer