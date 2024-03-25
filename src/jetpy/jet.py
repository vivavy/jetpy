import ctypes, json, sys, os, io, builtins, numpy

ctypes.c_void = None
ctypes.Any = object

__jetpath__ = ""

class path:
    def package(path):
        return __jetpath__+"/"+path
    def cwd(path):
        return path


class jcfg:
    def load(fp: io.TextIOWrapper):
        with fp:
            return jcfg.loads(fp.read())
    
    def loads(data: str):
        symbols = data.split("\n-----\n")
        syms = []

        for entry in symbols:
            syms.append({
                "name": entry.split("\n")[0],
                "args": tuple(eval("ctypes.c_"+i) for i in entry.split("\n")[1].split(",")) if entry.split("\n")[1] else (),
                "rtype": eval("ctypes.c_"+entry.split("\n")[2])
            })
        
        return tuple(syms)

# function to load shared library
def _load(name) -> ctypes.CDLL:
    return ctypes.CDLL(name)


class cfunc:
    def __init__(self, dll, name, *args):
        self.dll = dll
        self.name = name
        self.funcptr = dll.get_function(name, *args)
        self.args = args
    
    def __call__(self, *args):
        _args = []
        arg: object
        for i, arg in enumerate(args):
            if type(arg) == str:
                arg = arg.encode()
            if type(arg) != self.args[i]:
                _args.append(self.args[i](arg))
            else:
                _args.append(arg)
        return self.funcptr(*_args)


def string(name):
    with open(path.package("/resources/static/string/"+name+".string"), "rt") as f:
        return f.read()


class native:
    @staticmethod
    class library:
        def __init__(self, dll):
            self.dll = dll
        
        def init(self):
            for symbol in self.dll.cfg:
                self.__dict__.update(self.mkmcdict(symbol))
        
        def mkmcdict(self, symbol):
            name = symbol['name']
            args = symbol['args']
            
            return {name: staticmethod(cfunc(self.dll, name, *args))}

    @staticmethod
    class shared:
        def __init__(self, cfg: json, dll: ctypes.CDLL):
            self.dll = dll
            self.cfg = cfg
        
        def get_function(self, name: str, *args):
            return self.dll._FuncPtr(("$"+name, self.dll), args)

    @staticmethod
    def load(name: str) -> library:
        cfg = jcfg.load(open(os.path.abspath(path.package("resources/wrapped/" + name + ".jcfg"))))
        dll = ctypes.CDLL(path.package("resources/native/" + name))

        rv = native.library(native.shared(cfg, dll))

        rv.init()

        return rv

class DictObject:
    def __init__(self, dct):
        dct = {**dct}
        for k in dct:
            if type(dct[k]) == dict:
                dct[k] = DictObject(dct[k])
        self.__dict__.update(dct)
    
    def __getattribute__(self, __name: builtins.str) -> ctypes.Any:
        if __name.startswith("__"):
            return super().__getattribute__(__name)
        return self.__dict__[__name]

    def __setattr__(self, __name: builtins.str, __value: ctypes.Any) -> None:
        if __name.startswith("__"):
            super().__setattr__(__name, __value)
        else:
            self.__dict__[__name] = __value
    
    def __delattr__(self, __name: builtins.str) -> None:
        if __name.startswith("__"):
            super().__delattr__(__name)
        else:
            del self.__dict__[__name]
    
    def __getitem__(self, __name: builtins.str) -> ctypes.Any:
        return self.__dict__[__name]
    
    def __setitem__(self, __name: builtins.str, __value: ctypes.Any) -> None:
        self.__dict__[__name] = __value
    
    def __delitem__(self, __name: builtins.str) -> None:
        del self.__dict__[__name]

class JsonObject:
    @staticmethod
    def load(name: str) -> DictObject:
        return DictObject(json.load(open(os.path.abspath(path.package("resources/static/config/" + name + ".json")))))
    
    @staticmethod
    def save(name: str, data: DictObject):
        with open(os.path.abspath(path.package("resources/static/config/" + name + ".json")), "wt") as f:
            f.write(json.dumps(data, indent=4))
    
    @staticmethod
    def load_all():
        for f in os.listdir(path.package("resources/static/config")):
            if f.endswith(".json"):
                yield f[:-5], JsonObject.load(f[:-5])
    
    @staticmethod
    def save_all(data: dict):
        for f in os.listdir(path.package("resources/static/config")):
            if f.endswith(".json"):
                JsonObject.save(f[:-5], data[f[:-5]])

def array(tp, size):
    return to_array([tp()]*size, tp)

def malloc(size):
    return to_array([0]*size, numpy.byte)


def to_list(dctobj):
    rv = []

    for k in dctobj.__index__:
        rv.append(dctobj[k])
    
    return rv


def __init__(jetpath):
    global __jetpath__, __stdlib__, print, input, exit, to_array, config
    __jetpath__ = jetpath
    __stdlib__ = native.load("libj" + ("64" if sys.maxsize == 2 ** 63 - 1 else "32") + ".so")

    print = builtins.print
    input = builtins.input

    exit = __stdlib__.exit

    to_array = numpy.array

    cfg_keys, cfg_vals = zip(*JsonObject.load_all())
    config = DictObject({k: v for k, v in zip(cfg_keys, cfg_vals)})
