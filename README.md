# Jetpy - Python precompiler for convient distributing

Jetpy is a Python precompiler for convient distributing.

## creating project

```sh
$ jetpy init
```

## build project

```sh
$ jetpy build
```

## run *.jet file

```sh
$ jetpy run
```

## run project without build (unstable)

```sh
$ jetpy debug
```

Note: when you run `debug`, package is read-write, but when you run `run` package is read-only
and all changes in package will be reset.

# Project structure

```
.
├── resources - resources for project will be saved in single file - `out.jet`
│   ├── static
│   │   ├── png
│   │   │   └── icon.png
│   │   └── string - strings could be saved externally for much easier modding
│   │       └── title.string - string file for title
│   ├── wrapped
│   |   ├── opengl.so.jcfg - jcfg file for wrapped module
│   │   └── libc.so.jcfg - jcfg file for wrapped module
│   └── native
│       ├── opengl.so - native module to be wrapped
│       └── libc.so - native module to be wrapped
├── src
│   ├── opengl.py - wrapped module
│   └── main.py
├── README.md - needed for jetdistutils
├── config.json - needed for building
├── requirements.txt - needed for building and jetdistutils
└── LICENSE - needed for jetdistutils
```

Note: all *.py files will become *.pyc while build process

# License

MPL 2.0

# Author

Vi Chapmann

# Copyright

Copyright (c) 2018 Ivan Chetchasov

# See also

[ntw3](https://github.com/vivavy/ntw3)

[honey](https://github.com/vivavy/honey)

[pyosdk](https://github.com/vivavy/pyosdk)
