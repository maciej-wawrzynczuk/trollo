from markov import mk_pairs


def test_mk_pairs_null():
    words = []
    assert not list(mk_pairs(words))


def test_mk_pairs_begin():
    words = ['spam']
    expected = (None, 'spam')

    assert expected in list(mk_pairs(words))


def test_mk_pairs_end():
    words = ['spam']
    expected = ('spam', None)

    assert expected in list(mk_pairs(words))


def test_mk_pairs_pair():
    words = ['spam', 'eggs']
    expected = ('spam', 'eggs')

    assert expected in mk_pairs(words)


def test_mk_pairs_i_dont_believe():
    words = ['bacon', 'eggs', 'spam']
    e1 = ('bacon', 'eggs')
    e2 = ('eggs', 'spam')

    result = mk_pairs(words)

    assert e1 in result and e2 in result
