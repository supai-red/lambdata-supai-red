"""
lambdata-supai-red
A collection of data science helper tools.
"""

import setuptools

REQUIRED = [
  "numpy",
  "pandas"
]

with open("README.md", "r") as fh:
  LONG_DESCRIPTION = fh.read()

setuptools.setup(
  name="supai-red",
  version="0.0.1"
  author="supai-red",
  description="A collection of data science helper functions.",
  long_description=LONG_DESCRIPTION,
  long_description_content_type="text/markdown",
  url="https://github.com/supai-red/lambdata-supai-red",
  packages=setuptools.find_packages(),
  python_requires">=3.5",
  install_required=REQUIRED,
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: oSI Approved :: MIT License",
    "Operating System :: OS Independent",

  ],

)
