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
