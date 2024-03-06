import marko

text = open("./README.md").read()
doc = marko.parse(text)
for node in doc.children:
    print(node.body)
