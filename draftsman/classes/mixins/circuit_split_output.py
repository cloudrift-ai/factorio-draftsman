# circuit_split_output.py

from draftsman.classes.exportable import Exportable
from draftsman.serialization import draftsman_converters
from draftsman.signatures import CircuitNetworkSelection
from draftsman.validators import instance_of

import attrs


@attrs.define(slots=False)
class CircuitSplitOutputMixin(Exportable):
    """
    Allows the entity to specifiy what circuit wires it should output on.
    """

    output_networks: CircuitNetworkSelection = attrs.field(
        factory=CircuitNetworkSelection,
        converter=CircuitNetworkSelection.converter,
        validator=instance_of(CircuitNetworkSelection),
    )
    """
    .. serialized::

        This attribute is imported/exported from blueprint strings.

    What wires should be considered for this entity's circuit outputs.

    .. versionadded:: 4.0.0 (Factorio 2.1)
    """


draftsman_converters.get_version((2, 1)).add_hook_fns(
    CircuitSplitOutputMixin,
    lambda fields: {
        ("control_behavior", "output_networks"): fields.output_networks.name,
    },
)
