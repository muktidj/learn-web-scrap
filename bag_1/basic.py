states = ["Jakarta", "Aceh", "Jogja", "Papua", "Jepara"]

print(states[-2])

with open("write.txt", "w") as file:
     for state in states:
          if state != "Aceh":
               file.write(state)



