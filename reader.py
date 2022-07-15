import csv
import json



class Reader():
    def group_reader(self,FilePath: str):
        """reads group file quoting the pipe"""
        pass
    
    def group_dict_creator(self,content_dictionary: dict,to_groups_dict: dict):
        for group in content_dictionary:    
                key = group['uuid']
                to_groups_dict[key] = group['group']
        return to_groups_dict

    def item_reader(self, filePath: str, groups_dict: dict):
        """reads item file quoting the pipe and inputing correct group description/context"""
        pass

    @staticmethod
    def item_dict_creator(content_dictionary: dict,groups_dict: dict, to_item_dict: dict):
        for item in content_dictionary:    
                item_dict = {
                    'uuid': item['uuid'],
                    'title': item['title'],
                    'description': item['description'],
                    'context' : groups_dict.get(item['group_id']),
                }
                to_item_dict.append(item_dict)
        return to_item_dict

    

class JsonReader(Reader):

    def group_reader(self,jsonFilePath: str):
        groups_dict={}
        with open (jsonFilePath, 'r') as json_file:
            json_dict = json.load(json_file)
        return self.group_dict_creator(json_dict, groups_dict)
    
    def item_reader(self,JsonFilePath : str, groups_dict: dict):
        items_data=[]
        with open (JsonFilePath, 'r') as json_file:
            json_dict = json.load(json_file)
        return self.item_dict_creator(json_dict, groups_dict, items_data)
    
class CsvReader(Reader):
    def group_reader(self,csvFilePath: str):
        groups_dict={}
        with open (csvFilePath, newline= '', encoding='utf-8') as csv_file:
            csv_content = csv.DictReader(csv_file, quotechar='|')
            return self.group_dict_creator(csv_content, groups_dict)
    
    def item_reader(self,csvFilePath : str, groups_dict : dict):
        items_data=[]
        with open (csvFilePath, newline= '', encoding='utf-8') as csv_file:
            csv_content = csv.DictReader(csv_file, quotechar='|')
            return self.item_dict_creator(csv_content, groups_dict, items_data)

