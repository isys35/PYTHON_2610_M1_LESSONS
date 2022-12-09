from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Email(Notification):

    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send {message} to {self.email}')


class SMS(Notification):

    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send {message} to {self.phone}')


class NotificationManager:

    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == '__main__':
    notification_manager = NotificationManager(SMS("jonh@test.ru"))
    notification_manager.send("Hello")
