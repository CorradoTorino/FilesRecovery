import unittest
import os
import sys
import shutil

from FileProcessor import FileProcessor

class FileProcessorCopyToAbsolutePathTest(unittest.TestCase):

    def test_FileProcessorCopyFilesTest_Run_EmptyFolder(self):

        inputFolder = r"e:"
        outputFolder = r"d:\Temp\FileProcessorTestOuput"
                          
        processor = FileProcessor(inputFolder, outputFolder)
        processor.Run()

if __name__ == '__main__':
    unittest.main()