# station_id: String, 3-10 characters
# • name: String, 1-50 characters
# • crew_size: Integer, 1-20 people
# 7
# Cosmic Data Discover Pydantic Models & Validation
# • power_level: Float, 0.0-100.0 percent
# • oxygen_level: Float, 0.0-100.0 percent
# • last_maintenance: DateTime field
# • is_operational: Boolean, defaults to True
# • notes: Optional string, max 200 characters

from datetime import datetime
from typing import Optional


def main() -> None:
    try:
        from pydantic import BaseModel, Field, ValidationError

        class SpaceStationData(BaseModel):
            station_id: str = Field(min_length=3, max_length=10)
            name: str = Field(min_length=1, max_length=50)
            crew_size: int = Field(ge=1, le=20)
            power_level: float = Field(ge=0.0, le=100.0)
            oxygen_level: float = Field(ge=0.0, le=100.0)
            last_maintenance: datetime = Field()
            is_operational: bool = Field(default=True)
            notes: Optional[str] = Field(None, max_length=200)

    except ImportError:
        print(
            "Pydantic is not installed. Please install it to run this module."
        )
        return

    print("Space Station Data Validation")
    print("========================================")
    try:
        station_data = SpaceStationData(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes=None,
        )
        print("Valid station created:")
        operational_status = (
            "Operational" if station_data.is_operational else "Non-Operational"
        )
        print(
            f"ID: {station_data.station_id}",
            f"Name: {station_data.name}",
            f"Crew: {station_data.crew_size} people",
            f"Power Level: {station_data.power_level}%",
            f"Oxygen Level: {station_data.oxygen_level}%",
            f"Operational: {operational_status}",
            sep="\n",
        )
        if station_data.notes:
            print(f"Notes: {station_data.notes}")
        else:
            print("")
    except ValidationError as e:
        print("Validation error occurred:")
        error_details = e.errors()
        for error in error_details:
            print(error["msg"])
    print("==========================================")

    try:
        SpaceStationData(
            station_id="ISS001",
            name="International Space Station",
            crew_size=100000,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes=None,
        )
    except ValidationError as e:
        print("Expected validation error:")
        error_details = e.errors()
        for error in error_details:
            print(error["msg"])


if __name__ == "__main__":
    main()
