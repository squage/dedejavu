"""
A module containing helper functions regardings paths, files, and folders.
"""

import os

def create_folder_if_not_exist(model_folder, print0=True):
    if not os.path.exists(model_folder):
        if print0:
            print("created folder %s" % model_folder)
        os.makedirs(model_folder)
        # TODO set return code
    else:
        if print0:
            print("folder %s already exists!" % model_folder)
            # TODO set return code


def os_path_split_wrap(path, print0=False):

    # wrapping some os functions for later wrapping, safety, logging, and printing reasons
    out = os.path.split(path)
    if print0:
        print("splitting path: ", path, out)
    return out


def os_path_join_wrap(*args):
    return os.path.join(*args)


def os_walk_wrap(folder0):
    return os.walk(folder0)


def os_path_exists_wrap(path0, print0=False):
    out = os.path.exists(path0)
    if print0:
        print("Does path %s exists: %s " % (path0, out))
    return out


def get_file_extension(filename, print0=False):
    """
    Returns the extension of a file name with a verbosity/printing option.

    :param filename:
    :param print0:
    :return: string with the file extension (without the ".")
    """
    ext = os.path.splitext(filename)[1]
    if print0:
        print("file extension of %s: %s" % (filename, ext))
    return ext


def file_is_markdown(file1):
    """
    Markdown (.md) will be a central file format in many projects. Gathering test for that format here.
    """

    return get_file_extension(file1, print0=False) == ".md"


def file_is_python(file1):
    """
    Python (.py)  will be a central file format in many projects. Gathering test for that format here.
    """
    return get_file_extension(file1, print0=False) == ".py"


