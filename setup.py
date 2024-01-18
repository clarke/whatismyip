from setuptools import setup

setup(
    name='whatismyip',
    version='1.0.0',
    py_modules=['whatismyip'],
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'whatismyip = whatismyip:cli',
        ],
    },
)
