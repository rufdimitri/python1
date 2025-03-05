def print_types():
    int1: int = 123
    float1: float = 1.2
    str1: str = "Andrew"
    str2: str = 'Andrew'
    bool1: bool = True

    print(int1)
    print(float1)
    print(str1)
    print(str2)
    print(bool1)

def get_type():
    unknown = 34.2
    unknown2 = 1.23
    unknown3 = 123
    print(f"type of unknown is {type(unknown)}")
    print(f"type of unknown and unknown2 are same? \n - {type(unknown) == type(unknown2)}")
    print(f"type of unknown and unknown3 are same? \n - {type(unknown) == type(unknown3)}")

#print_types()
get_type()