"""Pydantic models"""
from pydantic import BaseModel as _BaseModel


class BaseModel(_BaseModel):
    """A modified base model which will hold some global configuration values"""

    class Config:
        """The configuration of the base model"""

        allow_population_by_field_name = True
        """A Field with an alias may also be populated by its field name"""

        arbitrary_types_allowed = True
        """Allow arbitrary user defined types"""
