## SAM Ingestion piplines to move data from SAMAPPMANAGER into AZure BLOB
def pipeline("CopySAMData"):
	def createLinkedService("SAMApp"):
		connection strin = '10.0.0.11'

def pipeline("SAMInfustionAPP"):
	def storeProc("Update SAM tables"):
		table = 'SAM_inf_patient'