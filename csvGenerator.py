import csv
from random import randint

def toCsv(Data,filepath):
	# with open(filepath,'wb') as file:
	# 	writer=csv.writer(file,delimiter=',')
	# 	for line in Data:
	# 		writer.writerow(line)
		# writer.writerows(input)

	#Context manager writing to CSV

	'Context manager writing to CSV'
	with open(filepath,'w') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',') 
		for line in Data:
			spamwriter.writerow(line)


def randomiser():
	#Boys' List
	boys=['Alan','Akash','Abhinav','Abhishek','Bhavesh','Batuk','Chintala','Donny','Edward','Finn','Gregory','Hambort','Ian','Jagga','Kallu','Lyon','Manvendra','Nana','Okeefe','Park','Quentin','Robert','Shah','Taimur','Umar','Vikash','Will','Xavier','Yoda','Zeus']
	#Girls' List
	girls=['Anshika','Bhavana','Chikku','Dolly','Fanny','Gagru','Henna','Illeana','Jyoti','Kashmera','Lopa','Mahima']
	typeOfBoys=['Miser','Generous','Geek']
	typeOfGirls=['Choosy','Normal','Desperate']
	typeOfGifts=['Essential','Luxury','Utility']
	ladData=[]
	lassData=[]
	giftData=[]


	for i in range(0,29):
		ladData +=[(str(boys[i]),randint(0,10),randint(0,1000),randint(0,100),randint(0,100),typeOfBoys[randint(0,2)])]
	for i in range(0,11):
		lassData +=[(str(girls[i]),randint(0,10),randint(0,1000),randint(0,100),randint(0,100),typeOfGirls[randint(0,2)])]
	for i in range(0,10):
		giftData +=[('Gift'+ str(i),randint(0,100),randint(0,100),typeOfGifts[randint(0,2)])]

	toCsv(ladData,'lad.csv')
	toCsv(lassData,'lass.csv')
	toCsv(giftData,'gifts.csv')