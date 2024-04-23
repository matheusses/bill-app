from domain.ports.email_notification import EmailNotification
from domain.bill import Bill
class BillService:
    def __init__(self, mailService: EmailNotification):
        self._mail_service = mailService

    def notify_customers(self, bills: list[Bill] ):
        self._mail_service.send_emails(bills)
