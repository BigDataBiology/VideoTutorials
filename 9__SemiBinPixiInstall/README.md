# How to get SemiBin installed with pixi

## Install pixi

First, you need to [install pixi](https://pixi.sh/dev/)

```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

Ensure that it is installed correctly by running

```bash
pixi info
```

## Install SemiBin (with CPU support)

Create a `pixi.toml` file with the following content (this is also available in this repository as `w_cpu_pixi.toml`):

```toml(./w_cpu_pixi.toml)
[project]
authors = ["Luis Pedro Coelho <luis@luispedro.org>"]
channels = ["conda-forge", "bioconda"]
name = "semibin_install"
platforms = ["linux-64", "osx-64"]
version = "0.1.0"

[tasks]

[dependencies]
semibin = ">=2.1.0,<3"
```

Then, run `pixi install` in the same directory as the `pixi.toml` file to download and install SemiBin2.

### With GPU support

If you want to use SemiBin with GPU, you need to install Pytorch with GPU support as well. Starting with the example above, you need to add `pytorch-gpu` to the `dependencies` section and `cuda` to the `system-requirements` section. This is also available in this repository as `w_gpu_pixi.toml`:

```toml(./w_gpu_pixi.toml)
[project]
authors = ["Luis Pedro Coelho <luis@luispedro.org>"]
channels = ["conda-forge", "bioconda"]
name = "semibin_install"
platforms = ["linux-64"]
version = "0.1.0"

[tasks]

[dependencies]
semibin = ">=2.1.0,<3"
pytorch-gpu = "*"

[system-requirements]
cuda = "12.0"
```

Now, as above, run `pixi install` in the same directory as the `pixi.toml` file to download and install SemiBin2 with GPU support.


