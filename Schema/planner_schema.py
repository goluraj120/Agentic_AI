from typing import List
from pydantic import BaseModel, Field


class WeekPlan(BaseModel):
    week_number: int = Field(
        description="Week number in the study plan."
    )

    topics: List[str] = Field(
        description="Topics to study during this week."
    )

    learning_objectives: List[str] = Field(
        default_factory=list,
        description="Learning objectives for this week."
    )

    estimated_study_hours: int = Field(
        default=0,
        description="Estimated study hours for this week."
    )

    revision: bool = Field(
        default=False,
        description="Whether this week includes a revision session."
    )

    recommended_agents: List[str] = Field(
        default_factory=list,
        description="AI agents recommended for this week's learning."
    )


class StudyPlan(BaseModel):
    title: str = Field(
        description="Title of the study plan."
    )

    goal: str = Field(
        description="User's learning goal."
    )

    level: str = Field(
        description="Current skill level."
    )

    duration: int = Field(
        description="Total duration of the study plan in weeks."
    )

    language: str = Field(
        description="Preferred language."
    )

    total_study_hours: int = Field(
        default=0,
        description="Total estimated study hours for the complete plan."
    )

    weeks: List[WeekPlan] = Field(
        default_factory=list,
        description="Weekly study plan."
    )