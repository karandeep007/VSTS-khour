#This is a Test file to start work on Git repo form second account

def pipeline("CopySAMData"):
	def createLinkedService("SAMApp"):
		connection strin = '10.0.0.11'

