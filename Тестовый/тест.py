def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

print(gen)
