from typing import List, Optional
from pydantic import BaseModel, Field


# -------------------------------
# Personal Information
# -------------------------------

class PersonalInformation(BaseModel):
    full_name: str = Field(description="Full name of the candidate")
    email: str = Field(description="Email address")
    phone: str = Field(description="Phone number")
    linkedin: Optional[str] = Field(default="")
    github: Optional[str] = Field(default="")
    portfolio: Optional[str] = Field(default="")


# -------------------------------
# Education
# -------------------------------

class Education(BaseModel):
    degree: str = Field(description="Degree name")
    institution: str = Field(description="College or university")
    graduation_year: str = Field(description="Graduation year")
    cgpa: Optional[str] = Field(default="")


# -------------------------------
# Project
# -------------------------------

class Project(BaseModel):
    title: str = Field(description="Project title")
    description: str = Field(
        description="Improved ATS-friendly project description"
    )
    technologies: List[str] = Field(
        default_factory=list,
        description="Technologies used"
    )


# -------------------------------
# Experience
# -------------------------------

class Experience(BaseModel):
    job_title: str = Field(description="Job title")
    company: str = Field(description="Company name")
    duration: str = Field(description="Employment duration")
    description: str = Field(
        description="Improved ATS-friendly work description"
    )


# -------------------------------
# Resume Schema
# -------------------------------

class Resume(BaseModel):

    personal_information: PersonalInformation

    target_role: str = Field(
        description="Target job role"
    )

    professional_summary: str = Field(
        description="Professional ATS-friendly summary"
    )

    career_objective: str = Field(
        description="Career objective"
    )

    education: List[Education] = Field(
        default_factory=list
    )

    skills: List[str] = Field(
        default_factory=list
    )

    suggested_skills: List[str] = Field(
        default_factory=list,
        description="AI suggested missing skills"
    )

    projects: List[Project] = Field(
        default_factory=list
    )

    experience: List[Experience] = Field(
        default_factory=list
    )

    certifications: List[str] = Field(
        default_factory=list
    )

    achievements: List[str] = Field(
        default_factory=list
    )

    languages: List[str] = Field(
        default_factory=list
    )

    additional_information: List[str] = Field(
        default_factory=list
    )
    