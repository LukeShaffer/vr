from util import image_formats


def TestOneInput(data):
	try:
		with Image.open(io.BytesIO(data)) as im:
			for im_format in image_formats:
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