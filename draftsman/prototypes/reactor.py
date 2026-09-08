# reactor.py

from draftsman.classes.entity import Entity
from draftsman.classes.mixins import (
    CircuitSplitIOMixin,
    CircuitReadTemperatureMixin,
    CircuitConnectableMixin,
    EnergySourceMixin,
)
from draftsman.serialization import draftsman_converters
from draftsman.validators import instance_of

from draftsman.data.entities import reactors

import attrs


@attrs.define
class Reactor(
    CircuitSplitIOMixin,
    CircuitReadTemperatureMixin,
    CircuitConnectableMixin,
    EnergySourceMixin,
    Entity,
):
    """
    An entity that converts a fuel into thermal energy.
    """

    @property
    def similar_entities(self) -> list[str]:
        return reactors

    # =========================================================================

    read_burner_fuel: bool = attrs.field(default=False, validator=instance_of(bool))
    """
    Whether or not to broadcast the amount of fuel currently in the reactor to 
    any connected circuit networks.
    """

    # =========================================================================

    __hash__ = Entity.__hash__


# TODO: need to figure out a way to make 1.0 hook not be circuit connectable

draftsman_converters.get_version((1, 0)).add_hook_fns(
    Reactor, lambda fields: {}, subclasses_to_ignore=[CircuitConnectableMixin]
)

draftsman_converters.get_version((2, 0)).add_hook_fns(
    Reactor,
    lambda fields: {
        ("control_behavior", "read_burner_fuel"): fields.read_burner_fuel.name,
    },
)

draftsman_converters.get_version((2, 1)).add_hook_fns(
    Reactor,
    lambda fields: {
        ("control_behavior", "read_burner_fuel"): fields.read_burner_fuel.name,
    },
)
