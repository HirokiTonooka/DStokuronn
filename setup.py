import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test.py",
    version="0.0.2",
    author="Hiroki Tonooka",
    author_email="ohnishi.https://github.com/HirokiTonooka/DStokuronn",
    description='A package for visualization of aggregate data of players in "test.py"',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HirokiTonooka/DStokuronn",
    project_urls={
        "Bug Tracker": "https://github.com/HirokiTonooka/DStokuronn",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['test.py'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points = {
        'console_scripts': [
            'test.py = test.py:main'
        ]
    },
)