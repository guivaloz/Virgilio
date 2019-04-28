from setuptools import setup

setup(
    name='Virgilio',
    version='1.0',
    py_modules=['virgilio'],
    install_requires=[
        'Click',
    ],
    entry_points="""
        [console_scripts]
        virgilio=virgilio:cli
    """,
)
