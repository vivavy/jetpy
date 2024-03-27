import jet, sys, os

file = sys.argv.pop()
path = sys.argv.pop()
jetp = sys.argv.pop()

if "--mswin" in sys.argv:
    mswin = True
else:
    mswin = False

os.chdir(path)

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
    "__jetpath__": jetp
}

if mswin:
    globs["__mswin__"] = True

jet.__init__(jetp, mswin)

globs = {
    **globs,
    "__dict__": globs
}

if __name__ == '__main__':
    with open(file, "rt") as f:
        exec(f.read().replace("import jet\n", "# import jet\n"), builtins, globs)
