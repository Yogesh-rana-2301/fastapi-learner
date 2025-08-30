from datetime import datetime, timedelta, timezone
from . import oauth2
import jwt
from jwt.exceptions import InvalidTokenError
from . import schema



SECRET_KEY = "f80b0f6440aaa40e90885c7eb14b347f98ed95a0c111e606e6815dfe3cce24d1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15



def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str,credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schema.TokenData(email=email)
    except InvalidTokenError:
        raise credentials_exception