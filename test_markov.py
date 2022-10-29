from markov import mk_pairs, DB


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


#############################################################

def test_db_add_to_empty():
    db = DB()

    db.add_pair(('spam', 'eggs'))

    excepted = {
        'spam': (['eggs'],
                 [1])
    }
    assert db.db == excepted


def test_dv_add_all_different():
    db = DB()

    db.add_pair(('spam', 'eggs'))
    db.add_pair(('bacon', 'ham'))

    expected = {
        'spam': (['eggs'], [1]),
        'bacon': (['ham'], [1])
    }

    assert db.db == expected
