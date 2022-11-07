# ⚙ TOML Config

## Getting started

You can write your config or simply use `vix prj init`, Vix will ask you some informations and will generate your project config.&#x20;

```toml
[project]
name = "VoxelCode"
version = "1.0"
authors = ['Unity']
description = "A Test for Voxel TOML Config"
mainfile = "main.vx"
args = []


[dependencies]
packages = ['std']
libraries = []
```

## Config

```toml
[project]         # -> Class
name              # -> Project name
version           # -> Project version
authors           # -> Project authors
description       # -> Project description
mainfile          # -> What file vix will run
args              # -> Compiler arguments


[dependencies]    # -> Class
packages          # -> Vix repo required Packages
libraries         # -> Builtin required C++ libraries like sqlite3
```
