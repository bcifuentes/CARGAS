import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Simulador_de_campo_electrico", # Replace with your own username
    version="0.0.1",
    author="Jean Pierre Cifuentes Salazar & Juan Diego Zuñiga",
    author_email="bcifuentes@unal.edu.co",
    description="Un agradable simulador de campo electrico",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ceratoide/CARGAS",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)