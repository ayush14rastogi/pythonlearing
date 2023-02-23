first_name=("ayush","sandeep")
last_name=("rastogi","reddy")

zipped_list = list(zip(first_name,last_name))

print(zipped_list)

zipped_set = set(zip(first_name,last_name))

print(zipped_set)

for (a,b) in zipped_set:
    print(a)

