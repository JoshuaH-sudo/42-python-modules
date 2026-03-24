from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    model_validator,
)


class ContactType(str, Enum):
    VISUAL = "visual"
    RADIO = "radio"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContactData(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def cross_field_checks(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if (
            self.contact_type == ContactType.RADIO
            and self.signal_strength > 7.0
            and self.message_received is None
        ):
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )

        return self


def main() -> None:
    good_test_data = {
        "contact_id": "AC_2024_001",
        "timestamp": datetime.now(),
        "location": "Area 51, Nevada",
        "contact_type": ContactType.RADIO,
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "message_received": "Greetings from Zeta Reticuli",
        "witness_count": 5,
    }

    print("Alien Contact Log Validation")
    print("======================================")
    try:
        contact_data = AlienContactData(**good_test_data)
        print("Valid contact report:")
        print(
            f"ID: {contact_data.contact_id}",
            f"Type: {contact_data.contact_type.value}",
            f"Location: {contact_data.location}",
            f"Signal: {contact_data.signal_strength}/10",
            f"Duration: {contact_data.duration_minutes} minutes",
            f"Witnesses: {contact_data.witness_count}",
            f"Message: '{contact_data.message_received or 'None'}'",
            sep="\n",
        )
    except ValidationError as e:
        print(f"Error creating contact: {e}")
    print("\n======================================")

    bad_test_data = {
        "contact_id": "AC12345",
        "timestamp": datetime.now(),
        "location": "Sector 7G",
        "contact_type": ContactType.TELEPATHIC,
        "signal_strength": 5.0,
        "duration_minutes": 30,
        "witness_count": 2,
    }

    try:
        AlienContactData(**bad_test_data)
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            msg = error["msg"]
            if msg.startswith("Value error, "):
                msg = msg.replace("Value error, ", "", 1)
            print(msg)


if __name__ == "__main__":
    main()
