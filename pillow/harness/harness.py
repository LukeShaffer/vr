import os
import atheris_no_libfuzzer as atheris
import sys
import io
import warnings
from PIL import Image, ImageFile, ImageFilter


from util import image_formats


def TestOneInput(data):
	try:
		for im_format in image_formats:
			filename = os.path.join('images', 'fuzz_data.'+im_format)
			with open(filename, 'wb') as file:
				file.write(data)

			with Image.open(filename) as im:
				im.filter(ImageFilter.DETAIL)
				im.save(io.BytesIO(), im_format)

	except Exception:
		return


def main():
	ImageFile.LOAD_TRUNCATED_IMAGES = LOAD_TRUNCATED_IMAGES
	warnings.filterwarnings("ignore")
	atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
	atheris.Fuzz()

if __name__ == '__main__':
	main()