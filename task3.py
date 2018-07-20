"""JSONParser class, This module is to parse the JSON in specific format and
to change it in specific format"""

import json
import sys


class JSONParser(object):
    """This class is to format JSON in specific format"""

    def __init__(self, source_path=None, destination_path=None):
        """This is the constructor of JSONParser class"""

        self.source_path = source_path
        self.destination_path = destination_path
        self.source_dictionary = None
        self.destination_dictionary = None

    def set_source_path(self, source_path):
        """This is the function to set source_path for loading JSON"""

        self.source_path = source_path

    def set_destination_path(self, destination_path):
        """This is the function to set destination_path for writing JSON"""

        self.destination_path = destination_path

    def save_JSON(self):
        """This function is to save the current formatted dictionary
           to current destination_path"""

        try:
            with open(self.destination_path, 'w') as to_write:
                json.dump(formatted_dictionary, to_write)
        except TypeError:
            print("please provide correct path for destination")



    def load_JSON(self):
        """This is the function to load JSON from source_path into source_dictionary object"""
        try:
            with open(self.source_path, 'r') as to_read:
                self.source_dictionary = json.load(to_read)
        except IOError:
            print ("Cannot find source file")

    def get_textures(self, current_set):
        """This is the function to get textures for given set"""
        try:
            texture_name = str(current_set["name"]) + '_' + str(current_set["id"])
            return self.source_dictionary.get("model_info").\
                        get("textures").get(texture_name).get("diffuse")
        except TypeError:
            print("Please define correct source file first")

    def get_sets(self, material):
        """This is the function to get sets along with features for given material"""
        try:
            set_name = str(material["name"]) + '_' + str(material["id"])
            j = 0
            setlist = []
            for _set in self.source_dictionary.get("model_info").get("sets").get(set_name):
                setlist.append(None)
                setlist[j] = self.source_dictionary.get("model_info").get("sets").get(set_name)[j]
                setlist[j]["texture"] = (self.get_textures(_set))
                j += 1
            return setlist
        except TypeError:
            print("Please define correct source file first")

    def parse_JSON(self):
        """This is the function to parse JSON in source_path"""
        try:
            self.destination_dictionary = {}
            materials = self.source_dictionary.get("model_info").get("materials")
            i = 0
            self.destination_dictionary["model_info"] = {}
            self.destination_dictionary["model_info"]["materials"] = []
            for material in materials:
                self.destination_dictionary["model_info"]["materials"].append(None)
                self.destination_dictionary["model_info"]["materials"][i] = \
                                      self.source_dictionary.get("model_info").get("materials")[i]
                self.destination_dictionary["model_info"]["materials"][i]["sets"] = \
                                      self.get_sets(material)
                i += 1
            return self.destination_dictionary
        except TypeError:
            print("Please define correct source file first")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        json_parser = JSONParser()
        json_parser.set_source_path(sys.argv[1])
        json_parser.set_destination_path(sys.argv[2])
        json_parser.load_JSON()
        formatted_dictionary = json_parser.parse_JSON()
        json_parser.save_JSON()
    else:
        print("Please provide exactly 2 arguments")





