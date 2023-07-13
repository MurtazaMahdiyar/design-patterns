from FormFactories import WindowsFormFactory, LinuxFormFactory, MacOSFormFactory


if __name__ == '__main__':

    formContainer = WindowsFormFactory()

    form = {
        'input': formContainer.getInput(),
        'alert': formContainer.getAlert(),
        'button': formContainer.getButton()
    }

    form['input'].desc()
    form['alert'].desc()
    form['button'].desc()

    formContainer = LinuxFormFactory()

    form = {
        'input': formContainer.getInput(),
        'alert': formContainer.getAlert(),
        'button': formContainer.getButton()
    }

    form['input'].desc()
    form['alert'].desc()
    form['button'].desc()
