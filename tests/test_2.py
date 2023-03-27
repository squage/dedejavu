import os
import pytest

# custom
import dedejavu.json_handling.auxillary_json as auxillary_json
import dedejavu.file_system.file_system as fs


def test3():
    """
    Assert that a list of files encountered in the test folder is a hardcoded answer below.
    """

    # TODO safer script path
    start_dir = os.getcwd()

    # init a list to hold files encountered.
    list_of_files = []
    for root, dirs, files in fs.os_walk_wrap(start_dir):
        assert root.startswith(start_dir)
        relative_root = root[len(start_dir):]

        #removing some files added after creating test.
        list_of_files.extend([x for x in files if ((fs.get_file_extension(x) not in [".pyc", ".swp"]) and (not x.startswith("non"))) ] )
    assert sorted(list_of_files)  == ['file1.txt', 'file2.md', 'file3.py', 'file4.md', 'test_1.py', 'test_2.py']






