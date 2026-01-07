from PIL import Image, ImageFilter, ImageOps, ImageEnhance

def black_and_white_filter(img):
    return img.convert("L")

def sepia_filter(img):
    gray = ImageOps.grayscale(img)
    return ImageOps.colorize(
        gray,
        black="#704214",
        white="#C0A080",
    )

def cool_filter(img):
    r, g, b = img.split()
    b = ImageEnhance.Brightness(b).enhance(1.2)
    return Image.merge("RGB", (r,g,b))

def warm_filter(img):
    r, g, b = img.split()
    r = ImageEnhance.Brightness(r).enhance(1.2)
    return Image.merge("RGB", (r,g,b))

def saturated_filter(img):
    return ImageEnhance.Color(img).enhance(1.5)

def negative_filter(img):
    return ImageOps.invert(img.convert("RGB"))

def blur_filter(img):
    return img.filter(ImageFilter.BLUR)

FILTERS = {
    "bw": black_and_white_filter,
    "sepia": sepia_filter,
    "cool": cool_filter,
    "warm": warm_filter,
    "saturated": saturated_filter,
    "negative": negative_filter,
    "blur": blur_filter,
}