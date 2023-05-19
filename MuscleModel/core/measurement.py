import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .position import Position
from .musclefiber import MuscleFiber


@forge_signature
class Measurement(sdRDM.DataModel):

    """In cupidatat mollit ipsum mollit. Do reprehenderit minim consequat mollit sit ad incididunt. Irure ullamco qui nulla consequat duis sit veniam. Nulla cupidatat enim pariatur mollit aliqua commodo deserunt non enim qui tempor est excepteur labore. Ex aliqua minim eu id laboris."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("measurementINDEX"),
        xml="@id",
    )

    force: Optional[float] = Field(
        default=None,
        description="Contraction force",
    )

    velocity: Optional[float] = Field(
        default=None,
        description="Contraction velocity",
    )

    position: Optional[Position] = Field(
        default=None,
        description="Spatial data",
    )

    live_position: List[Position] = Field(
        description="Live positions",
        default_factory=ListPlus,
        multiple=True,
    )

    fiber: Optional[MuscleFiber] = Field(
        default=None,
        description="Current state of the fiber",
    )

    def add_to_live_position(
        self,
        x: Optional[float] = None,
        y: Optional[float] = None,
        degree: Optional[float] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Position' to attribute live_position

        Args:
            id (str): Unique identifier of the 'Position' object. Defaults to 'None'.
            x (): X-coordinate of the point. Defaults to None
            y (): X-coordinate of the point. Defaults to None
            degree (): Degree in relation to zero-position of the foot. Defaults to None
        """

        params = {
            "x": x,
            "y": y,
            "degree": degree,
        }

        if id is not None:
            params["id"] = id

        self.live_position.append(Position(**params))
