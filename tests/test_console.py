import unittest
from io import StringIO  # For capturing console output
from unittest.mock import patch  # For mocking functions

import models  # Assuming models.py is in the same directory

class HBNBCommandTest(unittest.TestCase):

    def setUp(self):
        self.hbnb = HBNBCommand()
        self.captured_output = StringIO()
        self.patch_stdout = patch('sys.stdout', self.captured_output)
        self.patch_stdout.start()

    def tearDown(self):
        self.patch_stdout.stop()
        models.storage.reset()  # Clear any created objects

    def test_emptyline(self):
        self.hbnb.emptyline()
        self.assertEqual(self.captured_output.getvalue(), '')

    @patch('HBNBCommand.precmd')
    def test_do_quit_precmd_true(self, mock_precmd):
        mock_precmd.return_value = 'quit'
        self.hbnb.do_quit('')
        self.assertEqual(self.captured_output.getvalue(), 'Exiting the program with formatting\n')

    @patch('HBNBCommand.precmd')
    def test_do_quit_precmd_false(self, mock_precmd):
        mock_precmd.return_value = 'other_command'
        self.hbnb.do_quit('')
        self.assertEqual(self.captured_output.getvalue(), '')

    def test_do_EOF(self):
        self.hbnb.do_EOF('')
        self.assertEqual(self.captured_output.getvalue(), '\nExiting the program without formatting\n')

    @patch('HBNBCommand.classes.get')
    def test_do_create_valid_class(self, mock_get_class):
        mock_get_class.return_value = BaseModel
        args = 'BaseModel name="New Base Model"'
        self.hbnb.do_create(args)
        self.assertIn('New Base Model', self.captured_output.getvalue())

    @patch('HBNBCommand.classes.get')
    def test_do_create_invalid_class(self, mock_get_class):
        mock_get_class.return_value = None
        args = 'InvalidClass name="Invalid"'
        self.hbnb.do_create(args)
        self.assertIn('** class doesn\'t exist **', self.captured_output.getvalue())

    def test_do_create_missing_class(self):
        args = ''
        self.hbnb.do_create(args)
        self.assertIn('** class name missing **', self.captured_output.getvalue())

    def test_do_create_invalid_kwargs(self):
        args = 'BaseModel invalid_key=invalid_value'
        self.hbnb.do_create(args)
        self.assertIn('** class doesn\'t exist **', self.captured_output.getvalue())  # Expect class error for invalid kwargs

    @patch('HBNBCommand.storage.all')
    def test_do_show_valid_class_id(self, mock_storage_all):
        mock_storage_all.return_value = {'BaseModel.123': BaseModel(id="123")}
        args = 'BaseModel 123'
        self.hbnb.do_show(args)
        self.assertIn('BaseModel(id="123")', self.captured_output.getvalue())

    @patch('HBNBCommand.storage.all')
    def test_do_show_invalid_class(self, mock_storage_all):
        mock_storage_all.return_value = {}
        args = 'InvalidClass 123'
        self.hbnb.do_show(args)
        self.assertIn('** class doesn\'t exist **', self.captured_output.getvalue())

    def test_do_show_missing_class(self):
        args = ''
        self.hbnb.do_show(args)
        self.assertIn('** class name missing **', self.captured_output.getvalue())
