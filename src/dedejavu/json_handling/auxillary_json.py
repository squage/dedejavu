"""A few functions I tend to use across projects"""
import json
import os

def json_dumper(dict_to_save, filepath, print0=True):
    """
    Standardizing json saving.

    :param dict_to_save:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as outfile:
        json.dump(dict_to_save, outfile)

    if print0:
        print("saving json dict to %s os.getcwd(): %s " % (
            filepath, os.getcwd()))

    outfile.close()


def json_loader(filepath):
    """
    Standardizing json loading.

    :param filepath:
    :return:
    """
    with open(filepath, 'r') as f_json_load:
        out = json.load(f_json_load)
    return out


def make_tuple_key_jsonable(key, entry_sep="__", value_type_sep="@@"):
    """
    Implementing a small convention to serialize a key. No attempts at optimizing, just a small hacky way for a few small local projects.
    Simply choosing a convention for separators and concatenating.

    See tests for example.

    :param key:
    :param entry_sep:
    :param value_type_sep:
    :return:
    """
    list0 = []
    for x in key:
        if isinstance(x, int):
            t = "int"
        elif isinstance(x, str):
            t = "str"
        else:
            raise Exception("Sorry, non-allowed data type")
            #t = "?"
        list0.append("".join([str(x), value_type_sep, t]))
    return entry_sep.join(list0)


def reconstruct_tuple_key(t0, entry_sep="__", value_type_sep="@@"):
    """

    """

    out = []
    for x in t0.split(entry_sep):
        value, type0 = x.split(value_type_sep)
        if type0 == "int":
            out.append(int(value))
        elif type0 == "str":
            out.append(str(value))
        else:
            out.append(value)
    return tuple(out)

#if __name__ == '__main__':
#    print(__package__)
