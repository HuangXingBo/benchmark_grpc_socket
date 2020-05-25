def inc(x):
    return x + 1


def wrapper():
    import polyglot
    @polyglot.export_value
    def inc(a):
        return a

    return inc


import cloudpickle

data = cloudpickle.dumps(wrapper)
with open('/tmp/func.txt', 'wb') as fd:
    fd.write(data)
