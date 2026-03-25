from datetime import datetime
from typing import List
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validation_rules(self):
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        if not any(
            member.rank in {Rank.COMMANDER, Rank.CAPTAIN}
            for member in self.crew
        ):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        crew_with_5_years_exp = [
            member for member in self.crew if member.years_experience >= 5
        ]
        percentage_experienced = len(crew_with_5_years_exp) / len(self.crew)
        if self.duration_days > 365 and percentage_experienced < 0.5:
            raise ValueError(
                "Long missions (> 365 days)",
                "need 50% experienced crew (5+ years)",
            )
        if any(member.is_active is False for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    commander = CrewMember(
        member_id="CM001",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=38,
        specialization="Mission Command",
        years_experience=15,
        is_active=True,
    )
    lieutenant = CrewMember(
        member_id="CM002",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=34,
        specialization="Navigation",
        years_experience=8,
        is_active=True,
    )
    officer = CrewMember(
        member_id="CM003",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=31,
        specialization="Engineering",
        years_experience=7,
        is_active=True,
    )

    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[commander, lieutenant, officer],
            mission_status="planned",
            budget_millions=2500.0,
        )
        print("Valid mission created:")
        print(
            f"Mission: {mission.mission_name}",
            f"ID: {mission.mission_id}",
            f"Destination: {mission.destination}",
            f"Duration: {mission.duration_days} days",
            f"Budget: ${mission.budget_millions}M",
            f"Crew size: {len(mission.crew)}",
            "Crew members:",
            sep="\n",
        )
        for member in mission.crew:
            print(
                f"- {member.name} ({member.rank.value})",
                f"- {member.specialization}",
            )
    except ValidationError as e:
        print(f"Error creating mission: {e}")

    invalid_crew = [
        CrewMember(
            member_id="CM004",
            name="Eva Green",
            rank=Rank.OFFICER,
            age=29,
            specialization="Science",
            years_experience=6,
            is_active=True,
        ),
        CrewMember(
            member_id="CM005",
            name="Mike Ross",
            rank=Rank.LIEUTENANT,
            age=32,
            specialization="Communications",
            years_experience=7,
            is_active=True,
        ),
        CrewMember(
            member_id="CM006",
            name="Nina Cole",
            rank=Rank.OFFICER,
            age=30,
            specialization="Engineering",
            years_experience=8,
            is_active=True,
        ),
    ]

    print("\n=========================================")
    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=invalid_crew,
            mission_status="planned",
            budget_millions=2500.0,
        )
    except ValidationError as e:
        first_error = e.errors()[0]["msg"]
        if first_error.startswith("Value error, "):
            first_error = first_error.replace("Value error, ", "", 1)
        print(first_error)


if __name__ == "__main__":
    main()
