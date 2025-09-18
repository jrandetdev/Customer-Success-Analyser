customers = ["Swiss Tech AG", "ZurichCorp", "BaselSoft"]
health_scores = [8.5, 4.2, 3.8]

print("Customer List:")
for i in range(len(customers)):
	print(f"{customers[i]}: {health_scores[i]}/10")
