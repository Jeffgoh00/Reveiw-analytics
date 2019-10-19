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



#筛选有多少留言少过100个字
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print("Total have", len(new), "less than 100 words inside reviews")
print(new[0])
print("-------------------------------------------")
print(new[1])

#筛选有提到Good的留言
good = []
for d in data:
	if "good" in d: #It will be a question at here, and the answer only with True/False
		good.append(d)
# "a" in "abc" -> True
print("Total have", len(good), "mentioned good")
print(good[0])



