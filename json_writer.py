import json

class JsonWriter():
    

    def structure_output(self,items):
        output = []
        for item in items:
           uuid_title = item.get('uuid')+'_title'
           title = item.get('title')
           uuid_description = item.get('uuid')+'_description'
           description = item.get('description')
           context = item.get('context')
           
           output.append({
            uuid_title: {'string': title},
            uuid_description: {
                'string': description,
                'context': context,
            }
           })

        return output

    def write_to_json(self, items, json_file_path):
        with open(json_file_path, 'w+') as json_file:
            output = self.structure_output(items)
            json.dump(output, json_file)
        

        

        


