
item = {}
item.update({"ore": 1})

print(item)

modify_key = "ore"
item[modify_key] = item.get(modify_key, 0) + 1
print(item)
