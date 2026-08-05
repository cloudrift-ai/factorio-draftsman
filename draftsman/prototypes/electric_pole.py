# electric_pole.py

from draftsman.classes.entity import Entity
from draftsman.classes.mixins import CircuitConnectableMixin, PowerConnectableMixin
from draftsman.data import entities, qualities

from draftsman.data.entities import electric_poles
from draftsman.utils import AABB

import attrs


@attrs.define
class ElectricPole(CircuitConnectableMixin, PowerConnectableMixin, Entity):
    """
    An entity used to distribute electrical energy as a network.
    """

    @property
    def similar_entities(self) -> list[str]:
        return electric_poles

    # =========================================================================

    @property
    def circuit_wire_max_distance(self) -> float:
        # Electric poles use a custom key (for some reason)
        wire_max_dist = entities.raw.get(self.name, {}).get(
            "maximum_wire_distance", None
        )
        if wire_max_dist is None:
            return None
        buff = 2 * qualities.raw.get(self.quality, {"level": 0})["level"]
        return wire_max_dist + buff

    # =========================================================================

    @property
    def supply_area_distance(self) -> float:
        """
        The "radius" of this pole's supply area, in tiles, adjusted for quality.

        This is *half* of the supply area shown in the item tooltip: a medium
        electric pole's ``3.5`` describes a 7x7 square. Each quality level adds
        one tile of radius, so a legendary small pole (quality level 5, not 4)
        covers 15x15 rather than its base 5x5.

        Returns ``None`` if the prototype is unknown.

        :type: ``float``
        """
        base = entities.raw.get(self.name, {}).get("supply_area_distance", None)
        if base is None:
            return None
        return base + qualities.raw.get(self.quality, {"level": 0})["level"]

    # =========================================================================

    def get_world_supply_area(self) -> AABB:
        """
        The region this pole powers, in world-space coordinates.

        Unlike :py:meth:`.get_world_bounding_box`, this is not a collision
        volume; it is the square centered on the pole in which entities receive
        power. Use it to answer whether a given entity is covered:

        .. doctest::

            >>> from draftsman.entity import ElectricPole, Inserter
            >>> from draftsman.utils import aabb_overlaps_aabb
            >>> pole = ElectricPole("medium-electric-pole", tile_position=(0, 0))
            >>> inserter = Inserter("inserter", tile_position=(3, 0))
            >>> aabb_overlaps_aabb(pole.get_world_supply_area(), inserter.get_world_bounding_box())
            True

        Returns ``None`` if the prototype is unknown.

        :type: :py:class:`.AABB`
        """
        distance = self.supply_area_distance
        if distance is None:
            return None
        x, y = self.global_position.x, self.global_position.y
        return AABB(x - distance, y - distance, x + distance, y + distance)

    # =========================================================================

    __hash__ = Entity.__hash__
