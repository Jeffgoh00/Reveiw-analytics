data = []
count = 0
with open ("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 == 0:
			print(len(data))
print("Data has been read,it have", len(data) ,"data") 


sum_len = 0
for d in data:
	sum_len += len(d)
print("Averange reviews is", sum_len/len(data))

#筛选
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print("Total have", len(new), "less than 100 words inside reviews")