# circuit_read_pipe.py

from draftsman.classes.exportable import Exportable
from draftsman.constants import PipeReadMode
from draftsman.serialization import draftsman_converters
from draftsman.validators import instance_of

import attrs


@attrs.define(slots=False)
class CircuitReadPipeMixin(Exportable):
    """
    Mixin of common parameters that allows all pipes to broadcast their fluid
    contents as well as the temperature of that fluid.
    """

    read_mode: PipeReadMode = attrs.field(
        default=PipeReadMode.READ_CONTENTS,
        converter=PipeReadMode,
        validator=instance_of(PipeReadMode),
    )
    """
    .. serialized::

        This attribute is imported/exported from blueprint strings.

    In what manner this pipe should broadcast it's fluid contents to the 
    configured output wires.

    .. versionadded 4.0.0 (Factorio 2.1)
    """


draftsman_converters.get_version((2, 1)).add_hook_fns(
    CircuitReadPipeMixin,
    lambda fields: {
        ("control_behavior", "circuit_mode_of_operation"): fields.read_mode.name,
    },
)
