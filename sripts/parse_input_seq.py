fin = open("10000_ARB","r")
fout = open("10000_ARB_mod","w")

all_seq = [" 10000 1217\n"]
count = 0
for line in fin.readlines():
	
	if line == "\n":
		count = 1	
	elif line[0].isalpha():
		all_seq.append(str(line).rstrip('\r\n'))
	elif line[0] == " ":
		all_seq[count] += str(line[13:].rstrip('\r\n'))
		count += 1
	
for i in all_seq:
	word = i.split()
	temp = ''.join(word[1:])
	i = word[0] + "\t" + temp

for line in all_seq:
	word = line.split()
	temp = ''.join(word[1:])
	i = word[0] + "\t" + temp	
	fout.write(str(i)+"\n")
