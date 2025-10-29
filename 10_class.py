class VisaRequest:
    def __init__(self, name, nationality, purpose, date):
        self.name = name
        self.nationality = nationality
        self.purpose = purpose
        self.date = date

    def print_name(self):
        print(self.name)

req_visa1 = VisaRequest("wawan","Indonesia","jalan2","10 nov")
req_visa1.print_name()

req_visa2 = VisaRequest("andi","malaysia","kerja","11 nov")
req_visa2.print_name()