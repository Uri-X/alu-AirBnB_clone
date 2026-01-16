#!/usr/bin/python3
'''
TESTS
'''
import unittest
from models.engine.file_storage import FileStorage
from uuid import UUID
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    '''
    all tests
    '''

    def test_moduleDocs(self):
        '''
        testing
        '''
        moduleDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        testing
        '''
        classDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.FileStorage.__doc__)
        self.assertGreater(len(classDoc), 0)

    def test_methodDocsSave(self):
        '''
        testing
        '''
        methodDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.FileStorage.save.__doc__)
        self.assertGreater(len(methodDoc), 0)


if __name__ == "__main__":
    unittest.main()
