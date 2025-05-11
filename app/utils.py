from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated
import os

# Add these imports at the top of your file
security = HTTPBasic()

# Create a function to verify credentials
async def verify_credentials(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    # In a real application, you would check these against a database
    correct_username = os.getenv("USERNAME")
    correct_password = os.getenv("PASSWORD")
    
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username