def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("josé", "ortiz"))
#print(get_full_name("josé", 0)) #Esto genera error AttributeError 

