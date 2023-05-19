import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class MuscleFiber(sdRDM.DataModel):

    """Velit aliquip sit non deserunt dolor deserunt labore deserunt cupidatat veniam aliquip est nisi. Sit fugiat do voluptate cupidatat amet aute sint. Est Lorem duis sint est deserunt eiusmod ad duis officia. Incididunt nulla proident sint duis nulla cupidatat cillum proident. Do ad consectetur cupidatat pariatur laborum. Eiusmod labore dolor mollit nisi do dolore ad amet. Id laborum aliqua enim pariatur tempor culpa adipisicing ad aliquip."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("musclefiberINDEX"),
        xml="@id",
    )

    force: Optional[float] = Field(
        default=None,
        description="Force of the fiber",
    )

    length: Optional[float] = Field(
        default=None,
        description="Length of the fiber",
    )

    pennation_angle: Optional[float] = Field(
        default=None,
        description="Angle of pennation",
        min=0,
        max=89,
    )
