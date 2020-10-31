
'''
PROJECT
Client Mailer
Small CRM
emailer
'''

'''
JOBS
1. Get Client Data
2. create client class
3. test send email
4. create library of email messages
5. create scheduler to determine mailsend.

'''

class Client():
	def __init__(self, first, last, job, company, email, replies=0, searches=0):
		self.first = first
		self.last = last
		self.job = job
		self.company = company
		self.email = email
		self.replies = replies
		self.searches = searches

	def __repr__(self):
		return f"Name: {self.first} {self.last} \
			   Job: {self.job} \
			   Company: {self.company} \
			   email: {self.email}"

c1 = Client("Steve", "Winner" ,"Editor", "BBC", "steve.winner@bbc.co.uk")


print(c1)

