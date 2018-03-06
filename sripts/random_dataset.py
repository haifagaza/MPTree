import random

set_path_seq = raw_input("Input the path of sequence file: ")
set_path_tree = raw_input("Input the path of tree file: ")
num_dataset = input("Input number of datasets needed: ")

infile = open(set_path_seq, "r")
outfile = open("all_seq", "w")
outfile2 = open("all_tree", "w")

all_seq = []
dataset = ""
for line in infile.readlines():
	dataset += line
	if line[0] == " ":
		taxa = line.split()
		taxa = int(taxa[0])
	else:
		taxa -= 1;
		if taxa == 0:
			all_seq.append(dataset)
			dataset = ""


infile2 = open(set_path_tree, "r")
all_tree = []
for tree in infile2.readlines():
	all_tree.append(tree)

index_dataset = []
selected_dataset = []
selected_tree = []

while len(selected_dataset) < num_dataset:
	random_index = random.randint(0,len(all_seq)-1)
	if random_index not in index_dataset:
		index_dataset.append(random_index)
		selected_dataset.append(all_seq[random_index])
		selected_tree.append(all_tree[random_index])

for i in selected_dataset:
	outfile.write(i)
for i in selected_tree:
	outfile2.write(i)

infile.close()
infile2.close()
outfile.close()
outfile2.close()