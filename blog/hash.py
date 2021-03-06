from passlib.context import CryptContext


pass_context = CryptContext(schemes=["bcrypt"],deprecated="auto")


class Hash():
    def encrypt_bcrypt(password: str):
        hased_Password = pass_context.hash(password) #hasinng the password using passlib lib
        return hased_Password

    def verify(plain_password,hased_Password):
        verify_Password = pass_context.verify(plain_password,hased_Password) #verify the password
        return verify_Password
