Animal = [""] * 20
Colour = [""] * 10
AnimalTopPointer = 0
ColourTopPointer = 0


def PushAnimal(DataToPush:str):
    global AnimalTopPointer, ColourTopPointer, Animal, Colour
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True
    
def PopAnimal():
    global AnimalTopPointer, ColourTopPointer, Animal, Colour
    ReturnData = ""
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer = AnimalTopPointer - 1
        return ReturnData

    
