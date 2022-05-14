from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="green_controller",
    version='0.1.0',
    description='Greenhouse brain',
    long_description=readme,
    author='Gustavo Neiva',
    author_email='gustavo@neiva.dev',
    url='https://github.com/gustavo-neiva/green_controller',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

setup(
    version="0.1.0",
    packages=["green_controller"],
    entry_points={
        "console_scripts": [
            "green_controller_ctl = green_controller.__main__:main"
        ]
    },
)