users=["rahul","rohit","rishab","pandya","sanju","siraj"]
rahul_followers=["rohit","kohli","rishab"]
#follow_suggestions=[sanju,pandiya,siraj]
users_set=set(users)
difference_set=users_set.difference(rahul_followers)
print(difference_set)

#mutalfriends
users=["rahul","rohit","rishab","pandya","sanju","siraj"]
rahul_followers=["rohit","kohli","rishab"]
sanju_followers=["sanju","rohit","kohli"]
users_set=set(users)
mutual_friends= set(rahul_followers).intersection (set(sanju_followers))
print(mutual_friends)  

