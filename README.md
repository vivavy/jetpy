# Jetpy - Python precompiler for convient distributing

Jetpy is a Python precompiler for convient distributing.

## creating project

```sh
$ jetpy init
```

## building project

```sh
$ jetpy build
```

## running project

```sh
$ jetpy run
```

## running project with debug

```sh
$ jetpy run --debug
```

## pacakging details

by default, jetpy has only command `run`.
To add other commands, you need to install [jetpy-dev](https://github.com/vivavy/jetpy-dev) package.

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
│   |   ├── opengl.so.json - json file for wrapped module
│   │   └── libc.so.json - json file for wrapped module
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

# License

MPL 2.0

# Author

Vi Chapmann

# Copyright

Copyright (c) 2018 Ivan Chetchasov

# See also

[ntw3](https://github.com/vivavy/ntweb)

[honey](https://github.com/vivavy/honey)

[pyosdk](https://github.com/vivavy/pyosdk)
