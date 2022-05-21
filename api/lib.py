from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from service.jwt_bearer import\
    get_id_from_jwt, \
    JWTBearer, \
    validate_authority, \
    PasswordHasher, \
    sign_jwt
from service.enigma.enigma_aes import AESCipher
import json
