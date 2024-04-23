import time
from uuid import uuid4
from main import Main
from domain.bill import Bill


class EmailTest:
    def __init__(self):
        self.app = Main.build()
        
    def generate_mock_customers(self, size=1001):
        bills = []
        for _ in range(size):
            bill = Bill(name=f"John Doe{uuid4()}",
            governmentId=11111111111,
            email=f"{uuid4()}@teste.com", 
            debtAmount=13213,
            debtDueDate='2022-10-12',
            debId=uuid4())
            bills.append(bill)
        return bills
        

    def test_notifify_customers(self):
        # given 
        tic = time.perf_counter()
        email_size= 1000
        bills = self.generate_mock_customers(email_size)
        toc = time.perf_counter()
        # when
        self.app.notify_customers(bills)
        #then
        print(f"emails: {email_size} - {toc - tic:0.4f} seconds")

test = EmailTest()
test.test_notifify_customers()