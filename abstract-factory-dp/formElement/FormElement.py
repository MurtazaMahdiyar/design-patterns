from abc import ABC, abstractmethod


class FormElement(ABC):

    @abstractmethod
    def desc(self):
        pass


class FormInput(FormElement, ABC):
    pass


class FormButton(FormElement, ABC):
    pass


class FormAlert(FormElement, ABC):
    pass
