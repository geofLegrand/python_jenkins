def groups_per_user(group_dictionary:dict):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			
			if user in user_groups: 
				user_groups[user].append(group)
			else:
				user_groups[user]=[group]
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],"public":  ["admin", "userB"],"administrator": ["admin"] }))