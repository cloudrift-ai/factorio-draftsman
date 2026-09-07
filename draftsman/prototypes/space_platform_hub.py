# space_platform_hub.py

from draftsman.classes.entity import Entity
from draftsman.classes.mixins import (
    RequestFiltersMixin,
    CircuitSplitIOMixin,
    CircuitConnectableMixin,
)
from draftsman.serialization import draftsman_converters
from draftsman.signatures import SignalID
from draftsman.validators import instance_of

from draftsman.data.entities import space_platform_hubs

import attrs

from typing import Optional


@attrs.define
class SpacePlatformHub(
    RequestFiltersMixin, CircuitSplitIOMixin, CircuitConnectableMixin, Entity
):
    """
    .. versionadded:: 3.0.0 (Factorio 2.0)

    Main control center of space platforms.
    """

    @property
    def similar_entities(self) -> list[str]:
        return space_platform_hubs

    # =========================================================================

    set_requests: bool = attrs.field(default=False, validator=instance_of(bool))
    """
    Whether or not this space platform should set it's requests dynamically via
    its circuit network input wires.

    .. versionadded:: 4.0.0 (Factorio 2.1)
    """

    # =========================================================================

    read_contents: bool = attrs.field(default=True, validator=instance_of(bool))
    """
    Whether or not to broadcast the contents of the hub to any connected circuit
    network.
    """

    # =========================================================================

    send_to_platform: bool = attrs.field(default=True, validator=instance_of(bool))
    """
    Whether or not to send the contents of the circuit network to the platform 
    for determining it's circuit conditions.
    """

    # =========================================================================

    read_moving_from: bool = attrs.field(default=False, validator=instance_of(bool))
    """
    Whether or not to send the planet the platform is currently moving from to 
    the connected circuit network.
    """

    # =========================================================================

    read_moving_to: bool = attrs.field(default=False, validator=instance_of(bool))
    """
    Whether or not to send the planet the platform is currently moving to to the 
    connected circuit network.
    """

    # =========================================================================

    read_speed: bool = attrs.field(default=False, validator=instance_of(bool))
    """
    Whether or not to output the platforms current speed to the connected 
    circuit network.
    """

    # =========================================================================

    speed_signal: Optional[SignalID] = attrs.field(
        factory=lambda: SignalID(name="signal-V", type="virtual"),
        converter=SignalID.converter,
        validator=instance_of(Optional[SignalID]),
    )
    """
    The signal to output the speed of the platform's current speed, if 
    configured to do so.
    """

    # =========================================================================

    read_damage_taken: bool = attrs.field(default=False, validator=instance_of(bool))
    """
    Whether or not to output the total amount of damage this platform has taken
    (since it started moving) to the connected circuit network.
    """

    # =========================================================================

    damage_taken_signal: Optional[SignalID] = attrs.field(
        factory=lambda: SignalID(name="signal-D", type="virtual"),
        converter=SignalID.converter,
        validator=instance_of(Optional[SignalID]),
    )
    """
    The signal to output the total amount of damage taken, if configured to do
    so.
    """

    # =========================================================================

    request_missing_construction_materials: bool = attrs.field(
        default=True, validator=instance_of(bool)
    )
    """
    Whether or not to automatically request construction materials from 
    configured surfaces the platform is stationed above.
    """

    # =========================================================================

    provide_to_other_platforms: bool = attrs.field(
        default=False, validator=instance_of(bool)
    )
    """
    Whether or not this platform should satisfy the requests of other platforms
    in orbit if it's own requests for that item are sufficient.

    .. versionadded:: 4.0.0 (Factorio 2.1)
    """

    # =========================================================================

    __hash__ = Entity.__hash__


draftsman_converters.get_version((2, 0)).add_hook_fns(
    SpacePlatformHub,
    lambda fields: {
        ("control_behavior", "read_contents"): fields.read_contents.name,
        ("control_behavior", "send_to_platform"): fields.send_to_platform.name,
        ("control_behavior", "read_moving_from"): fields.read_moving_from.name,
        ("control_behavior", "read_moving_to"): fields.read_moving_to.name,
        ("control_behavior", "read_speed"): fields.read_speed.name,
        ("control_behavior", "speed_signal"): fields.speed_signal.name,
        ("control_behavior", "read_damage_taken"): fields.read_damage_taken.name,
        ("control_behavior", "damage_taken_signal"): fields.damage_taken_signal.name,
        "request_missing_construction_materials": fields.request_missing_construction_materials.name,
    },
)

draftsman_converters.get_version((2, 1)).add_hook_fns(
    SpacePlatformHub,
    lambda fields: {
        ("control_behavior", "set_requests"): fields.set_requests.name,
        ("control_behavior", "read_contents"): fields.read_contents.name,
        ("control_behavior", "send_to_platform"): fields.send_to_platform.name,
        ("control_behavior", "read_moving_from"): fields.read_moving_from.name,
        ("control_behavior", "read_moving_to"): fields.read_moving_to.name,
        ("control_behavior", "read_speed"): fields.read_speed.name,
        ("control_behavior", "speed_signal"): fields.speed_signal.name,
        ("control_behavior", "read_damage_taken"): fields.read_damage_taken.name,
        ("control_behavior", "damage_taken_signal"): fields.damage_taken_signal.name,
        "request_missing_construction_materials": fields.request_missing_construction_materials.name,
        "providing_to_other_platforms": fields.provide_to_other_platforms.name,
    },
)
