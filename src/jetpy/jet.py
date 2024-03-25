import ctypes, json, sys, os, io, builtins, numpy

ctypes.c_void = None

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

def array(tp, size):
    return to_array([tp()]*size, tp)

def malloc(size):
    return to_array([0]*size, numpy.byte)


def __init__(jetpath):
    global __jetpath__, __stdlib__, print, input, exit, to_array
    __jetpath__ = jetpath
    __stdlib__ = native.load("libj" + ("64" if sys.maxsize == 9223372036854775807 else "32") + ".so")

    print = builtins.print
    input = builtins.input

    exit = __stdlib__.exit

    to_array = numpy.array
