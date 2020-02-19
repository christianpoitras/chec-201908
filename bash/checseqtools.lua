help([[
For detailed instructions, go to:
    https://github.com/francoisrobertlab/checseqtools

This module loads the following modules and their requirements:
    - python/3.7.4
    - fastqc/0.11.8
    - bwa/0.7.17
    - bowtie2/2.3.4.3
    - samtools/1.9
    - bedtools/2.27.1
    - kentutils/20180716
    - vap
    - plot2do
]])

whatis("Version: 1.0.0")
whatis("Keywords: ChEC-SEQ, Utility")
whatis("URL: https://github.com/francoisrobertlab/checseqtools")
whatis("Description: Tools for analysis of ChEC-seq data")

always_load("nixpkgs/16.09")
always_load("gcc/7.3.0")
always_load("python/3.7.4")
always_load("fastqc/0.11.8")
always_load("bwa/0.7.17")
always_load("bowtie2/2.3.4.3")
always_load("samtools/1.9")
always_load("bedtools/2.27.1")
always_load("kentutils/20180716")
always_load("vap")
always_load("plot2do")

local venv = "~/checseqtools-robertf-venv"
prepend_path("PATH", pathJoin(venv,"bash"))
prepend_path("PATH", pathJoin(venv,"bin"))
