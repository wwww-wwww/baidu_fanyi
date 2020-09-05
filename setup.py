import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="baidu_fanyi",
  version="0.0.3",
  author="wwwwwwww",
  author_email="wvvwvvvvwvvw@gmail.com",
  description="Baidu translation API",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/wwww-wwww/baidu_fanyi",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)
