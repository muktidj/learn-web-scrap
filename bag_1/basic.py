import pandas as pd

states = ["Jakarta", "Aceh", "Jogja", "Papua", "Jepara"]
population = [5000, 6000, 8000,10000, 2000]

dict_states = {"States": states, "Population": population}

# Metode from_dict dalam pandas digunakan untuk membuat DataFrame baru dari dictionary. Ini adalah salah satu cara paling umum dan nyaman untuk membuat DataFrame dari data terstruktur yang sudah ada.
df_states = pd.DataFrame.from_dict(dict_states)
# print(df_states)

df_states.to_csv("states.csv")


# with open("write.txt", "w") as file:
#      for state in states:
#           if state != "Aceh":
#                file.write(state)



