"""Pydantic data models for ShopMind."""

from pydantic import BaseModel, Field

class UserProfile(BaseModel):
    budget_max: int | None = None
    child_age_months: int | None = None
    usage: list[Literal['city', 'travel', 'terrain', 'jogging']] | None = None
    car_trunk: bool | None = None
    public_transport: bool | None = None
    priority: Literal['weight', 'comfort', 'price', 'durability'] | None = None
    country: str | None = None

    def user_profile_complete(self) -> bool:
        return all([
            self.budget_max is not None,
            self.child_age_months is not None,
            self.usage is not None,
            self.car_trunk is not None,
            self.public_transport is not None,
            self.priority is not None,
        ])