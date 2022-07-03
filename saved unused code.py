def set_pw_to_current(self, current_pw):
    self.__password = current_pw


def set_password(self):
    new_pass_1 = '1'
    new_pass_2 = '2'
    if input("Old password: ") == self.__password:
        while new_pass_1 != new_pass_2:
            new_pass_1 = input("New password: ")
            new_pass_2 = input("Confirm new password: ")
            if new_pass_1 != new_pass_2:
                print("Passwords do not match")
        self.__password = new_pass_1
    else:
        print("Please contact customer support for help resetting your password")
