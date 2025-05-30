# coding: utf-8

"""
    Algod REST API.

    API endpoint for algod operations.

    The version of the OpenAPI document: 0.0.1
    Contact: contact@algorand.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from algokit_algod_api.models.simulate_request_transaction_group import SimulateRequestTransactionGroup
from algokit_algod_api.models.simulate_trace_config import SimulateTraceConfig
from typing import Optional, Set
from typing_extensions import Self

class SimulateRequest(BaseModel):
    """
    Request type for simulation endpoint.
    """ # noqa: E501
    txn_groups: List[SimulateRequestTransactionGroup] = Field(description="The transaction groups to simulate.", alias="txn-groups")
    round: Optional[StrictInt] = Field(default=None, description="If provided, specifies the round preceding the simulation. State changes through this round will be used to run this simulation. Usually only the 4 most recent rounds will be available (controlled by the node config value MaxAcctLookback). If not specified, defaults to the latest available round.")
    allow_empty_signatures: Optional[StrictBool] = Field(default=None, description="Allows transactions without signatures to be simulated as if they had correct signatures.", alias="allow-empty-signatures")
    allow_more_logging: Optional[StrictBool] = Field(default=None, description="Lifts limits on log opcode usage during simulation.", alias="allow-more-logging")
    allow_unnamed_resources: Optional[StrictBool] = Field(default=None, description="Allows access to unnamed resources during simulation.", alias="allow-unnamed-resources")
    extra_opcode_budget: Optional[StrictInt] = Field(default=None, description="Applies extra opcode budget during simulation for each transaction group.", alias="extra-opcode-budget")
    exec_trace_config: Optional[SimulateTraceConfig] = Field(default=None, alias="exec-trace-config")
    fix_signers: Optional[StrictBool] = Field(default=None, description="If true, signers for transactions that are missing signatures will be fixed during evaluation.", alias="fix-signers")
    __properties: ClassVar[List[str]] = ["txn-groups", "round", "allow-empty-signatures", "allow-more-logging", "allow-unnamed-resources", "extra-opcode-budget", "exec-trace-config", "fix-signers"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SimulateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in txn_groups (list)
        _items = []
        if self.txn_groups:
            for _item_txn_groups in self.txn_groups:
                if _item_txn_groups:
                    _items.append(_item_txn_groups.to_dict())
            _dict['txn-groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of exec_trace_config
        if self.exec_trace_config:
            _dict['exec-trace-config'] = self.exec_trace_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SimulateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "txn-groups": [SimulateRequestTransactionGroup.from_dict(_item) for _item in obj["txn-groups"]] if obj.get("txn-groups") is not None else None,
            "round": obj.get("round"),
            "allow-empty-signatures": obj.get("allow-empty-signatures"),
            "allow-more-logging": obj.get("allow-more-logging"),
            "allow-unnamed-resources": obj.get("allow-unnamed-resources"),
            "extra-opcode-budget": obj.get("extra-opcode-budget"),
            "exec-trace-config": SimulateTraceConfig.from_dict(obj["exec-trace-config"]) if obj.get("exec-trace-config") is not None else None,
            "fix-signers": obj.get("fix-signers")
        })
        return _obj


