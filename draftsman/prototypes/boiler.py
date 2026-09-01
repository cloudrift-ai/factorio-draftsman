# boiler.py

from draftsman.classes.entity import Entity
from draftsman.classes.mixins import (
    EnergySourceMixin,
    LogisticConditionMixin,
    CircuitConditionMixin,
    CircuitEnableMixin,
    CircuitSplitOutputMixin,
    CircuitSplitInputMixin,
    CircuitConnectableMixin,
    DirectionalMixin,
)
from draftsman.validators import instance_of

from draftsman.data.entities import boilers

import attrs
from typing import Optional


@attrs.define
class Boiler(
    EnergySourceMixin,
    LogisticConditionMixin,
    CircuitConditionMixin,
    CircuitEnableMixin,
    CircuitSplitOutputMixin,
    CircuitSplitInputMixin,
    CircuitConnectableMixin,
    DirectionalMixin,
    Entity,
):
    """
    An entity that uses a fuel to convert a fluid (usually water) to another
    fluid (usually steam).
    """

    # TODO: ensure fuel requests to this entity match it's allowed fuel categories

    @property
    def similar_entities(self) -> list[str]:
        return boilers

    # =========================================================================

    read_fuel: Optional[bool] = attrs.field(
        default = False,
        validator=instance_of(Optional[bool])
    )
    """
    .. serialized::
    
        This attribute is imported/exported from blueprint strings.

    Whether or not this entity should broadcast its current fuel level to the
    configured output circuit wires.

    .. versionadded:: 4.0.0 (Factorio 2.1)
    """

    # =========================================================================

    __hash__ = Entity.__hash__
