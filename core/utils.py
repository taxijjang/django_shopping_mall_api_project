import os
from uuid import uuid4


def rename_image_file_to_uuid(instance, filename):
    upload_to = f'media/{instance.__class__.__name__}'
    ext = filename.split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return os.path.join(upload_to, filename)
