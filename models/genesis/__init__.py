"""A package containing the different requests which may be sent to the genesis server"""
from pydantic import Field

from enums import GENESISOnlineLanguage
from models import BaseModel
from settings import GENESISAPISettings


class SimpleGenesisRequest(BaseModel):
    """This class is used for always needed parameters in the requests"""

    username: str = Field(
        default=GENESISAPISettings().username,
        title='GENESIS Online Username',
        description='The username which was issued by the GENESIS Online database via this page'
                    '(https://www-genesis.destatis.de/genesis/online?Menu=Registrierung)',
    )
    """
    GENESIS Online Username

    The username which was issued by the GENESIS Online database during the signup. The signup is 
    possible on the following page: `https://www-genesis.destatis.de/genesis/online?Menu=Registrierung`.
    
    IMPORTANT: If no username is explicitly given, the default value is the value given in the settings
    """

    password: str = Field(
        default=GENESISAPISettings().password.get_secret_value(),
        alias='password',
        title='GENESIS Online Password',
        description='The password used to access the GENESIS Online database. The initial '
                    'password may not be used due to restrictions imposed on the database side',
    )
    """
    GENESIS Online Password

    The password used to access the GENESIS Online database. The initial password received via the
    registration confirmation may not be used here. This is a restriction imposed by the GENESIS 
    Online database. Please change your password beforehand.
    """

    language: GENESISOnlineLanguage = Field(
        default=GENESISAPISettings().language,
        alias='language',
        title='GENESIS Online Language',
        description='The language which is used in responses by the database',
    )
    """
    GENESIS Online Language

    The language used by GENESIS Online in the text fields in the responses.

    Possible values
     - de (German/Deutsch)
     - en (English/Englisch) [default]
    """
