class Pet:

    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        if pet_type not in Pet.PET_TYPES:
            raise TypeError("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    # @property
    # def pet_type(self):
    #     return self._pet_type
    
    # @pet_type.setter
    # def pet_type(self, type):
    #     if not isinstance (type, Pet.PET_TYPES):
    #         raise TypeError("Pet TYpe must be an instance of PET_TYPE")
    #     self._pet_type = type

   
        

class Owner:
    
    def __init__(self, name):
        self.name = name

    def pets(self):
        return[pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance (pet, Pet):
            raise TypeError("Pet must be of type Pet")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)