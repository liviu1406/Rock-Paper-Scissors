# read animals.txt
ori_file = open("animals.txt", "r")
animals = ori_file.read()
ori_file.close()
# and write animals_new.txt
new_file = open("animals_new.txt", "w")
new_file.write(animals.replace("\n", " "))
new_file.close()
