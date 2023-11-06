class ArcherFieldList(list):
    def __display_all_archer_fields__(self):
        for af in self:
            af.display()

    def __search_archer_field_name__(self, name):
        for afr in self:
            if afr.name == name:
                return f'Field name \"{name}\" found'

        return f'Field name \"{name}\" not found'

class ArcherField:
    fields = ArcherFieldList() # ref variable of list suppose 3000
    def __init__(self, id, name, type, value):
        self.id = id
        self.name = name
        self.type = type
        self.value = value
        ArcherField.fields.append(self)
    
    def display(self):
        print(self.__dict__)

def main():
    af_attach = ArcherField(9884, 'attachment', 6, ['test.pdf', 'sdfds.xlsx'])

    #af_attach.display()
    af_loc = ArcherField(9885, 'location', 2, [98894])
    #af_loc.display()    
    #print(ArcherField.fields)
    ArcherField.fields.__display_all_archer_fields__()
    # for archer_field in ArcherField.fields:
    #     if archer_field.name == 'attachment3':
    #         print('Name found')
    #     else:
    #         print('Name not found')
    print(ArcherField.fields.__search_archer_field_name__('attachment'))

if __name__ == '__main__':
    main()