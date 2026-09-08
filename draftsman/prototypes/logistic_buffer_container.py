# logistic_buffer_container.py

from draftsman.classes.entity import Entity
from draftsman.classes.mixins import (
    LogisticModeOfOperationMixin,
    CircuitConditionMixin,
    CircuitEnableMixin,
    CircuitSplitIOMixin,
    CircuitConnectableMixin,
    RequestFiltersMixin,
    InventoryMixin,
)
from draftsman.serialization import draftsman_converters

from draftsman.data.entities import logistic_buffer_containers

import attrs


@attrs.define
class LogisticBufferContainer(
    InventoryMixin,
    LogisticModeOfOperationMixin,
    CircuitConditionMixin,
    CircuitEnableMixin,
    CircuitSplitIOMixin,
    CircuitConnectableMixin,
    RequestFiltersMixin,
    Entity,
):
    """
    A logistics container that requests items on a secondary priority.
    """

    @property
    def similar_entities(self) -> list[str]:
        return logistic_buffer_containers

    # =========================================================================

    __hash__ = Entity.__hash__


draftsman_converters.get_version((1, 0)).add_hook_fns(
    LogisticBufferContainer,
    lambda fields: {},
    subclasses_to_ignore=[CircuitEnableMixin, CircuitConditionMixin],
)

draftsman_converters.get_version((2, 0)).add_hook_fns(
    LogisticBufferContainer,
    lambda fields: {},
)
