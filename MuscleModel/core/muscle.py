import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


from .measurement import Measurement


@forge_signature
class Muscle(sdRDM.DataModel):

    """Nostrud amet incididunt est veniam aliqua mollit voluptate sint. Incididunt non deserunt tempor aute labore tempor duis magna ad culpa. Incididunt ea qui veniam duis aliqua enim exercitation ea. Culpa officia ipsum in aliqua reprehenderit eu sunt quis incididunt veniam irure sunt. Nostrud velit laborum quis mollit adipisicing fugiat exercitation deserunt adipisicing magna. Id cupidatat minim anim minim minim nostrud."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("muscleINDEX"),
        xml="@id",
    )

    name: Optional[str] = Field(
        default=None,
        description="Name of the muscle",
    )

    isometric_measurements: Optional[Measurement] = Field(
        default=None,
        description="Measurements with regard to the muscle",
    )

    isokinetic_measurements: Optional[Measurement] = Field(
        default=None,
        description="Measurements with regard to the muscle",
    )
