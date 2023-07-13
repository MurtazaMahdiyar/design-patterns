from watchable import Watchable
from watcher import Watcher


if __name__ == "__main__":

    o1 = Watcher('O-1')
    o2 = Watcher('O-2')

    email = Watchable()

    email.add(o1)
    email.add(o2)

    email.data = 'sample_email@gmail.com'
    print('----------')
    email.data = 'email_sample@gmail.com'
