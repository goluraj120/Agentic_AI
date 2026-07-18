from typing import Dict, List, Literal
from pydantic import BaseModel, Field


class Question(BaseModel):
    id: int = Field(
        description="Unique question number"
    )

    question: str = Field(
        description="The quiz question"
    )

    

    options: Dict[str, str] = Field(
        description="Options A, B, C and D"
    )

    answer: Literal[
        "A",
        "B",
        "C",
        "D"
    ] = Field(
        description="Correct option"
    )

    explanation: str = Field(
        description="Short explanation of the correct answer"
    )

    marks: int = Field(
        default=1,
        description="Marks for this question"
    )


class Quiz(BaseModel):

    title: str = Field(
        description="Title of the quiz"
    )

    topic: str = Field(
        description="Quiz topic"
    )

    goal: str = Field(
        description="Student learning goal"
    )

    level: Literal[
        "Beginner",
        "Intermediate",
        "Advanced"
    ]

    language: str = Field(
        description="Quiz language"
    )

    total_questions: int = Field(
        description="Total number of questions"
    )

    total_marks: int = Field(
        description="Total marks of the quiz"
    )

    estimated_time: str = Field(
        description="Estimated completion time"
    )

    questions: List[Question]