from distutils.core import setup
import py2exe

# Run 'python setup.py py2exe' with setup.py and food.py in the same directory
setup(console=['food.py'])