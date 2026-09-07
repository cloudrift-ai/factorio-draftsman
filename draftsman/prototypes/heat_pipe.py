# heat_pipe.py

from draftsman.classes.entity import Entity
from draftsman.classes.mixins import (
    CircuitReadTemperatureMixin,
    CircuitSplitIOMixin,
    CircuitConnectableMixin,
)

from draftsman.data.entities import heat_pipes

import attrs


@attrs.define
class HeatPipe(
    CircuitReadTemperatureMixin,
    CircuitSplitIOMixin,
    CircuitConnectableMixin,
    Entity,
):
    """
    An entity used to transfer thermal energy.
    """

    @property
    def similar_entities(self) -> list[str]:
        return heat_pipes

    # =========================================================================

    __hash__ = Entity.__hash__
