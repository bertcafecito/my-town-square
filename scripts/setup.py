"""
Setup configuration for My Town Square Scripts package.
"""
from setuptools import setup, find_packages

setup(
    name="my-town-square-scripts",
    version="1.0.0",
    description="Automation scripts for My Town Square community event calendar",
    author="Bayonne Community",
    packages=find_packages(),
    install_requires=[
        "python-json-logger>=4.0.0",
        "icalendar>=6.3.2",
        "requests>=2.32.5",
        "PyPDF2>=3.0.1",
        "python-dateutil>=2.9.0",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "fetch-events=calendar_data.fetch_data:main",
            "aggregate-events=calendar_data.aggregate_data:main",
            "summarize-events=calendar_data.summarize_data:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
