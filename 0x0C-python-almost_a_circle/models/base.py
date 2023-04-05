#!/usr/bin/python3
""" Base class of all other classes in this project"""
import json
import os
import csv


class Base:
    """ first class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor """
        if (id is not None):
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        my_list = []
        fname = cls.__name__ + '.json'
        if (list_objs is not None):
            for ins in list_objs:
                my_list.append(ins.to_dictionary())
        jstr = cls.to_json_string(my_list)
        with open(fname, 'w') as f:
            f.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if (json_string is None or len(json_string) == 0):
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if (cls.__name__ == 'Rectangle'):
            dummy = cls(1, 2)
        elif (cls.__name__ == 'Square'):
            dummy = cls(3)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        my_list = []
        fname = cls.__name__ + '.json'
        if os.path.isfile(fname):
            with open(fname, 'r') as f:
                stread = f.read()
                listjson = cls.from_json_string(stread)
                for l in listjson:
                    my_list.append(cls.create(**l))
        return (my_list)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes list objects in csv format and save"""
        fname = cls.__name__ + '.csv'
        my_list = []
        if (list_objs is not None):
            for ins in list_objs:
                dc = ins.to_dictionary()
                if (cls.__name__ == 'Rectangle'):
                    my_list.append([dc['id'], dc['width'], dc['height'],
                                    dc['x'], dc['y']])
                elif (cls.__name__ == 'Square'):
                    my_list.append([dc['id'], dc['size'], dc['x'], dc['y']])
                # print(my_list)
        with open(fname, "w") as f:
            wcsv = csv.writer(f)
            wcsv.writerows(my_list)

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes csv of the list of instances """
        my_list = []
        dc = {}
        fname = cls.__name__ + '.csv'
        if os.path.isfile(fname):
            with open(fname, 'r') as f:
                csvread = csv.reader(f)
                if (cls.__name__ == 'Rectangle'):
                    keys = ['id', 'width', 'height', 'x', 'y']
                elif (cls.__name__ == 'Square'):
                    keys = ['id', 'size', 'x', 'y']
                for row in csvread:
                    aux = 0
                    for i in row:
                        dc[keys[aux]] = int(i)
                        aux += 1
                    my_list.append(cls.create(**dc))
        return (my_list)
