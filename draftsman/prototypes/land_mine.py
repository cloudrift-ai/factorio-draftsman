# land_mine.py

from draftsman.classes.entity import Entity
from draftsman.classes.mixins import CircuitConditionMixin, CircuitEnableMixin, CircuitConnectableMixin

from draftsman.data.entities import land_mines

import attrs


@attrs.define
class LandMine(CircuitConditionMixin, CircuitEnableMixin, CircuitConnectableMixin, Entity):
    """
    An entity that explodes when in proximity to another force.
    """

    @property
    def similar_entities(self) -> list[str]:
        return land_mines

    # =========================================================================

    __hash__ = Entity.__hash__

# TODO: write custom hook that only allows land mines to be circuit connectable post Factorio 2.1