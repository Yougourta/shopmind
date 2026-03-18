"""Pydantic data models for ShopMind."""

from pydantic import BaseModel
from typing import Literal
from datetime import datetime

# Shared type alias — used in both UserProfile and Stroller
TerrainType = Literal['city', 'travel', 'off_road', 'jogging']

PriorityType = Literal['weight', 'comfort', 'price', 'durability', 'safety', 'style']

StrollerType = Literal['single', 'double', 'tandem', 'travel_system']


class UserProfile(BaseModel):
    budget_min: float | None = None
    budget_max: float | None = None
    children_ages_months: list[int] | None = None
    usage: list[TerrainType] | None = None
    car_trunk: bool | None = None          # does the user use a car boot?
    public_transport: bool | None = None   # does the user use public transport?
    staircase: bool | None = None          # no elevator, must carry up stairs?
    priority: PriorityType | None = None
    preferred_brands: list[str] | None = None
    country: str | None = None

    def user_profile_complete(self) -> bool:
        return all([
            self.budget_max is not None,
            self.children_ages_months is not None,
            self.usage is not None
        ])


class PriceRecord(BaseModel):
    date: datetime
    price: float
    currency: str = "EUR"
    store: str | None = None
    source_url: str | None = None
    is_promotional: bool | None = None


class Dimension(BaseModel):
    height_cm: float | None = None
    length_cm: float | None = None
    width_cm: float | None = None


class Stroller(BaseModel):
    product_code: str
    name: str
    brand: str
    stroller_type: StrollerType | None = None
    price: float | None = None
    available: bool | None = None
    currency: str = "EUR"
    store: str | None = None
    url: str | None = None
    price_history: list[PriceRecord] | None = None
    dimensions: Dimension | None = None
    folded_dimensions: Dimension | None = None
    weight: float | None = None
    min_age_months: int | None = None
    max_age_months: int | None = None
    max_child_weight: float | None = None
    terrain_types: list[TerrainType] | None = None
    cabin_approved: bool | None = None
    one_hand_fold: bool | None = None
    suspension: bool | None = None
    seat_reversible: bool | None = None
    newborn_compatible: bool | None = None
    nacelle_included: bool | None = None
    basket_capacity_liters: float | None = None
    compatible_car_seats: list[str] | None = None
    certifications: list[str] | None = None
    resale_value: Literal['low', 'medium', 'high'] | None = None
    handlebar_adjustable: bool | None = None
    accessories: list[str] | None = None
    cleaning_difficulty: Literal['easy', 'medium', 'hard'] | None = None
    warranty_months: int | None = None
    discontinued: bool | None = None
    extra_preferences: list[str] | None = None


class StrollerList(BaseModel):
    strollers: list[Stroller]
    scraped_at: str | None = None   # ISO datetime string
    market: str | None = None
