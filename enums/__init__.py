"""A python package which contains all enumerations used in this service"""
from enum import Enum


class GENESISOnlineLanguage(str, Enum):
    """
    An enumeration which contains the languages which may be used in the GENESIS database
    """

    ENGLISH = 'en'
    """English/Englisch"""

    GERMAN = 'de'
    """German/Deutsch"""
