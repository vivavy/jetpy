import jet, sys, os

file = sys.argv.pop()
path = sys.argv.pop()

builtins = {
    "jet": jet,
    "int": int,
    "float": float,
    "str": str,
    "bytes": bytes,
    "object": object,
    "any": object
}

globs = {
    "__builtins__": builtins,
    "__file__": file,
    "__jetpath__": path
}

jet.__jetpath__ = path

globs = {
    **globs,
    "__dict__": globs
}

if __name__ == '__main__':
    with open(file, "rt") as f:
        exec(f.read(), builtins, globs)
