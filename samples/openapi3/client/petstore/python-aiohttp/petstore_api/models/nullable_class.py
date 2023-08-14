# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist

class NullableClass(BaseModel):
    """
    NullableClass
    """
    required_integer_prop: Optional[StrictInt] = Field(...)
    integer_prop: Optional[StrictInt] = None
    number_prop: Optional[float] = None
    boolean_prop: Optional[StrictBool] = None
    string_prop: Optional[StrictStr] = None
    date_prop: Optional[date] = None
    datetime_prop: Optional[datetime] = None
    array_nullable_prop: Optional[conlist(Dict[str, Any])] = None
    array_and_items_nullable_prop: Optional[conlist(Dict[str, Any])] = None
    array_items_nullable: Optional[conlist(Dict[str, Any])] = None
    object_nullable_prop: Optional[Dict[str, Dict[str, Any]]] = None
    object_and_items_nullable_prop: Optional[Dict[str, Dict[str, Any]]] = None
    object_items_nullable: Optional[Dict[str, Dict[str, Any]]] = None
    __properties = ["required_integer_prop", "integer_prop", "number_prop", "boolean_prop", "string_prop", "date_prop", "datetime_prop", "array_nullable_prop", "array_and_items_nullable_prop", "array_items_nullable", "object_nullable_prop", "object_and_items_nullable_prop", "object_items_nullable"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> NullableClass:
        """Create an instance of NullableClass from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if required_integer_prop (nullable) is None
        # and __fields_set__ contains the field
        if self.required_integer_prop is None and "required_integer_prop" in self.__fields_set__:
            _dict['required_integer_prop'] = None

        # set to None if integer_prop (nullable) is None
        # and __fields_set__ contains the field
        if self.integer_prop is None and "integer_prop" in self.__fields_set__:
            _dict['integer_prop'] = None

        # set to None if number_prop (nullable) is None
        # and __fields_set__ contains the field
        if self.number_prop is None and "number_prop" in self.__fields_set__:
            _dict['number_prop'] = None

        # set to None if boolean_prop (nullable) is None
        # and __fields_set__ contains the field
        if self.boolean_prop is None and "boolean_prop" in self.__fields_set__:
            _dict['boolean_prop'] = None

        # set to None if string_prop (nullable) is None
        # and __fields_set__ contains the field
        if self.string_prop is None and "string_prop" in self.__fields_set__:
            _dict['string_prop'] = None

        # set to None if date_prop (nullable) is None
        # and __fields_set__ contains the field
        if self.date_prop is None and "date_prop" in self.__fields_set__:
            _dict['date_prop'] = None

        # set to None if datetime_prop (nullable) is None
        # and __fields_set__ contains the field
        if self.datetime_prop is None and "datetime_prop" in self.__fields_set__:
            _dict['datetime_prop'] = None

        # set to None if array_nullable_prop (nullable) is None
        # and __fields_set__ contains the field
        if self.array_nullable_prop is None and "array_nullable_prop" in self.__fields_set__:
            _dict['array_nullable_prop'] = None

        # set to None if array_and_items_nullable_prop (nullable) is None
        # and __fields_set__ contains the field
        if self.array_and_items_nullable_prop is None and "array_and_items_nullable_prop" in self.__fields_set__:
            _dict['array_and_items_nullable_prop'] = None

        # set to None if object_nullable_prop (nullable) is None
        # and __fields_set__ contains the field
        if self.object_nullable_prop is None and "object_nullable_prop" in self.__fields_set__:
            _dict['object_nullable_prop'] = None

        # set to None if object_and_items_nullable_prop (nullable) is None
        # and __fields_set__ contains the field
        if self.object_and_items_nullable_prop is None and "object_and_items_nullable_prop" in self.__fields_set__:
            _dict['object_and_items_nullable_prop'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NullableClass:
        """Create an instance of NullableClass from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NullableClass.parse_obj(obj)

        _obj = NullableClass.parse_obj({
            "required_integer_prop": obj.get("required_integer_prop"),
            "integer_prop": obj.get("integer_prop"),
            "number_prop": obj.get("number_prop"),
            "boolean_prop": obj.get("boolean_prop"),
            "string_prop": obj.get("string_prop"),
            "date_prop": obj.get("date_prop"),
            "datetime_prop": obj.get("datetime_prop"),
            "array_nullable_prop": obj.get("array_nullable_prop"),
            "array_and_items_nullable_prop": obj.get("array_and_items_nullable_prop"),
            "array_items_nullable": obj.get("array_items_nullable"),
            "object_nullable_prop": obj.get("object_nullable_prop"),
            "object_and_items_nullable_prop": obj.get("object_and_items_nullable_prop"),
            "object_items_nullable": obj.get("object_items_nullable")
        })
        return _obj


