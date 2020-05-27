def toLowerCase(str: str) -> str:
    
    new_str = ""
    for c in str:
        new_str += c.lower()

    return new_str


print( toLowerCase("Hello") )