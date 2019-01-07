import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="is_valid",
    version="0.0.1",
    author="Zane",
    author_email="zongzhen@yahoo.com",
    description="String validator for more",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zane-studio/is_valid",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
