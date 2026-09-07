# pipe.py

from draftsman.classes.entity import Entity
from draftsman.classes.mixins import (
    CircuitReadTemperatureMixin,
    CircuitReadPipeMixin,
    CircuitSplitIOMixin,
    CircuitConnectableMixin,
)

from draftsman.data.entities import pipes

import attrs


@attrs.define
class Pipe(
    CircuitReadTemperatureMixin,
    CircuitReadPipeMixin,
    CircuitSplitIOMixin,
    CircuitConnectableMixin,
    Entity,
):
    """
    A structure that transports a fluid across a surface.
    """

    @property
    def similar_entities(self) -> list[str]:
        return pipes

    # =========================================================================

    __hash__ = Entity.__hash__
