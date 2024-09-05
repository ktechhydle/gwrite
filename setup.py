from setuptools import setup

setup(
    name='gwrite',
    version='1.0',
    description='A simple way to interact with your 3d Printer using GCODE in Python',
    author='Keller Hydle',
    author_email='ktechindustries2019@gmail.com',
    packages=['gwrite'],  #same as name
    install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
    scripts=['gwrite', 'tests']
)