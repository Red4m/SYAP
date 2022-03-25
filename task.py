data = {
    1: {
        "name": "name1",
        "password": ("lastname1", 1, "june")
    },
    2: {
        "name": "name2",
        "password": ("lastname2", 2, "february")
    },
    3: {
        "name": "name3",
        "password": ("lastname3", 3, "july")
    }
}

month = input("month")
resent_month = input("recent month")

for key, value in data.items():
  for i in value.keys():
    if data[key][i][2] == month:
      print(data[key][i][2])
      new_l = list(data[key][i])
      new_l.pop()
      new_l.append(resent_month)
      data[key][i] = tuple(new_l)


print(data)