# contents of ./setup.py
from setuptools import setup

setup(
    name='pytest_report_autoname',
    packages=['pytest_report_autoname'],
    version='0.0.1',
    entry_points={
        'console_scripts': [
        ], # feel free to add if you have any
        "pytest11": ["name_of_plugin = pytest_report_autoname.plugin"]
    },
    classifiers=["Framework :: Pytest"],
)