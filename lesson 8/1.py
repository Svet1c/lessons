# task 1
import re


def email_parsing(email):
    re_email = re.compile(r'^([a-z0-9_-]+)*[a-z0-9_-]+@[a-z0-9_-]+\.[a-z]{2,6}$')
    email_checker = re_email.match(email)
    if not email_checker:
        msg = f"wrong email: {email}"
        raise ValueError(msg)
    else:
        username = re.compile(r'^([a-z0-9_-]+)*')
        domain = re.compile(r'[a-z0-9_-]+\.[a-z]{2,6}$')
        return {"Username": username.findall(email)[0], "Domain": domain.findall(email)[0]}


if __name__ == "__main__":
    print(email_parsing('someone@geekbrains.ru'))