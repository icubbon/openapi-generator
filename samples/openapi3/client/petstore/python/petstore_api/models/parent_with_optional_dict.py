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


from typing import Dict, Optional
from pydantic import BaseModel, Field
from petstore_api.models.inner_dict_with_property import InnerDictWithProperty

class ParentWithOptionalDict(BaseModel):
    """
    ParentWithOptionalDict
    """
    optional_dict: Optional[Dict[str, InnerDictWithProperty]] = Field(None, alias="optionalDict")
    additional_properties: Dict[str, Any] = {}
    __properties = ["optionalDict"]

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
    def from_json(cls, json_str: str) -> ParentWithOptionalDict:
        """Create an instance of ParentWithOptionalDict from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in optional_dict (dict)
        _field_dict = {}
        if self.optional_dict:
            for _key in self.optional_dict:
                if self.optional_dict[_key]:
                    _field_dict[_key] = self.optional_dict[_key].to_dict()
            _dict['optionalDict'] = _field_dict
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParentWithOptionalDict:
        """Create an instance of ParentWithOptionalDict from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParentWithOptionalDict.parse_obj(obj)

        _obj = ParentWithOptionalDict.parse_obj({
            "optional_dict": dict(
                (_k, InnerDictWithProperty.from_dict(_v))
                for _k, _v in obj.get("optionalDict").items()
            )
            if obj.get("optionalDict") is not None
            else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


