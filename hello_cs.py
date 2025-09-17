print("Customer Success Analytics Tool v1.0")
print("Ready to analyse customer data!")
#simple hashtag for comments, and use of print.

customer_name = "SwissTech AG"
logins_this_month = 25 #customers logged 25 times this month
ideal_logins_per_month = 30
login_ratio = logins_this_month / ideal_logins_per_month #percentage value of the raito
raw_score = login_ratio / 10 #gives a score out of 10, easy to understand
health_score = min(raw_score, 10) #the score is capped at min 10

print(f"Customer: {customer_name}")
print(f"Health Score: {health_score:.1f}/10")
#f is like formating a screen 