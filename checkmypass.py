import requests
import hashlib
import sys


def request_api_data(query_char):
    url = f"http://api.pwnedpasswords.com/range/{query_char}"
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {res.status_code}, check the api and try again."
        )
    return res


def hash_sha1(password):
    encoded_pass = password.encode("utf-8")
    sha1pass = hashlib.sha1(encoded_pass).hexdigest()
    return sha1pass.upper()


def split_hash(hash):
    return hash[:5], hash[5:]


def get_leaked_passwords_counter(response):
    response_lines = response.text.splitlines()
    return (line.split(":") for line in response_lines)


def check_my_password(my_password, leaked_passwords):
    for leak_password, count in leaked_passwords:
        if my_password == leak_password:
            return count
    return 0


def read_passwords_from_files(path):
    passwords = set()
    for document in path:
        with open(document, "r") as file:
            raw_passwords = file.read()
            passwords.update(raw_passwords.splitlines())
    return passwords


def main(args):
    passwords = read_passwords_from_files(args)
    for password in passwords:
        hashed_pass = hash_sha1(password)
        head, tail = split_hash(hashed_pass)
        res = request_api_data(head)
        leaked_passwords = get_leaked_passwords_counter(res)
        count = check_my_password(tail, leaked_passwords)
        if count:
            print(
                f"The password {password} was found {count} on the leaked password database! You should not use this password!"
            )
        else:
            print(
                f"The password {password} was NOT found on leaked password database. You can use that!"
            )
    return "done!"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
