
    #     for index, file in enumerate(self.fileList):
    #         self.assertEqual(csvTool.count(
    #             file), self.testCases[self.files[index]]['count'])
    #         file.seek(0)

    # def test_mean(self):
    #     for index, file in enumerate(self.fileList):
    #         meanTests = self.testCases[self.files[index]]['mean']
    #         for case in meanTests:
    #             self.assertEqual(csvTool.mean(
    #                 file, case['col']), case['value'])
    #         file.seek(0)