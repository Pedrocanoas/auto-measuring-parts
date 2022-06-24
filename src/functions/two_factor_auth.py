import pyotp


def generate_token_google_auth():
    base32secret = pyotp.random_base32()
    print(f"Your token:{base32secret}")

    provi_uri = pyotp.totp.TOTP(base32secret)
    provi_uri.provisioning_uri(
        name="SAIQ",
        issuer_name="Secure App"
    )

def check_two_factor_auth(entry_code):
    tokens = [
        "JTB4HZNR25ORG5Y42NXM6QMMOS2SH5OQ"
    ]
    for token in tokens:
        totp = pyotp.TOTP(token)
        code_google_auth = totp.now()
        if int(entry_code) == int(code_google_auth):
            return True
        return False
