# it needed for linter. you can skip this line
try:
    jet
    try:
        import jet  # definetly ImportError
        raise RuntimeError("Broken runtime")
    except ImportError:pass
except NameError:
    raise RuntimeError("Not a JETPY runtime")

"""# this linese are equals
intp = jet.array(int, 32)
intp = jet.to_array([0]*32, int)

# this line makes maximum of member value x[i] < 256
intp = jet.malloc(32)

intp[0] = 2
intp[1] = 10

jet.print(intp[0], intp[1])

jet.print("Hello, World!")

jet.print(jet.input("lol> "))

jet.exit(32)"""

jet.print(jet.string("message"))

jet.exit(0)
