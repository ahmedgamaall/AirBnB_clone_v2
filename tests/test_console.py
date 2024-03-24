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

        u_data = {
            "id": "1995123",
            "email": "ahmed@gmail.com",
            "password": "passAhmedWord95",
            "first_name": "Ahmed",
            "last_name": "Gamal",
            "created_at": create_time,
            "updated_at": update_time
        }
        usr = User(**u_data)
        storage.new(usr)
        a_data = {
            "id": "1995A_ID",
            "name": "AC",
            "created_at": create_time,
            "updated_at": update_time
        }
        amnty = Amenity(**a_data)
        storage.new(amnty)
        s_data = {
            "id": "1995S_ID",
            "name": "Cairo",
            "created_at": create_time,
            "updated_at": update_time
        }
        st = State(**s_data)
        storage.new(st)
        c_data = {
            "id": "1995C_ID",
            "state_id": st.id,
            "name": "Qena",
            "created_at": create_time,
            "updated_at": update_time
        }
        ct = City(**c_data)
        storage.new(ct)
        p_data = {
            "id": "1995P_ID",
            "city_id": ct.id,
            "user_id": usr.id,
            "name": "Entire home in Luray, Virginia",
            "description": "Short walk to River Outfitters for tubing, canoeing + kayaking. ",
            "number_rooms": 5,
            "number_bathrooms": 4,
            "max_guest": 5,
            "price_by_night": 400,
            "latitude": 45.8474,
            "longitude": -90.7564,
            "created_at": create_time,
            "updated_at": update_time
        }
        plc = Place(**p_data)
        storage.new(plc)
        r_data = {
            "id": "1995R_ID",
            "place_id": plc.id,
            "user_id": usr.id,
            "text": "George Washington National Forest + the National Park",
            "created_at": create_time,
            "updated_at": update_time
        }
        r = Review(**r_data)
        storage.new(r)
        bs = BaseModel(id="1995B_ID", created_at=create_time,
                      updated_at=update_time)
        storage.new(bs)
        storage.save()

    def test_create(self):
        """test method create"""
        self.rest_file_storage()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create ahmed")
            self.assertEqual("** class doesn't exist **", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create ahmed")
            self.assertEqual("** class doesn't exist **", f.getvalue()[:-1])

        for count in self.__dictionary_4_classes.keys():
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {count}")
                self.assertTrue(f"{count}."+f.getvalue()
                                [:-1] in storage.all().keys())
                self.assertIsInstance(storage.all().get(
                    f"{count}."+f.getvalue()[:-1]), eval(count))
        self.assertTrue(os.path.isfile("file.json"))

    def test_create_key_values(self):
        """test method create key values"""
        self.rest_file_storage()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City name="t"e_st"')
            self.assertTrue("City."+f.getvalue()
                            [:-1] in storage.all().keys())
            self.assertIsInstance(storage.all().get(
                f"City."+f.getvalue()[:-1]), City)
            self.assertIn("'name': 't\"e_st'")

    def test_docstrings(self):
        """test method docstrings"""
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
        self.assertIsNotNone(HBNBCommand.__doc__)

    def test_show(self):
        """test method show"""
        self.rest_file_storage()
        self.create_new_objects()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **", f.getvalue()[:-1])

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show ahmed")
            self.assertEqual("** class doesn't exist **", f.getvalue()[:-1])

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual("** instance id missing **", f.getvalue()[:-1])

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 45789321")
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
        """test method destroy"""
        self.rest_file_storage()
        self.create_new_objects()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual("** class name missing **", f.getvalue()[:-1])

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy ahmed")
            self.assertEqual("** class doesn't exist **", f.getvalue()[:-1])

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual("** instance id missing **", f.getvalue()[:-1])

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 45789321")
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
    """test method count"""
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd("count")
        self.assertEqual("** class name missing **", f.getvalue()[:-1])
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd("count ahmed")
        self.assertEqual("** class doesn't exist **", f.getvalue()[:-1])
    for count in self.__dictionary_4_classes.keys():
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"count {count}")
            expected_count = len([obj for obj in storage.all(
            ).values() if isinstance(obj, self.__dictionary_4_classes[count])])
            self.assertEqual(str(expected_count), f.getvalue()[:-1])
