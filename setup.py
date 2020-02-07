import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="gitbackhub",
    author="Markus Holtermann",
    author_email="info@markusholtermann.eu",
    description="A script to backup / mirror GitHub repositories.",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarkusH/gitbackhub",
    packages=setuptools.find_packages(),
    install_requires=["Click>=6", "requests>=2.18.3"],
    extras_require={"testing": ["pytest>=5.3,<5.4"]},
    setup_requires=["setuptools_scm>=3.4.2,<4"],
    use_scm_version=True,
    entry_points={"console_scripts": ["gitbackhub = gitbackhub.cli:cli"]},
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Version Control",
        "Topic :: System :: Archiving :: Backup",
        "Topic :: Utilities",
    ),
)
