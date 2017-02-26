from boyClass import Lad
from girlClass import Lass
from csvGenerator import randomiser
import csv
import logge

randomiser()
boysList=[]
girlsList=[]
boycsv = open('lad.csv')
girlcsv = open('lass.csv')
readBoy = csv.reader(boycsv, delimiter = ',')
readGirl = csv.reader(girlcsv, delimiter = ',')
#Adding Boys to the boyslist
for row in readBoy:
	boysList += [ Lad(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),row[5])]
#Adding Girls to the girlsList
for row in readGirl:
	girlsList+= [ Lass(row[0],int(row[1]),int(row[2]),int(row[3]),row[4]) ]

for girl in  girlsList:
	for boy in  boysList:
		
		if(girl.isPairable(boy) and boy.isPairable(girl)):

		
			#Displaying and logging commitments
			print(boy.name + " fell for the girl named " + girl.name)
			girl.changeCommitment()
			boy.changeCommitment()
			logge.log_maker(' commitment : ' + girl.name + ' and ' + boy.name)
			setattr(girl,girl.bfName,boy.name)
			setattr(boy,boy.gfName,girl.name)
			break

