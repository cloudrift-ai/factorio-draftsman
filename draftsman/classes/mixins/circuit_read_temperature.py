# circuit_read_temperature.py

from draftsman.classes.exportable import Exportable
from draftsman.serialization import draftsman_converters
from draftsman.signatures import SignalID
from draftsman.validators import instance_of

import attrs
from typing import Optional


@attrs.define(slots=False)
class CircuitReadTemperatureMixin(Exportable):
    """
    Permits this entity to read and broadcast it's temperature to the output circuit
    network.
    """

    read_temperature: Optional[bool] = attrs.field(
        default=False, validator=instance_of(Optional[bool])
    )
    """
    .. serialized::

        This attribute is imported/exported from blueprint strings.

    Whether or not this pipe should broadcast it's temperature to its configured
    output wires. The output signal type is defined by 
    :py:attr:`.temperature_signal`.

    .. versionadded 4.0.0 (Factorio 2.1)
    """

    temperature_signal: Optional[SignalID] = attrs.field(
        factory=lambda: SignalID(name="signal-T", type="virtual"),
        converter=SignalID.converter,
        validator=instance_of(Optional[SignalID]),
    )
    """
    .. serialized::

        This attribute is imported/exported from blueprint strings.

    What signal should hold the fluid temperature value, if 
    :py:attr:`.read_temperature` is ``True``.

    .. versionadded 4.0.0 (Factorio 2.1)
    """


draftsman_converters.get_version((2, 0)).add_hook_fns(
    CircuitReadTemperatureMixin,
    lambda fields: {
        ("control_behavior", "read_temperature"): fields.read_temperature.name,
        ("control_behavior", "temperature_signal"): fields.temperature_signal.name,
    }
)

draftsman_converters.get_version((2, 1)).add_hook_fns(
    CircuitReadTemperatureMixin,
    lambda fields: {
        ("control_behavior", "read_temperature"): fields.read_temperature.name,
        ("control_behavior", "temperature_signal"): fields.temperature_signal.name,
    }
)