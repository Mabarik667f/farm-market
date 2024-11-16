from io import BytesIO
from PIL import Image

def create_img(filename: str = "dummy", file_type: str = "png") -> BytesIO:
    image_data = BytesIO()
    image = Image.new("RGB", (100, 100), 0)
    image.save(image_data, format=file_type)
    image_data.name = f"{filename}.{file_type}"
    image_data.seek(0)
    return image_data
