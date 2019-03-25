def pipeline("CopyRX30 Data"):

	def activity("Copy"):
		add.Source("linktoRX30")
		add.Sink("insightsdwh")
