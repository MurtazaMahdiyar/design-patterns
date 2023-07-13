from .FormElement import FormInput, FormAlert, FormButton


class MacFormInput(FormInput):

    def desc(self):
        print('MacOS form input.')


class MacFormAlert(FormAlert):

    def desc(self):
        print('MacOS form alert.')


class MacFormButton(FormButton):

    def desc(self):
        print('MacOS form button.')
