import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vennfig",
    version="0.2.2",
    author="Shinichi Okada",
    author_email="okada.shin@gmail.com",
    description="Basic Venn Diagram Figures package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shinokada/vennfig",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'matplotlib', 'matplotlib_venn',
    ],
    python_requires='>=3.6',
)
