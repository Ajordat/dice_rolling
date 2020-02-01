from setuptools import setup

from dice_roller import __version__

setup(
    name="dice_roller",
    version=__version__,
    description="Module to roll a dice with certain variations.",
    url="https://github.com/Ajordat/dice_roller",
    author="Ajordat",
    author_email="alexjortri@gmail.com",
    maintainer="Ajordat",
    maintainer_email="alexjortri@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8"
    ],
    packages=["dice_roller"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "roll=dice_roller.main:main"
        ]
    }
)
