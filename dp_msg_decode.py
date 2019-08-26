h = {}

def msg_decode(string, i = 0):
    if i >= len(string):
        return 1

    # already computed
    if h.get(i):
        return h.get(i)

    # consider only one number
    k = msg_decode(string, i + 1)

    # consider two numbers
    if i + 1 < len(string) and int(string[i]+string[i + 1]) < 27:
        k += msg_decode(string, i + 2)

    h[i] = k

    return k
        