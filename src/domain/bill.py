class Bill:
    def __init__(self, name, governmentId, email, debtAmount, debtDueDate, debId):
        self.__name = name
        self.__governmentId = governmentId
        self.__email= email
        self.__debtAmount = debtAmount
        self.__debtDueDate = debtDueDate
        self.__debId = debId

    def arrive_bill(self):
        return f"The bill with value {self.debtAmount} was received"
    
    def get_recipient(self):
        return self.__email