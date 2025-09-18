# Enhanced Swiss customer database
customers = [
	{
		"name": "SwissTech AG",
		"health_score": 8.5,
		"monthly_logins": 25,
		"features_used": 7,
		"support_tickets": 1,
		"mrr": 2500,
		"region": "Zurich",
		"signup_date": "2024-03-15",
		"last_login": "2025-09-16"
	},
	{
		"name": "Geneva Consulting SA",
		"health_score": 4.2,
		"monthly_logins": 8,
		"features_used": 2,
		"support_tickets": 5,
		"mrr": 1200,
		"region": "Geneva",
		"signup_date": "2024-01-20",
		"last_login": "2025-09-10"
	},
	{
		"name": "Basel Innovation GmbH",
		"health_score": 9.1,
		"monthly_logins": 67,
		"features_used": 9,
		"support_tickets": 0,
		"mrr": 3500,
		"region": "Basel",
		"signup_date": "2024-06-08",
		"last_login": "2025-09-17"
	},
	{
		"name": "Lausanne Digital SARL",
		"health_score": 3.8,
		"monthly_logins": 12,
		"features_used": 3,
		"support_tickets": 8,
		"mrr": 1800,
		"region": "Lausanne",
		"signup_date": "2024-02-12",
		"last_login": "2025-08-30"
	},
	{
		"name": "Bern Systems AG",
		"health_score": 7.3, 
		"monthly_logins": 22, #how many times he or she logged in :)
		"features_used": 5,
		"support_tickets": 2, #when the client needed a support ticket 
		"mrr": 2100, #monthly recurring revenue used in Saas companies 
		"region": "Bern",
		"signup_date": "2024-04-03",
		"last_login": "2025-09-15" #you can analyze these
	}
]

def get_sample_customers():
	"""Return the sample customer database"""
	return (customers)