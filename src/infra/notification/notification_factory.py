from infra.notification.thread_notification import ThreadedEmailNotification
from enum import Enum


class NotificationType(Enum):
    THREAD=1,
    QUEUE=2,
    STREAM=3


class NotificationFactory:

    @staticmethod
    def get_notification_system( email_notification_enum=NotificationType.THREAD):
        match email_notification_enum:
            case NotificationType.QUEUE:
                # TODO: SOME ASYNC(I.E:QUEUE)
                raise Exception('just to be expressive')
            case _:
                # simulating async enviroment
                return ThreadedEmailNotification()
            