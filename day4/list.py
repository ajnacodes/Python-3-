# lists are a way of storing and organising data 
# fruits = ["Cherries", "Apples", "Pears"]
# list of states in America
usa_states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "New York",
              "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
              "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana",
              "Indiana", "Texas", "Iowa", "Wisconsin", "Alabama", "Maine", "Missouri", 
              "Arkansas", "Michigan", "Florida", "Nevada", "Colorado", "Alaska", "Hawaii"]

print(usa_states[2])
# change the content of an individual state
usa_states[-2] = "COLORADO"
print(usa_states[-2])
# add another state to the end of the list
# function append("") will add a new state to the end of the list
usa_states.append("Arizona")
print(usa_states[-1])

# function extend(["",""..]) will add new states to the end of the list - by adding a new list to it
usa_states.extend(["Utah", "New Mexico", "Montana"])

print(usa_states[-1])
print(usa_states[-2])
print(usa_states[-3])