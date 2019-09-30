from setuptools import setup, find_packages

setup(
    name="ChecSeqTools",
    version="0.1-SNAPSHOT",
    packages=find_packages(),
    author="Christian Poitras",
    author_email="christian.poitras@ircm.qc.ca",
    description="Tools to analyze ChEC-seq data",
    keywords="bioinformatics, ChEC-seq",
    url="https://github.com/francoisrobertlab/chec-201908",
    license='GNU General Public License version 3',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License version 3'
    ],
    install_requires=[
        'click>=7.0',
        'pandas>=0.25.1',
        'seqtools@http://github.com/francoisrobertlab/seqtools/tarball/0.1'
    ],
    entry_points={
        'console_scripts': [
            'prepgenecov = checseqtools.PrepareGenomeCoverage:main',
            'fullanalysis = checseqtools.FullAnalysis:main'
        ]
    }
)
