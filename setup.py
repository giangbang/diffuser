from setuptools import setup, find_packages

setup(
  name = 'diffuser',
  packages = find_packages(),
  install_requires=[
    "torch",
    "einops",
    "tap.py"
  ],
  # python_requires="<=3.8"
)
