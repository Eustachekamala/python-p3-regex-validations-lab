import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = re.compile(r"[A-Z][a-zA-Z-']*(?: [A-Z][a-zA-Z-']*)*")
name_regex = re.compile(name)

phone_number = r"\(\d{3}\) \d{3}-\d{4}"
phone_regex = re.compile(phone_number)

email_address = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
email_regex = re.compile(email_address)

# # Test function
# def test_matches_anya_taylor_joy():
#     '''Matches the string "Anya Taylor-Joy".'''
#     assert name_regex.fullmatch("Anya Taylor-Joy")

# # Additional test functions
# def test_matches_phone_number():
#     '''Matches a phone number in the format (123) 456-7890.'''
#     assert phone_regex.fullmatch("(123) 456-7890")

# def test_matches_email_address():
#     '''Matches an email address.'''
#     assert email_regex.fullmatch("example@example.com")
    


# ## TESTS

# test_matches_anya_taylor_joy()
# test_matches_phone_number()
# test_matches_email_address()

