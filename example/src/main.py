# it needed for linter. you can skip this line
if "jet" not in __dict__: import jet

# this linese are equals
intp = jet.array(int, 32)
intp = jet.to_array([0]*32, int)

# this line makes maximum of member value x[i] < 256
intp = jet.malloc(32)

intp[0] = 2
intp[1] = 10

jet.print(intp[0], intp[1])

jet.print("Hello, World!")

jet.print(jet.input("lol> "))

jet.exit(32)
