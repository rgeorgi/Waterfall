from setuptools import setup, find_packages

setup(
    name="waterfall",  # Replace with your package name
    version="0.1.0",
    packages=find_packages(),
    scripts=["waterfall/watermark.py"],
    install_requires=[],  # Specify any dependencies if required
    author="Xinyuan Niu",  # Replace with the author's name
    description="Scalable Framework for Robust Text Watermarking and Provenance for LLMs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aoi3142/Waterfall",  # Replace with your repository URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",  # Adjust as per your version requirement
)
