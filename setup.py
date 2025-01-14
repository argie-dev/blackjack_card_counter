from setuptools import setup

setup(
    name="card-counter",
    version="0.1",
    py_modules=["card_counter"],
    install_requires=[
        "tkinter",  # tkinter is used in your script
    ],
    entry_points={
        'console_scripts': [
            'card-counter = card_counter:main',  # Make the main function callable
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
