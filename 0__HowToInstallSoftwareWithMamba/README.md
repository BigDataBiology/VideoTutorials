# How to install software with mamba

Video: [https://youtu.be/GEZn3fsrSdE](https://youtu.be/GEZn3fsrSdE)

Download mambaforge. You can find the right version at [https://github.com/conda-forge/miniforge#mambaforge](https://github.com/conda-forge/miniforge#mambaforge):

```bash
wget https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh
```

Install it

```bash
bash Mambaforge-Linux-x86_64.sh
```

Now you need to restart your shell

## Creating environments and installing software

```bash
mamba create -n semibin
```

Activate the environment

```bash
mamba activate semibin
```

```bash
mamba install -c conda-forge -c bioconda semibin
```

You can also set up `bioconda` and `conda-forge` once and for all. From the [bioconda documentation](https://bioconda.github.io/):

```bash
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
conda config --set channel_priority strict
```

Then all you need is to run

```bash
mamba install semibin
```

