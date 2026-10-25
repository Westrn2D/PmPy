import getpass , keyring
def Setup():
    SERVICE = "PmPy"
    USER = getpass.getuser()


    pin = getpass.getpass("Set PIN: ")
    keyring.set_password(SERVICE, USER, pin)
    pin = None
