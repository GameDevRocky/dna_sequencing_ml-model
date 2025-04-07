import unittest
from src.data_loader import load_data, preprocess_data

class TestDataLoader(unittest.TestCase):

    def test_load_data(self):
        # Test loading of raw data
        raw_data = load_data('data/raw/sample.fast5')
        self.assertIsNotNone(raw_data)
        self.assertTrue(len(raw_data) > 0)

    def test_preprocess_data(self):
        # Test preprocessing of raw data
        raw_data = load_data('data/raw/sample.fast5')
        processed_data = preprocess_data(raw_data)
        self.assertIsNotNone(processed_data)
        self.assertTrue('kmer' in processed_data.columns)

if __name__ == '__main__':
    unittest.main()