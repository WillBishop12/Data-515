"""
Unit tests for homework3 file
Classes included:
 - TestHomework3: Tests create_dataframe function, which returns a data frame from a SQL query
of video ID, category ID, and language from YouTube videos.
"""

import unittest
import homework3_modified as hw3

class TestHomework3(unittest.TestCase):
    """
    Unit tests for create_dataframe
    Functions included:
    - test_wrong_filepath: tests an example of a filepath that doesn't exist
    - test_column_names: tests that the SQL query result has 3 columns with the right names
    - test_len: tests that the SQL query result has at least 10 rows
    - test_key: tests whether video_id and language are a key (expected to fail)
    """

    def test_wrong_filepath(self):
        """Tests that non-existent file path throws an error"""
        with self.assertRaises(ValueError):
            hw3.create_dataframe('x.db')

    def test_column_names(self):
        """Test for column names: 3 columns named video_id, category_id, language"""
        data_frame = hw3.create_dataframe('class.db')
        self.assertTrue(len(data_frame.columns) == 3)
        self.assertTrue(all(x in data_frame.columns
                            for x in ['video_id', 'category_id', 'language']))

    def test_len(self):
        """Test for length: SQL query returns at least 10 rows"""
        data_frame = hw3.create_dataframe('class.db')
        self.assertTrue(len(data_frame) > 9)

    def test_key(self):
        """Test for key: video_id and language are a key (expected to fail)"""
        data_frame = hw3.create_dataframe('class.db')
        self.assertTrue(len(data_frame.groupby(['video_id', 'language']).count())
                        == len(data_frame))

if __name__ == '__main__':
    unittest.main()
