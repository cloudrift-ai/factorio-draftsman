# radar.py

from draftsman.classes.entity import Entity
from draftsman.constants import RadarMode
from draftsman.classes.mixins import CircuitConnectableMixin, EnergySourceMixin
from draftsman.serialization import draftsman_converters
from draftsman.signatures import SignalID
from draftsman.validators import instance_of

from draftsman.data.entities import radars

import attrs
from typing import Optional


@attrs.define
class Radar(CircuitConnectableMixin, EnergySourceMixin, Entity):
    """
    An entity that reveals and scans neighbouring chunks.
    """

    @property
    def similar_entities(self) -> list[str]:
        return radars

    # =========================================================================

    mode: RadarMode = attrs.field(
        default=RadarMode.SURFACE, converter=RadarMode, validator=instance_of(RadarMode)
    )
    """
    .. serialized::
        
        This attribute is imported/exported from blueprint strings.
    
    In what manner should circuit signals be propagated across radars.

    .. versionadded:: 4.0.0 (Factorio 2.1)
    """

    universe_channel: Optional[SignalID] = attrs.field(
        default=None,
        converter=SignalID.converter,
        validator=instance_of(Optional[SignalID]),
    )
    """
    .. serialized::
        
        This attribute is imported/exported from blueprint strings.
    
    A signal representing a unique signal frame that this radar will use for 
    reading/writing across all surfaces, if :py:attr:`.mode` is set to
    ``UNIVERSE``.

    .. versionadded:: 4.0.0 (Factorio 2.1)
    """

    # =========================================================================

    __hash__ = Entity.__hash__


draftsman_converters.get_version((2, 0)).add_hook_fns(
    Radar,
    lambda _: {
        ("control_behavior", "mode"): None,
        ("control_behavior", "universe_channel"): None,
    },
)

draftsman_converters.get_version((2, 1)).add_hook_fns(
    Radar,
    lambda fields: {
        ("control_behavior", "mode"): fields.mode.name,
        ("control_behavior", "universe_channel"): fields.universe_channel.name,
    },
)
