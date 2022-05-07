from setuptools import setup

setup(
    name="green_controler",
    version="0.1.0",
    packages=["my_project"],
    entry_points={
        "console_scripts": [
            "my_project = my_project.__main__:main"
        ]
    },
)