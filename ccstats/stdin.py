import getpass

class stdInput:

    @staticmethod
    def ask_info(name, default=None, pwd=False):
        if pwd:
            res = stdInput.get_password()
        else:
            res = raw_input("%s %s:" % (name, stdInput.get_default(default)) ) \
                    or default
        return res

    @staticmethod
    def get_password():
        pprompt = lambda: (getpass.getpass(),
                           getpass.getpass('Retype password:'))
        db_p1, db_p2 = pprompt()
        while db_p1 != db_p2:
            print('Passwords do not match. Try again')
            db_p1, db_p2 = pprompt()
        return db_p1

    @staticmethod
    def get_default(name):
        if not name:
            return ""
        else:
            return "[" + str(name) + "]"
