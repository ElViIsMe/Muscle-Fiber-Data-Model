import sdRDM

from typing import List, Optional
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .position import Position
from .musclefiber import MuscleFiber
from .measurement import Measurement
from .muscle import Muscle


@forge_signature
class Root(sdRDM.DataModel):

    """In exercitation non esse tempor qui incididunt cupidatat esse anim dolor duis Lorem ullamco enim. Incididunt enim do labore pariatur aliquip proident elit nostrud dolore laboris labore ad tempor ad. Labore duis exercitation adipisicing velit id ea eiusmod aliquip enim ullamco."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("rootINDEX"),
        xml="@id",
    )

    muscles: List[Muscle] = Field(
        description="All muscles",
        default_factory=ListPlus,
        multiple=True,
    )

    isometric_measurements: List[Measurement] = Field(
        description="Enter something",
        default_factory=ListPlus,
        multiple=True,
    )

    isokinetic_measurements: List[Measurement] = Field(
        description="Enter something",
        default_factory=ListPlus,
        multiple=True,
    )

    def add_to_muscles(
        self,
        name: Optional[str] = None,
        isometric_measurements: Optional[Measurement] = None,
        isokinetic_measurements: Optional[Measurement] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Muscle' to attribute muscles

        Args:
            id (str): Unique identifier of the 'Muscle' object. Defaults to 'None'.
            name (): Name of the muscle. Defaults to None
            isometric_measurements (): Measurements with regard to the muscle. Defaults to None
            isokinetic_measurements (): Measurements with regard to the muscle. Defaults to None
        """

        params = {
            "name": name,
            "isometric_measurements": isometric_measurements,
            "isokinetic_measurements": isokinetic_measurements,
        }

        if id is not None:
            params["id"] = id

        self.muscles.append(Muscle(**params))

    def add_to_isometric_measurements(
        self,
        force: Optional[float] = None,
        velocity: Optional[float] = None,
        position: Optional[Position] = None,
        live_position: List[Position] = ListPlus(),
        fiber: Optional[MuscleFiber] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Measurement' to attribute isometric_measurements

        Args:
            id (str): Unique identifier of the 'Measurement' object. Defaults to 'None'.
            force (): Contraction force. Defaults to None
            velocity (): Contraction velocity. Defaults to None
            position (): Spatial data. Defaults to None
            live_position (): Live positions. Defaults to ListPlus()
            fiber (): Current state of the fiber. Defaults to None
        """

        params = {
            "force": force,
            "velocity": velocity,
            "position": position,
            "live_position": live_position,
            "fiber": fiber,
        }

        if id is not None:
            params["id"] = id

        self.isometric_measurements.append(Measurement(**params))

    def add_to_isokinetic_measurements(
        self,
        force: Optional[float] = None,
        velocity: Optional[float] = None,
        position: Optional[Position] = None,
        live_position: List[Position] = ListPlus(),
        fiber: Optional[MuscleFiber] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Measurement' to attribute isokinetic_measurements

        Args:
            id (str): Unique identifier of the 'Measurement' object. Defaults to 'None'.
            force (): Contraction force. Defaults to None
            velocity (): Contraction velocity. Defaults to None
            position (): Spatial data. Defaults to None
            live_position (): Live positions. Defaults to ListPlus()
            fiber (): Current state of the fiber. Defaults to None
        """

        params = {
            "force": force,
            "velocity": velocity,
            "position": position,
            "live_position": live_position,
            "fiber": fiber,
        }

        if id is not None:
            params["id"] = id

        self.isokinetic_measurements.append(Measurement(**params))
