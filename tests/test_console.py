#!/usr/bin/python3
"""test module"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models import storage
import os


class TestConstructor(unittest.TestCase):
    """test class"""
    __dictionary_4_classes = {
        "BaseModel": BaseModel, "State": State, "State": State,
        "City": City, "Amenity": Amenity,
        "Place": Place, "Review": Review, "User": User
        }

    def test_help_method(self):
        """test help"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(
                "Quit command to exit the program.", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual("EOF command to exit the program.",
                             f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(
                """Creates a new instance of BaseModel, saves it""",
                f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual("""Print the string representation of an instance
        based on the class name and id.""", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(
                """Delete an instance based on the class name and id.""",
                f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(
                """Print all string representation of all instances""",
                f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(
                """Updates an instance based on the class name and id""",
                f.getvalue()[:-1])

    def rest_file_storage(self):
        """test create"""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        storage._FileStorage__objects = {}

    def create_new_objects(self):
        """create"""
        create_time = "2024-03-20T6:00:00"
        update_time = "2024-03-20T10:00:00"

        user_data = {
            "id": "1995123",
            "email": "ahmed@gmail.com",
            "password": "passAhmedWord95",
            "first_name": "Ahmed",
            "last_name": "Gamal",
            "created_at": create_time,
            "updated_at": update_time
        }
        u = User(**user_data)
        storage.new(u)
        amenity_data = {
            "id": "1995A_ID",
            "name": "AC",
            "created_at": create_time,
            "updated_at": update_time
        }
        a = Amenity(**amenity_data)
        storage.new(a)
        state_data = {
            "id": "1995S_ID",
            "name": "California",
            "created_at": create_time,
            "updated_at": update_time
        }
        s = State(**state_data)
        storage.new(s)
        city_data = {
            "id": "1995C_ID",
            "state_id": s.id,
            "name": "San Francisco",
            "created_at": create_time,
            "updated_at": update_time
        }
        c = City(**city_data)
        storage.new(c)
        place_data = {
            "id": "1995P_ID",
            "city_id": c.id,
            "user_id": u.id,
            "name": "Cozy Cottage",
            "description": "A lovely cottage in the heart of the city.",
            "number_rooms": 2,
            "number_bathrooms": 1,
            "max_guest": 4,
            "price_by_night": 100,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "created_at": create_time,
            "updated_at": update_time
        }
        p = Place(**place_data)
        storage.new(p)
        review_data = {
            "id": "1995R_ID",
            "place_id": p.id,
            "user_id": u.id,
            "text": "Had a great time staying here!",
            "created_at": create_time,
            "updated_at": update_time
        }
        f = Review(**review_data)
        storage.new(f)
        b = BaseModel(id="1995B_ID", created_at=create_time,
                      updated_at=update_time)
        storage.new(b)
        storage.save()

    def test_create(self):
        """test create"""
        self.rest_file_storage()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Emad")
            self.assertEqual("** class doesn't exist **", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Emad")
            self.assertEqual("** class doesn't exist **", f.getvalue()[:-1])

        for k in self.__dictionary_4_classes.keys():
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {k}")
                self.assertTrue(f"{k}."+f.getvalue()
                                [:-1] in storage.all().keys())
                self.assertIsInstance(storage.all().get(
                    f"{k}."+f.getvalue()[:-1]), eval(k))
        self.assertTrue(os.path.isfile("file.json"))

    def test_create_key_values(self):
        """test create"""
        self.rest_file_storage()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City name="t"e_st"')
            self.assertTrue("City."+f.getvalue()
                                [:-1] in storage.all().keys())
            self.assertIsInstance(storage.all().get(
                    f"City."+f.getvalue()[:-1]), City)
            self.assertIn("'name': 't\"e_st'")

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.count.__doc__)
        self.assertIsNotNone(HBNBCommand.strip_clean.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_show(self):
        """test create"""
        self.rest_file_storage()
        self.create_new_objects()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **", f.getvalue()[:-1])

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Emad")
            self.assertEqual("** class doesn't exist **", f.getvalue()[:-1])

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual("** instance id missing **", f.getvalue()[:-1])

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 3212133")
            self.assertEqual("** no instance found **", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User 1995123")
            self.assertEqual(
                storage.all()["User.1995123"].__str__(), f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Amenity 1995A_ID")
            self.assertEqual(
                storage.all()["Amenity.1995A_ID"].__str__(),
                f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show State 1995S_ID")
            self.assertEqual(
                storage.all()["State.1995S_ID"].__str__(),
                f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show City 1995C_ID")
            self.assertEqual(
                storage.all()["City.1995C_ID"].__str__(), f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Place 1995P_ID")
            self.assertEqual(
                storage.all()["Place.1995P_ID"].__str__(),
                f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Review 1995R_ID")
            self.assertEqual(
                storage.all()["Review.1995R_ID"].__str__(),
                f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel 1995B_ID")
            self.assertEqual(
                storage.all()["BaseModel.1995B_ID"].__str__(),
                f.getvalue()[:-1])

    def test_destroy(self):
        """test create"""
        self.rest_file_storage()
        self.create_new_objects()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual("** class name missing **", f.getvalue()[:-1])

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Emad")
            self.assertEqual("** class doesn't exist **", f.getvalue()[:-1])

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual("** instance id missing **", f.getvalue()[:-1])

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 3212133")
            self.assertEqual("** no instance found **", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User 1995123")
            self.assertEqual("", f.getvalue()[:-1])
            self.assertFalse("User.1995123" in storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Amenity 1995A_ID")
            self.assertEqual("", f.getvalue()[:-1])
            self.assertFalse("Amenity.1995A_ID" in storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy State 1995S_ID")
            self.assertEqual("", f.getvalue()[:-1])
            self.assertFalse("State.1995S_ID" in storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy City 1995C_ID")
            self.assertEqual("", f.getvalue()[:-1])
            self.assertFalse("City.1995C_ID" in storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Place 1995P_ID")
            self.assertFalse("Place.1995P_ID" in storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy Review 1995R_ID")
            self.assertEqual("", f.getvalue()[:-1])
            self.assertFalse("Review.1995R_ID" in storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy BaseModel 1995B_ID")
            self.assertEqual("", f.getvalue()[:-1])
            self.assertFalse("BaseModel.1995B_ID" in storage.all().keys())

def test_count(self):
    """test create"""
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd("count")
        self.assertEqual("** class name missing **", f.getvalue()[:-1])
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd("count Emad")
        self.assertEqual("** class doesn't exist **", f.getvalue()[:-1])
    for k in self.__dictionary_4_classes.keys():
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"count {k}")
            expected_count = len([obj for obj in storage.all(
            ).values() if isinstance(obj, self.__dictionary_4_classes[k])])
            self.assertEqual(str(expected_count), f.getvalue()[:-1])