import setuptools

with open("README.md") as fh:
	long_description = fh.read()

packs = setuptools.find_packages()

setuptools.setup(
	name="pyzeron",
	version="1.0.0.dev3",
	author="OmarShadowSpike",
	author_email="omarwt92@gmail.com",
	description="A 2D Game engine library",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/OmarShadowSpike/pyzeron",
	packages=packs,
	install_requires=[
		"pygame",
		"keyboard",
	],
	keywords="pyzeron",
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
