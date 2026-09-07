# ammo_turret.py

from draftsman.classes.entity import Entity
from draftsman.classes.mixins import (
    ReadAmmoMixin,
    TargetPrioritiesMixin,
    CircuitConditionMixin,
    LogisticConditionMixin,
    CircuitEnableMixin,
    CircuitSplitIOMixin,
    CircuitConnectableMixin,
    EnergySourceMixin,
    DirectionalMixin,
)

from draftsman.data.entities import ammo_turrets

import attrs


@attrs.define
class AmmoTurret(
    ReadAmmoMixin,
    TargetPrioritiesMixin,
    CircuitConditionMixin,
    LogisticConditionMixin,
    CircuitEnableMixin,
    CircuitSplitIOMixin,
    CircuitConnectableMixin,
    DirectionalMixin,
    EnergySourceMixin,
    Entity,
):
    """
    An entity that automatically targets and attacks other forces within range.
    Consumes item-based ammunition.
    """

    # TODO: validate item_requests match this particular turret type

    @property
    def similar_entities(self) -> list[str]:
        return ammo_turrets

    # =========================================================================

    __hash__ = Entity.__hash__
