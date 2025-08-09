from sqlAlchemy_example import DefaultDataAccess
from unittest.mock import MagicMock, patch
import unittest

class TestDefaultDataAccess(unittest.TestCase):
    def setUp(self):
        self.mock_engine = MagicMock()
        self.mock_session = MagicMock()
        
        # Patch sessionmaker to return the mock_session
        patcher = patch('sqlalchemy.orm.sessionmaker', return_value=lambda: self.mock_session)
        self.addCleanup(patcher.stop)
        self.mock_sessionmaker = patcher.start()
        
        # Class to be tested
        class TestDAO(DefaultDataAccess):
            def entityType(self):
                return 'Entity'  # Dummy

        self.dao = TestDAO(self.mock_engine)
        self.dao.session = self.mock_session  # Direct replacement for tests

    def test_create_calls(self):
        dummy_entity = MagicMock()
        self.dao.create(dummy_entity)
        self.mock_session.add.assert_called_with(dummy_entity)
        self.mock_session.commit.assert_called_once()

    def test_update_calls(self):
        dummy_entity = MagicMock()
        self.dao.update(dummy_entity)
        self.mock_session.merge.assert_called_with(dummy_entity)
        self.mock_session.commit.assert_called_once()

    def test_all_instances_calls(self):
        self.mock_session.query.return_value.all.return_value = ['entity1', 'entity2']
        result = self.dao.all_instances()
        self.mock_session.query.assert_called_with('Entity')
        self.assertEqual(result, ['entity1', 'entity2'])

if __name__ == "__main__":
    unittest.main()

