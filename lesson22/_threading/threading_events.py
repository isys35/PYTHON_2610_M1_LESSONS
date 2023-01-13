import logging
import threading
import time


def wait_for_event(event):
    """Дождаться установки события, прежде чем что-то делать."""
    logging.debug('wait_for_event starting')
    event_is_set = event.wait()
    logging.debug('event set: %s', event_is_set)


def wait_for_event_timeout(event, timeout):
    """Подождать t секунд и завершиться по тайм-ауту."""
    while not event.is_set():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = event.wait(timeout)
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')



logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

event = threading.Event()

tl = threading.Thread(
    name='block',
    target=wait_for_event,
    args=(event,),
)
tl.start()

t2 = threading.Thread(
    name='nonblock',
    target=wait_for_event_timeout,
    args=(event, 2),
)
t2.start()

logging.debug('Waiting before calling Event.set()')
time.sleep(0.3)
event.set()
logging.debug('Event is set')
