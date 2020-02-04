import json
with open("author_links.json", "r") as read_file:
    data = json.load(read_file)
    items =[]
    for item in data:
        items.append(item['author links'])
        new_items = ("\n".join(items))
    f = open("author_links.txt", "w")
    f.writelines(new_items)
    f.close()