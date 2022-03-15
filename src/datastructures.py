
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
#p
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
    
    'id': self._generateId(),
    'name': 'John',
    'age' : 33,
    'lucky_numbers' : [7, 13, 22]
},{
     "id": self._generateId(),
    'name': 'Jane',
    'age' : 35,
    'lucky_numbers' : [10, 14, 3]
},{
     "id": self._generateId(),
    'name': 'Jimmy',
    'age' : 5,
    'lucky_numbers' : [1]
}]

    def __str__(self):
        return "Object family"

    # This method returns all the family members
    def get_all_members(self):
        return self._members

    # This method retrieve a single member
    def get_member(self, id):
        "Returns the member with the given id or None"
        member = None

        # We find the member with the given id
#        try:
#            member = [member for member in self._members if member["id"] == id][0]
#        except IndexError:
#            pass
#        return member

        for member in self._members:
            #if id == member.get('id'): #--ambos sirven aqui--
            if id == member['id']:
                return member
 

    # This method creates random members ID's when adding members
    def _generateId(self):
        return randint(0, 99999999)

    # This method add a new member
    def add_member(self, member):            
        self._members.append({
            "id": "id" not in member and self._generateId(),**member,})
    
    # This method delete a member
    def delete_member(self, id):      
        self._members = [member for member in self._members if member["id"] != id]

family = FamilyStructure('Jackson')

print(family)
