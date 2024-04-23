from domain.ports.email_notification import EmailNotification
from domain.bill import Bill
from concurrent.futures import ThreadPoolExecutor


class ThreadedEmailNotification(EmailNotification):

    def __send_email(self, email:str):
        print (f"Sending email {email}...")

    def send_emails(self, bills: list[Bill], max_workers=4):
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(self.__send_email, bill.get_recipient()) for bill in bills]
