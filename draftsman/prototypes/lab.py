# lab.py

from draftsman.classes.entity import Entity
from draftsman.classes.mixins import (
    ModulesMixin,
    CircuitSplitOutputMixin,
    CircuitSplitInputMixin,
    CircuitConnectableMixin,
    EnergySourceMixin,
)
from draftsman.constants import InventoryType
from draftsman.serialization import draftsman_converters
from draftsman.signatures import Condition, QualityID, SignalID
from draftsman.validators import instance_of

from draftsman.data.entities import labs
from draftsman.data import entities, modules

import attrs
from typing import Iterable, Optional


@attrs.define
class Lab(
    ModulesMixin,
    CircuitSplitOutputMixin,
    CircuitSplitInputMixin,
    CircuitConnectableMixin,
    EnergySourceMixin,
    Entity,
):
    """
    An entity that consumes items and produces research.
    """

    @attrs.define
    class ResearchCondition(Condition):
        condition: Condition = attrs.field(
            factory=Condition,
            converter=Condition.converter,
            validator=instance_of(Condition),
        )
        """
        The condition that must pass in order for this lab to pick this 
        technology to research.
        """
        name: Optional[str] = attrs.field(  # TODO: should be technology name
            default=None, validator=instance_of(Optional[str])
        )
        """
        The name of the technology to research if this condition passes. Can be
        omitted, in which case this condition will be ignored.
        """
        count: int = attrs.field(default=0, validator=instance_of(int))
        """
        Unknown.
        """

    # =========================================================================

    @property
    def similar_entities(self) -> list[str]:
        return labs

    @property
    def inputs(self) -> Optional[list[str]]:
        """
        The inputs that this Lab uses to research, listed in their Factorio
        order. Returns ``None`` if this entity is not recognized by Draftsman.
        """
        return entities.raw.get(self.name, {"inputs": None})["inputs"]

    @property
    def module_slots_occupied(self) -> int:
        return len(
            {
                inv_pos.stack
                for req in self.item_requests
                if req.id.name in modules.raw
                for inv_pos in req.items.in_inventory
                if inv_pos.inventory == InventoryType.LAB_MODULES
            }
        )

    # TODO: should be evolve
    # item_requests = attrs.fields(ItemRequestMixin).item_requests.reuse()

    # @item_requests.validator()
    # @conditional(ValidationMode.STRICT)
    # def ensure_name_recognized(self, attr, value):
    #     # TODO: check the lab's limitations to see if the module is allowed
    #     # ('allowed_effects')
    #     # This is all for regular labs, but not necessarily modded ones.
    #     if item not in modules.raw and item not in self.inputs:
    #         warnings.warn(
    #             "Item '{}' cannot be placed in Lab '{}'".format(item, self.name),
    #             ItemLimitationWarning,
    #             stacklevel=2,
    #         )

    @property
    def allowed_effects(self) -> Optional[set[str]]:
        return entities.get_allowed_effects(
            self.name, default=entities.ALL_EFFECTS_EXCEPT_QUALITY
        )

    # =========================================================================

    set_research: Optional[bool] = attrs.field(
        default=False, validator=instance_of(Optional[bool])
    )
    """
    .. serialized::
    
        This attribute is imported/exported from blueprint strings.

    Whether or not the technology that this lab is researching should be decided
    globally via the technology menu or locally via the 
    :py:attr:`.research_conditions` and the connected input circuit wires.

    .. versionadded:: 4.0.0 (Factorio 2.1)
    """

    research_conditions: list[ResearchCondition] = attrs.field(
        factory=list, validator=instance_of(list[ResearchCondition])
    )
    """
    .. serialized::
        
        This attribute is imported/exported from blueprint strings.

    The list of conditions that specify what technology should be researched by
    this particular lab, given some circuit network input.

    .. versionadded:: 4.0.0 (Factorio 2.1)
    """

    read_contents: bool = attrs.field(default=False, validator=instance_of(bool))
    """
    .. serialized::
        
        This attribute is imported/exported from blueprint strings.

    Whether or not the current inventory contents of this lab should be output
    to the output circuit wires.

    .. versionadded:: 4.0.0 (Factorio 2.1)
    """

    read_research_cost: bool = attrs.field(default=False, validator=instance_of(bool))
    """
    .. serialized::
        
        This attribute is imported/exported from blueprint strings.

    Whether or not to output the total number of science packs required for the
    current research to the output circuit wires.

    .. versionadded:: 4.0.0 (Factorio 2.1)
    """

    read_technology_level: bool = attrs.field(
        default=False, validator=instance_of(bool)
    )
    """
    .. serialized::
        
        This attribute is imported/exported from blueprint strings.

    Whether or not to read the current technology level of the current research,
    if that research has a level associated with it.

    .. versionadded:: 4.0.0 (Factorio 2.1)
    """

    technology_level_signal: Optional[SignalID] = attrs.field(
        factory=lambda: SignalID(name="signal-L", type="virtual"),
        converter=SignalID.converter,
        validator=instance_of(Optional[SignalID]),
    )
    """
    .. serialized::
        
        This attribute is imported/exported from blueprint strings.

    What signal to output the current recipe level, if configured to do so via
    :py:attr:`.read_technology_level`.

    .. versionadded:: 4.0.0 (Factorio 2.1)
    """

    # =========================================================================

    def request_modules(
        self,
        module_name: str,  # TODO: should be ModuleID
        slots: int | Iterable[int],
        quality: QualityID = "normal",
    ):
        return super().request_modules(
            InventoryType.LAB_MODULES, module_name, slots, quality
        )

    # =========================================================================

    __hash__ = Entity.__hash__


draftsman_converters.get_version((2, 1)).add_hook_fns(
    Lab.ResearchCondition,
    lambda fields: {
        "condition": fields.condition.name,
        "name": fields.name.name,
        "count": fields.count.name,
    },
)

draftsman_converters.get_version((2, 1)).add_hook_fns(
    Lab,
    lambda fields: {
        ("control_behavior", "set_research"): fields.set_research.name,
        ("control_behavior", "conditions"): fields.research_conditions.name,
        ("control_behavior", "read_contents"): fields.read_contents.name,
        ("control_behavior", "read_research_cost"): fields.read_research_cost.name,
        (
            "control_behavior",
            "read_technology_level",
        ): fields.read_technology_level.name,
        (
            "control_behavior",
            "technology_level_signal",
        ): fields.technology_level_signal.name,
    },
)
