from application.bill_service import BillService
from infra.notification.notification_factory import NotificationFactory, NotificationType

class Main:
    
    @staticmethod
    def build():
        notifification_provider = NotificationFactory.get_notification_system(NotificationType.THREAD)
        return BillService(notifification_provider)

