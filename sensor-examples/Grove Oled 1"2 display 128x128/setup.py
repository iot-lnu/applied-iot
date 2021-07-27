import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)
from setuptools import setup

setup(
    name='micropython-ssd1327',
    py_modules=['ssd1327'],
    version='1.1.1',
    description='MicroPython library for SSD1327 based OLED displays.',
    long_description='This library lets you update SSD1327 based 128x128 4-bit grayscale OLED displays.',
    keywords='ssd1327 oled micropython',
    url='https://github.com/mcauser/micropython-ssd1327',
    author='Mike Causer',
    author_email='mcauser@gmail.com',
    maintainer='Mike Causer',
    maintainer_email='mcauser@gmail.com',
    license='MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: Implementation :: MicroPython',
        'License :: OSI Approved :: MIT License',
    ],
)