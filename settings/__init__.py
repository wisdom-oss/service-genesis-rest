"""Python Package for the different settings which need to be configured"""
from pydantic import BaseSettings, Field

from enums import GENESISOnlineLanguage


class GENESISAPISettings(BaseSettings):
    """
    A Settings class handling the needed information for the access to the GENESIS Online database
    """

    username: str = Field(
        default=...,
        title='GENESIS Online Username',
        description='The username which was issued by the GENESIS Online database via this page'
                    '(https://www-genesis.destatis.de/genesis/online?Menu=Registrierung)',
        env='GENESIS_USER'
    )
    """
    GENESIS Online Username
    
    The username which was issued by the GENESIS Online database during the signup. The signup is 
    possible on the following page: `https://www-genesis.destatis.de/genesis/online?Menu=Registrierung`
    """

    password: str = Field(
        default=...,
        title='GENESIS Online Password',
        description='The password used to access the GENESIS Online database. The initial '
                    'password may not be used due to restrictions imposed on the database side',
        env='GENESIS_PASSWORD'
    )
    """
    GENESIS Online Password
    
    The password used to access the GENESIS Online database. The initial password received via the
    registration confirmation may not be used here. This is a restriction imposed by the GENESIS 
    Online database. Please change your password beforehand.
    """

    language: GENESISOnlineLanguage = Field(
        default=GENESISOnlineLanguage.ENGLISH,
        title='GENESIS Online Language',
        description='The language which is used in responses by the database',
        env='GENESIS_LANGUAGE'
    )
    """
    GENESIS Online Language
    
    The language used by GENESIS Online in the text fields in the responses.
    
    Possible values
     - de (German/Deutsch)
     - en (English/Englisch) [default]
    """


class ServiceRegistrySettings(BaseSettings):
    """
    A settings class used to handle settings for the service registry
    """

    host: str = Field(
        default=...,
        title='Service Registry Host',
        description='The hostname or IP address of the service registry on which this service '
                    'shall register itself',
        env='SERVICE_REGISTRY_HOST'
    )
    """
    Service Registry Host
    
    The hostname or ip address of the service registry which this service uses to register and 
    set its status.
    """

    port: int = Field(
        default=8761,
        title='Service Registry Port',
        description='The port on which the service registry listens on, defaults to 8761',
        env='SERVICE_REGISTRY_PORT'
    )
    """
    Service Registry Port
    
    The port on which the service registry listens on, defaults to `8761`
    """


class ApplicationSettings(BaseSettings):
    """A settings class managing the general settings of the application"""

    name: str = Field(
        default="genesis-rest",
        title='Service Name',
        description='The name under which this service will register itself on the service '
                    'registry',
        env='APPLICATION_NAME'
    )
    """
    Application Name
    
    The name under which this service will register itself on the service registry and under 
    which is it callable via the service registry, defaults to: `genesis-rest`
    """

    port: int = Field(
        default=5000,
        title='Application Port',
        description='The port which will be used for the HTTP binding of this application',
        env='APPLICATION_PORT'
    )
    """
    Application Port
    
    The port which will be bound by the HTTP server for incoming traffic
    """
