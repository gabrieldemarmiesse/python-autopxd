#!/usr/bin/env python
import glob
import os.path
import re
import pytest
import autopxd


def test_all():
    for file_path in glob.iglob('test/*.test'):
        with open(file_path) as f:
            data = f.read()
        c, cython = re.split('^-+$', data, maxsplit=1, flags=re.MULTILINE)
        c = c.strip()
        cython = cython.strip() + '\n'

        whitelist = None
        cpp_args = []
        if file_path == 'test/whitelist.test':
            test_path = os.path.dirname(file_path)
            whitelist = ['test/tux_foo.h']
            cpp_args = ['-I', test_path]
        actual = autopxd.translate(c, os.path.basename(file_path), cpp_args, whitelist)
        assert cython == actual



if __name__ == '__main__':
    pytest.main([__file__])
