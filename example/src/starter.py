import jet, os

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
    "__file__": os.path.dirname(__file__)+"/main.py"
}

globs = {
    **globs,
    "__dict__": globs
}

if __name__ == '__main__':
    with open(os.path.dirname(__file__)+"/main.py", "rt") as f:
        exec(f.read(), builtins, globs)
