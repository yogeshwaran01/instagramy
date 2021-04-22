import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="instagramy",
    version="4.4",
    license='MIT',
    author="Yogeshwaran R",
    author_email="yogeshin247@gmail.com",
    description="Python Package for Instagram User, Posts, Hashtags and Locations data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yogeshwaran01/instagramy/",
    packages=setuptools.find_packages(),
    download_url="https://github.com/yogeshwaran01/instagramy/archive/master.zip",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
