import pytest

# custom
import dedejavu.json_handling.auxillary_json as auxillary_json
import dedejavu.file_system.file_system as fs


def test_stuff():
    """
    Testing the serialization function.
    """

    test_key = ("this", "that", 5)

    entry_sep = "__"
    value_type_sep = "@@"
    test_key_jsonabled = auxillary_json.make_tuple_key_jsonable(test_key, entry_sep=entry_sep,
                                                                value_type_sep=value_type_sep)
    test_key_rec = auxillary_json.reconstruct_tuple_key(test_key_jsonabled,
                                                        entry_sep=entry_sep,
                                                        value_type_sep=value_type_sep)
    assert test_key == test_key_rec


def test_file_is_markdown1():
    file1 = "this.md"
    assert fs.file_is_markdown(file1)


def test_make_tuple_key_jsonable1():
    # TODO fixtures ?
    # TODO variations on entry_sep, value_type_sep
    t1 = (1, "a", 113, "bcdef")
    a = auxillary_json.make_tuple_key_jsonable(t1)
    assert a == "1@@int__a@@str__113@@int__bcdef@@str"

    b = auxillary_json.reconstruct_tuple_key(a)
    assert t1 == b


def test_make_tuple_key_jsonable2():
    t2 = (1, "a", 113, 3.14, "bcdef")
    with pytest.raises(Exception) as _:
        auxillary_json.make_tuple_key_jsonable(t2)
