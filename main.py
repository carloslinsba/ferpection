import argparse
from reader import CsvReader, JsonReader
from json_writer import JsonWriter

parser = argparse.ArgumentParser()

parser.add_argument('items', help='Please input filePath containing items, accepts json or csv')
parser.add_argument('groups', help='Please input filePath containing groups, accepts json or csv')
parser.add_argument('-o',"--output_file", help='Please input filename to the output file', required=True)


def is_file_a_csv_or_json(FilePath: str, filetype: str):
    if FilePath.lower().endswith(filetype):
        return True
    else:
        return False        

def read_group_file(group_file: str):
    """checks if group file is csv or json and reads it"""
    if is_file_a_csv_or_json(group_file, '.csv'):
        return CsvReader().group_reader(group_file)
    else:
        if is_file_a_csv_or_json(group_file,'.json'):
            return JsonReader().group_reader(group_file)
        else:
            raise Exception('Group filetype should be .csv or .json')
    
    
def read_item_file(item_file, items_dict, groups_dict):
    """checks if item file is csv or json and reads it"""
    if is_file_a_csv_or_json(item_file, '.csv'):
        return CsvReader().item_reader(item_file, groups_dict)
    else:
        if is_file_a_csv_or_json(item_file,'.json'):
            return JsonReader().item_reader(item_file, groups_dict)
        else:
            raise Exception('Item filetype should be .csv or .json')



if __name__ == '__main__':
    args = parser.parse_args()
    group_file = args.groups
    item_file=args.items
    output_file = args.output_file

    groups_dict={}
    items_dict={}
    try:
        groups_dict= read_group_file(group_file)
        items_dict= read_item_file(item_file, items_dict, groups_dict)
    except:
        raise Exception('Please check your input files') 
    try:
        JsonWriter().write_to_json(items_dict, output_file)
    except: 
        raise Exception('Not possible to write output file.')
    
