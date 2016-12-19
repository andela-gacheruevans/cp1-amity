import unittest
from amityClass import Amity, rooms

class TestAmity(unittest.TestCase):
    """ Class contains method tests for creating rooms and getting rooms"""

    def setUp(self):
        self.test_amity = Amity()
        self.test_create_single_room = self.test_amity_.create_room({"<room_name>":["OCULUS"]},"O")

    def test_get_room_type(self):
        self.get_room_type = self.test_amity.get_room_type("O")
        self.assertEqual(self.get_room_type, "O", msg = "Wrong room type returned")

    def test_creation_of_rooms(self):
        #Test for creation of multiple offices
        self.test_amity.create_room({"<room_name>":["KRYPTON", "HOGWARTS"]}, "O")

        # Test or creation of multiple living spaces
        self.test_amity.create_room({"<room_name>":["GO", "PHP"]}, "L")
        self.assertIn("MODOR", self.test_create_single_room, msg = "Room not created")
        #All the key/value pairs in dictionary exist in rooms
        self.assertDictContainsSubset({
            "MODOR":{"occupants":[], "is_office": True},
            "OCULUS":{"occupants" :[], "is_office":True},
            "KRYPTON": {"occupants": [], "is_office": True},
            "VALHALLA": {"occupants": [], "is_office": True},
            "HOGWARTS": {"occupants": [], "is_office": True}},
            rooms, msg = "Multiple Rooms were not created")

    def test_adding_rooms_twice(self):
        #Test if room is added twice
        self.adding_room_twice = self.test_amity.create_room({"<room_name>":["HOGWARTS"]}, "O")
        self.ssertIn("HOGWARTS Exists\n", self.adding_room_twice, msg ="Room added twice")


if __name__ == '__main__':
    unittest.main()