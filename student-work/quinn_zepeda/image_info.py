import os
import sys
import json

import django
from django.conf import settings  # noqa Django magic starts here

import PIL.Image
from PIL.ExifTags import TAGS as tag_num2name


# `labeler_site` must be a python package installed in your environment (virtualenv)
# OR "install" it manually before running this: `export PYTHONPATH=$PYTHONPATH:/path/to/labeler_site_basedir/`

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'labeler_site.settings')
django.setup()


if __name__ == '__main__':
    if len(sys.args) > 1:
        image_path = ' '.join(sys.args[1:])
    else:
        os.path.join(settings.BASE_DIR, 'labeler', 'data', 'DSC_4621.jpg')
    img = PIL.Image.open(image_path)
    exif_data = img._getexif()
    print(exif_data)

    exif_data = dict(
        zip(
            map(tag_num2name.get, exif_data.keys()),
            exif_data.values()
        )
    )
    print(json.dumps(exif_data, indent=2))
    

