#!/usr/bin/python3
"""
contains the FileStorage class
"""

import json 
from Models.amenity import Amenity 
from models.base-model import BaseModel
from models.city import City 
from models.place import Place
from models.review import Review
from models.state import State 
from models .user import User
name-Class = ["BaseModel", "City", "State", "place", "Amenity", "Review", "User"]

class filestorage:
	"""
	"""
	_file_path = "file.json"
	_object = {}

	def.all(self):
	"""
	"""
	return FileStorage.__objects

	def new(self, obj):
		""" sets  the obj with key in __objects
		"""
		class_name = obj.__class__.__name__
		id = obj.id
		clas_id = class_name + "." + id
		FileStorage.__objects[clas_id] = obj

	def save (self):
		""" file storage
		"""
		dict_to_json = {}
		for key, value in FileStorage.__objects.items():
			dict_to_json[key] = value.to_dict()
		with open(FileStorage.__file_path, "w", encoding='utf-8') as fil:
			dump(dict_to_json, fil)

	def reload(self):
		""" if (__file_path) exists deserializes JSON file to __objects
			elif , do nothing. If the file not exist,
		"""
		dic_obj = {}
		FileStorage.__objects = {}
		if (exists(FileStorage.__file_path)):
			with open(FileStorage.__file_path, "r") as fil:
				dic_obj = load(fil)
				for key, value in dic_obj.items():
					class_nam = key.split(".")[0]
					if class_nam in name_class:
						FileStorage.__objects[key] = eval(class_nam)(**value)
					else:
						pass
