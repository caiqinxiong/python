import abc


class Person(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def talk(self):
        print('talk')

class China(Person):

    def talk(self):
        pass

p = China()


class Person():

    def talk(self):
        raise NotImplementedError('talk must be Implemented')

class China(Person):
    pass

p = China()
p.talk()
