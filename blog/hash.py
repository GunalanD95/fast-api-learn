from passlib.context import CryptContext


pass_context = CryptContext(schemes=["bcrypt"],deprecated="auto")


class Hash():
    def encrypt_bcrypt(password: str):
        hased_Password = pass_context.hash(password) #hasinng the password using passlib lib
        return hased_Password