"""Customer success analysis functions"""

def find_critical_customers(customer):
	"""Find customers that need immediate attention"""
	critical = []
	#Multiple risk factors = critical status
	for customer in customers:
		risk_factor = 0

		if customer["health_score"] < 5:
			risk_factor += 1
		if customer["monthly_logins"] < 10:
			risk_factor += 1
		if customer["support_tickets"] > 4:
			risk_factor += 1
		if risk_factor >= 2:
			critical.append(customer) #add customer to the array
	return critical

def calculate_expansion_opportunities(customers):
	"""Find customers ready for upselling"""
	expansion_ready = []
	
	for customer in customers:
		# High engagement + healthy = expansion opportunity
		if (customer["health_score"] >= 8 and 
			customer["features_used"] >= 7 and 
			customer["monthly_logins"] >= 20):
			expansion_ready.append(customer)
	
	return expansion_ready