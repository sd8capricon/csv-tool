import os
import unittest
import csvTool
from testCases.testCases import cases


class TestCSVTool(unittest.TestCase):

    def setUp(self):
        self.files = ['hw_25000.csv', 'deniro.csv']
        self.testCases = cases
        self.fileList = []
        for file in self.files:
            pathTOFile = os.path.join('csvs', file)
            f = open(pathTOFile, 'r')
            self.fileList.append(f)

    def tearDown(self):
        for file in self.fileList:
            file.close()

    def test_count(self):
        for index, file in enumerate(self.fileList):
            if 'count' in self.testCases[self.files[index]]:
                self.assertEqual(csvTool.count(
                    file), self.testCases[self.files[index]]['count'])
                file.seek(0)
            else:
                print("No count tests for this file {}".format(
                    self.files[index]))
            print("Count tests passed for file {}".format(self.files[index]))
        print('\n')

    def test_mean(self):
        for index, file in enumerate(self.fileList):
            if 'mean' in self.testCases[self.files[index]]:
                meanTests = self.testCases[self.files[index]]['mean']
                for case in meanTests:
                    self.assertEqual(csvTool.mean(
                        file, case['col']), case['value'])
                file.seek(0)
            else:
                print("No mean tests for file {}".format(self.files[index]))
            print("Mean tests passed for file, {}".format(self.files[index]))
        print('\n')

    def test_filter(self):
        for index, file in enumerate(self.fileList):
            if 'filter' in self.testCases[self.files[index]]:
                filterTests = self.testCases[self.files[index]]['filter']
                for case in filterTests:
                    self.assertEqual(csvTool.filter(
                        file, case['col'], case['filter']), case['result'])
                file.seek(0)
            else:
                print("No filter tests for file {}".format(self.files[index]))
            print("Filter tests passed for file {}".format(self.files[index]))
        print('\n')


if __name__ == "__main__":
    unittest.main()
