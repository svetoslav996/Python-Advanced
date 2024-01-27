class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def validate_email(email):
    try:
        if '@' not in email:
            raise MustContainAtSymbolError("Email must contain @")

        name, domain = email.split('@')

        # Check Name Length
        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")

        # Check Domain
        valid_domains = ['.com', '.bg', '.net', '.org']
        if not any(domain.endswith(d) for d in valid_domains):
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

        print("Email is valid")

    except MustContainAtSymbolError as e:
        print(f"Traceback (most recent call last):\n  {e.__class__.__name__}: {str(e)}")

    except NameTooShortError as e:
        print(f"Traceback (most recent call last):\n  {e.__class__.__name__}: {str(e)}")

    except InvalidDomainError as e:
        print(f"Traceback (most recent call last):\n  {e.__class__.__name__}: {str(e)}")


# Example usage:
emails = [
    "abc@abv.bg",
    "peter@gmail.com",
    "petergmail.com",
    "peter@gmail.hotmail",
    "john@example.net",
    "alice@yahoo.org",
    "end"
]

for email in emails:
    if email.lower() == "end":
        break
    validate_email(email)
