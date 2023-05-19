import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Position(sdRDM.DataModel):

    """Mollit quis proident nisi magna. Exercitation excepteur eu amet est ex reprehenderit ullamco ipsum occaecat do ut. Commodo magna anim laborum nostrud aute id ipsum velit laborum. Eiusmod qui sunt laborum elit dolor incididunt est commodo eu sint labore culpa officia. Ex laboris excepteur ad duis reprehenderit consectetur amet."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("positionINDEX"),
        xml="@id",
    )

    x: Optional[float] = Field(
        default=None,
        description="X-coordinate of the point",
    )

    y: Optional[float] = Field(
        default=None,
        description="X-coordinate of the point",
    )

    degree: Optional[float] = Field(
        default=None,
        description="Degree in relation to zero-position of the foot",
    )
