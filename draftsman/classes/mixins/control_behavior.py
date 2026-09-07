# control_behavior.py

from draftsman.classes.exportable import Exportable
from draftsman.serialization import draftsman_converters
from draftsman.signatures import (
    CircuitNetworkSelection,
)
from draftsman.validators import instance_of

import attrs


@attrs.define(slots=False)
class CircuitSplitIOMixin(Exportable):
    """
    .. versionadded:: 4.0.0 (Factorio 2.1)

    Enables the entity to specify split input/output circuit wires.
    """

    input_networks: CircuitNetworkSelection = attrs.field(
        factory=CircuitNetworkSelection,
        converter=CircuitNetworkSelection.converter,
        validator=instance_of(CircuitNetworkSelection),
    )
    """
    .. serialized::

        This attribute is imported/exported from blueprint strings.

    What wires should be considered for this entity's circuit inputs.

    .. versionadded:: 4.0.0 (Factorio 2.1)
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

    # =========================================================================

    def merge(self, other: "CircuitSplitIOMixin"):
        super().merge(other)
        self.input_networks = other.input_networks
        self.output_networks = other.output_networks


draftsman_converters.get_version((2, 1)).add_hook_fns(
    CircuitSplitIOMixin,
    lambda fields: {
        ("control_behavior", "input_networks"): fields.input_networks.name,
        ("control_behavior", "output_networks"): fields.output_networks.name,
    },
)
