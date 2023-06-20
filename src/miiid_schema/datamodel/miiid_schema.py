# Auto generated from miiid_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-06-20T17:04:30
# Schema: miiid-schema
#
# id: https://w3id.org/FAIR-MI/miiid-schema
# description: Minimal Information about Intermicrobial Interaction Data schema
# license: GNU GPL v3.0

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'https://www.wikidata.org/prop/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MIIID = CurieNamespace('miiid', 'https://w3id.org/FAIR-MI/miiid/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = MIIID


# Types
class NCBITaxId(int):
    """ Numeric identifier following the NCBI Taxonomy schema. """
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "NCBITaxId"
    type_model_uri = MIIID.NCBITaxId


# Class references
class NamedThingId(URIorCURIE):
    pass


class IntermicrobialInteractionId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = MIIID.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class IntermicrobialInteraction(NamedThing):
    """
    Represents an interaction between microbial entities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIIID.IntermicrobialInteraction
    class_class_curie: ClassVar[str] = "miiid:IntermicrobialInteraction"
    class_name: ClassVar[str] = "IntermicrobialInteraction"
    class_model_uri: ClassVar[URIRef] = MIIID.IntermicrobialInteraction

    id: Union[str, IntermicrobialInteractionId] = None
    participants: Union[str, List[str]] = None
    tax_id: Union[int, List[int]] = None
    evidence_type: str = None
    reference: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntermicrobialInteractionId):
            self.id = IntermicrobialInteractionId(self.id)

        if self._is_empty(self.participants):
            self.MissingRequiredField("participants")
        if not isinstance(self.participants, list):
            self.participants = [self.participants] if self.participants is not None else []
        self.participants = [v if isinstance(v, str) else str(v) for v in self.participants]

        if self._is_empty(self.tax_id):
            self.MissingRequiredField("tax_id")
        if not isinstance(self.tax_id, list):
            self.tax_id = [self.tax_id] if self.tax_id is not None else []
        self.tax_id = [v if isinstance(v, int) else int(v) for v in self.tax_id]

        if self._is_empty(self.evidence_type):
            self.MissingRequiredField("evidence_type")
        if not isinstance(self.evidence_type, str):
            self.evidence_type = str(self.evidence_type)

        if self._is_empty(self.reference):
            self.MissingRequiredField("reference")
        if not isinstance(self.reference, str):
            self.reference = str(self.reference)

        super().__post_init__(**kwargs)


@dataclass
class IntermicrobialInteractionCollection(YAMLRoot):
    """
    A holder for IntermicrobialInteraction objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIIID.IntermicrobialInteractionCollection
    class_class_curie: ClassVar[str] = "miiid:IntermicrobialInteractionCollection"
    class_name: ClassVar[str] = "IntermicrobialInteractionCollection"
    class_model_uri: ClassVar[URIRef] = MIIID.IntermicrobialInteractionCollection

    entries: Optional[Union[Dict[Union[str, IntermicrobialInteractionId], Union[dict, IntermicrobialInteraction]], List[Union[dict, IntermicrobialInteraction]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=IntermicrobialInteraction, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=MIIID.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=MIIID.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=MIIID.description, domain=None, range=Optional[str])

slots.participants = Slot(uri=MIIID.participants, name="participants", curie=MIIID.curie('participants'),
                   model_uri=MIIID.participants, domain=None, range=Union[str, List[str]])

slots.tax_id = Slot(uri=MIIID.tax_id, name="tax_id", curie=MIIID.curie('tax_id'),
                   model_uri=MIIID.tax_id, domain=None, range=Union[int, List[int]])

slots.evidence_type = Slot(uri=MIIID.evidence_type, name="evidence_type", curie=MIIID.curie('evidence_type'),
                   model_uri=MIIID.evidence_type, domain=None, range=str)

slots.reference = Slot(uri=MIIID.reference, name="reference", curie=MIIID.curie('reference'),
                   model_uri=MIIID.reference, domain=None, range=str)

slots.intermicrobialInteractionCollection__entries = Slot(uri=MIIID.entries, name="intermicrobialInteractionCollection__entries", curie=MIIID.curie('entries'),
                   model_uri=MIIID.intermicrobialInteractionCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, IntermicrobialInteractionId], Union[dict, IntermicrobialInteraction]], List[Union[dict, IntermicrobialInteraction]]]])