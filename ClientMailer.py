
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
5. create scheduler to determine mail send.

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
		''' Returns client object as client detail '''
		return f"Name: {self.first} {self.last} \
		Job: {self.job} \
		Company: {self.company} \
		email: {self.email}"

def get_clients(job):
	'''Get clients dependent on job '''
	for x in clients:
		if x.job == job:
			print(x)




c1 = Client("Steve", "Winner" , "Editor", "BBC", "steve.winner@bbc.co.uk")
c2 = Client("John", "Baker", "Producer", "ITV", "john.baker@itv.com")
c3 = Client("Isabelle", "Smith", "Promo Producer", "ITV", "isabelle.smith@itv.com")

clients = [c1,c2,c3]




get_clients('Promo Producer')

