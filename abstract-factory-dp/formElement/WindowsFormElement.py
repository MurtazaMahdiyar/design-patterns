from .FormElement import FormInput, FormAlert, FormButton


class WinFormInput(FormInput):

    def desc(self):
        print('windows form input.')


class WinFormAlert(FormAlert):

    def desc(self):
        print('windows form alert.')


class WinFormButton(FormButton):

    def desc(self):
        print('windows form button.')
