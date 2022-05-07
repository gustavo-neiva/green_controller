from setuptools import setup

setup(
    name="green_contrller",
    version="0.1.0",
    packages=["green_controller"],
    entry_points={
        "console_scripts": [
            "green_controller = green_controller.__main__:main"
        ]
    },
)
