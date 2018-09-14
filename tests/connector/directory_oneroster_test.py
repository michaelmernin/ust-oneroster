import unittest
import user_sync.connector.directory_oneroster

class OneRosterDirectoryTest(unittest.TestCase):

    def assert_eq(self, result, expected, error_message):
        '''
        compares the result against the expected value, and outputs an error
        message if they don't match. Also outputs the expected and result
        values.
        '''
        self.assertEqual(result, expected, error_message + '\nexpected: %s, got: %s' % (expected, result))

    def test_connector_metadata(self):
        directory_connector = user_sync.connector.directory_oneroster

        self.assert_eq(directory_connector.connector_metadata(), {'name': 'oneroster'},
                       "The OneRoster connector has an invalid name in its metadata")