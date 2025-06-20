given_name = "William"
middle_name = "Bradley"
family_name = "Pitt"

# calculate how long this name is
name_length = len(given_name + " " + middle_name + " " + family_name)

# Now we check to make sure that the name fits within the named entity character limit
named_entity_character_limit = 28
print(name_length <= named_entity_character_limit)