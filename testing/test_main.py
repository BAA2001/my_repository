def test_get_none():
    from main import get_none

    assert get_none() is None


test_get_none()


def test_flatten_dict():
    from main import flatten_dict

    assert flatten_dict({"a": {"b": 1}, "c": 2}) == [1, 2]


test_flatten_dict()
