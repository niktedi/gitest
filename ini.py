import sys
import numpy
import os

for key in os.environ.keys():
    print(key +"=" + os.environ[key])
    