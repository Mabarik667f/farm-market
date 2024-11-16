import logging
from pathlib import Path
from ninja import UploadedFile
from django.utils import timezone

from product.models import Product

logger = logging.getLogger("cons")

class UploadMediaFile:

    def __init__(self, file: UploadedFile) -> None:
        self.file = file

    @staticmethod
    def clean_dir(path: Path):
        for f in path.glob("*"):
            if f.is_file():
                f.unlink

    @staticmethod
    def get_default_file_name():
        return timezone.now().strftime("%Y-%m-%d %H:%M:%S")

    def write_product_img(self, product: Product) -> None:
        upload_path = Path(product.get_upload_path())
        if upload_path.is_dir():
            self.clean_dir(upload_path)
        file_path = self.write_file(product, upload_path)
        setattr(product, "img", file_path)

    def write_file(self, product: Product, upload_path: Path) -> str:
        upload_path.mkdir(exist_ok=True)
        if not self.file.name:
            self.file.name = self.get_default_file_name()
        file_path = f"{str(upload_path)}/{self.file.name}"
        with open(file_path, "wb") as buf:
            buf.write(self.file.read())
        return file_path
