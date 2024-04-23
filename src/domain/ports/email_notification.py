from domain.bill import Bill


class EmailNotification:
    """ Interface for email sending strategies. """
    def send_emails(self, bills: list[Bill]):
          pass