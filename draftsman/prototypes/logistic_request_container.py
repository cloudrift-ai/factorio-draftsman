# logistic_request_container.py

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
from draftsman.validators import instance_of

from draftsman.data.entities import logistic_request_containers

import attrs


@attrs.define
class LogisticRequestContainer(
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
    A logistics container that requests items with a primary priority.
    """

    @property
    def similar_entities(self) -> list[str]:
        return logistic_request_containers

    # =========================================================================

    # TODO: should be evolve
    request_from_buffers: bool = attrs.field(
        default=False,
        validator=instance_of(bool),
    )

    # =========================================================================

    __hash__ = Entity.__hash__


draftsman_converters.get_version((1, 0)).add_hook_fns(
    LogisticRequestContainer,
    lambda fields: {},
    subclasses_to_ignore=[CircuitEnableMixin, CircuitConditionMixin],
)

draftsman_converters.get_version((2, 0)).add_hook_fns(
    LogisticRequestContainer,
    lambda fields: {},
)
