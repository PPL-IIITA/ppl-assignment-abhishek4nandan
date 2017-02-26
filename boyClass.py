class Lad:

	#Class Variables
	noOfLads=0;
	commitStatus='S'
	gfName=''
	happinessMeter=0
	pairable=True


	#Constructor for attribute initialisation
	def __init__(self,name,attractionRating,budget,intelligence,minAttrReq,typeOfBoy):
		self.name=name
		self.attractionRating=attractionRating
		self.budget=budget
		self.intelligence=intelligence
		self.minAttrReq=minAttrReq
		self.typeOfBoy=typeOfBoy


	#Checks if a lad and a lass can be paired
	def isPairable(self,lass):
		if(self.budget<lass.budget):
			self.pairable=False
		if(lass.attractionRating<self.minAttrReq):
			self.pairable=False
		if(lass.commitStatus=='C' or self.commitStatus=='C'):
			self.pairable=False
		return self.pairable

	#Check commitment status	
	def isCommitted(self):
		
			return self.commitStatus
	#Alter commitment status
	def changeCommitment(self):
		if self.commitStatus=='S':
			self.commitStatus='C'  




