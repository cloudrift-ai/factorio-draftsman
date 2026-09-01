# agricultural_tower.py

from draftsman.classes.entity import Entity
from draftsman.classes.mixins import (
    CircuitConditionMixin,
    CircuitEnableMixin,
    LogisticConditionMixin,
    ControlBehaviorMixin,
    CircuitConnectableMixin,
    EnergySourceMixin,
)
from draftsman.serialization import draftsman_converters
from draftsman.signatures import Condition
from draftsman.validators import instance_of

from draftsman.data.entities import agricultural_towers

import attrs
from typing import Optional


@attrs.define
class AgriculturalTower(
    LogisticConditionMixin,
    CircuitConditionMixin,
    CircuitEnableMixin,
    ControlBehaviorMixin,
    CircuitConnectableMixin,
    EnergySourceMixin,
    Entity,
):
    """
    .. versionadded:: 3.0.0 (Factorio 2.0)

    An entity that can plant and harvest growables.
    """

    @property
    def similar_entities(self) -> list[str]:
        return agricultural_towers

    # =========================================================================

    enable_harvesting_condition: bool = attrs.field(
        default=False, validator=instance_of(bool)
    )
    """
    .. serialized::
    
        This attribute is imported/exported from blueprint strings.

    Whether or not this tower should check :py:attr:`.harvesting_condition` to
    determine whether or not it should harvest mature crops.

    .. versionadded:: 4.0.0 (Factorio 2.1)
    """

    harvesting_condition: Optional[Condition] = attrs.field(
        factory=Condition,
        converter=Condition.converter,
        validator=instance_of(Optional[Condition]),
    )
    """
    .. serialized::
    
        This attribute is imported/exported from blueprint strings.

    The condition that must be true in order for this tower to harvest crops, if
    :py:attr:`.enable_harvesting_condition` is ``True``.

    .. versionadded:: 4.0.0 (Factorio 2.1)
    """

    enable_planting_condition: bool = attrs.field(
        default=False, validator=instance_of(bool)
    )
    """
    .. serialized::
    
        This attribute is imported/exported from blueprint strings.

    Whether or not this tower should check :py:attr:`.planting_condition` to
    determine whether or not it should harvest mature crops.

    .. versionadded:: 4.0.0 (Factorio 2.1)
    """

    planting_condition: Optional[Condition] = attrs.field(
        factory=Condition,
        converter=Condition.converter,
        validator=instance_of(Optional[Condition]),
    )
    """
    .. serialized::
    
        This attribute is imported/exported from blueprint strings.

    The condition that must be true in order for this tower to plant crops, if
    :py:attr:`.enable_planting_condition` is ``True``.

    .. versionadded:: 4.0.0 (Factorio 2.1)
    """

    read_contents: bool = attrs.field(default=False, validator=instance_of(bool))
    """
    .. serialized::

        This attribute is imported/exported from blueprint strings.

    Whether or not to broadcast the entities inside of this tower's inventory to
    any connected circuit network.
    """

    # =========================================================================

    __hash__ = Entity.__hash__


draftsman_converters.get_version((2, 0)).add_hook_fns(
    AgriculturalTower,
    lambda fields: {("control_behavior", "read_contents"): fields.read_contents.name},
)

draftsman_converters.get_version((2, 1)).add_hook_fns(
    AgriculturalTower,
    lambda fields: {
        (
            "control_behavior",
            "enable_harvesting_condition",
        ): fields.enable_harvesting_condition.name,
        ("control_behavior", "harvesting_condition"): fields.harvesting_condition.name,
        (
            "control_behavior",
            "enable_planting_condition",
        ): fields.enable_planting_condition.name,
        ("control_behavior", "planting_condition"): fields.planting_condition.name,
        ("control_behavior", "read_contents"): fields.read_contents.name,
    },
)
