def mk_pairs(words):
    if words:
        yield None, words[0]
        for count in range(len(words) - 1):
            yield words[count], words[count+1]
        yield words[-1], None
