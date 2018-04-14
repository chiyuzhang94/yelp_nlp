# for class balance, save 7000 records for each rating level
import json
import csv
file = open("1104data.json").read()
data = json.loads(file)

WriterIn = open("smalldata.csv",'wb')
record={"rating":'',"date":'', "content":'',"useful":'',"funny":'',"cool":'',"checkin":'', "online_order":'', "reservation":''}
writer=csv.DictWriter(WriterIn, record.keys())
writer.writeheader()  
stoplist = []
countdic = {}
for item in data:
	if item['rating'][0].split(" ")[0] not in stoplist:
		rating = item['rating'][0].split(" ")[0]
		if rating in countdic.keys():
			countdic[rating] += 1
			if countdic[rating] == 7000:
				stoplist.append(rating)
		else:
			countdic[rating] = 1
		content = " ".join(item['content']).encode("utf-8")
		useful = ""
		funny =""
		cool = ""
		check_count = ""
		online_order = ""
		reservation = ""
		if len(item['useful'])>0:
			useful = item['useful'][0]
		if len(item['funny'])>0:
			funny = item['funny'][0]
		if len(item['cool'])>0:
			cool = item['cool'][0]
		date = item['date'][0].split("\n")[1].split(" ")[-1]
		for statue in item['statue']:
			if "check" in statue:
				check_count = statue.split(" ")[0]
			if "Online" in statue:
				online_order = "1"
			if "Reservations" in statue:
				reservation = "1"

		record["rating"] = rating
		record["content"] = content
		record["useful"] = useful
		record["funny"] = funny
		record["cool"] = cool
		record["checkin"] = check_count
		record["online_order"] = online_order
		record["reservation"] = reservation 
		record["date"] = date
		
		writer.writerow(record)
	else:
		continue 
	#print item['date'][0].split("\n")[1].split(" ")[-1]

WriterIn.close()