ent = int(input())
ent2 = []
while(ent != 0):
	ent2.insert(0,ent)
	ent = int(input())
	if (ent == 0):
		while(ent2 != []):
			print(ent2[0])
			del(ent2[0])
