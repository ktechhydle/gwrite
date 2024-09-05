from setuptools import setup, find_packages

setup(
    name='gwrite',
    version='1.0',
    description='A simple way to interact with your 3d Printer using GCODE in Python',
    author='Keller Hydle',
    author_email='ktechindustries2019@gmail.com',
    packages=find_packages(),
    install_requires=['wheel', 'bar', 'greek', 'pyserial'], #external packages as dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["gwrite = src.gwrite:gwrite"]},
)
