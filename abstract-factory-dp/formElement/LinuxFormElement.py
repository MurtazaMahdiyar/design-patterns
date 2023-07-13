from .FormElement import FormInput, FormAlert, FormButton


class LinuxFormInput(FormInput):

    def desc(self):
        print('linux form input.')


class LinuxFormAlert(FormAlert):

    def desc(self):
        print('linux form alert.')


class LinuxFormButton(FormButton):

    def desc(self):
        print('linux form button.')
