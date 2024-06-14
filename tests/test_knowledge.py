import unittest
from models.knowledge import Knowledge

class TestKnowledge(unittest.TestCase):
    def test_add_data(self):
        knowledge = Knowledge()
        knowledge.add(["item1", "item2"])
        self.assertEqual(knowledge.data, [["item1", "item2"]])

if __name__ == "__main__":
    unittest.main()