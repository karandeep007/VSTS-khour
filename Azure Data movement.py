## RX30 Copy piplines to move data from SSP1 to Blob
def pipeline("CopyRX30 Data"):

	def activity("Copy"):
		add.Source("linktoRX30")
		add.Sink("insightsdwh")
def pipeline("SingleShotSTG"):
	def activity("lookupconfigdata"):

	def activity("ForEachTable"):
