import os 
import pathlib
import unittest

# from selenium import webdriver - probably have to pip this

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# driver = webdriver.Chrome() - google how/where to get this

class WebpageTests(unittest.TestCase):
    # Will contain a bunch of test cases to check for functionailty in the browser
    # will not work as i dont have selenium or webdriver rn
    pass

