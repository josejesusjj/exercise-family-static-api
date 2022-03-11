
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
    
    'name': 'John',
    'Age' : 33,
    'Lucky Numbers' : [7, 13, 22]
},{
    
    'name': 'Jane',
    'Age' : 35,
    'Lucky Numbers' : [10, 14, 3]
},{
    
    'name': 'Jimmy',
    'Age' : 5,
    'Lucky Numbers' : [1]
}]

    def __str__(self):
        return "Objeto familia"


    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member['id'] = self._generateId()
        self._members.append(member)
       

    def delete_member(self, id):
        # fill this method and update the return
        pass

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            #if id == member.get('id'): --ambos sirven aqui--
            if id == member['id']:
                return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

family = FamilyStructure('Jackson')

print(family)
