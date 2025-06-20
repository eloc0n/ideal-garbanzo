from pydantic import BaseModel, HttpUrl, RootModel
from typing import List, Optional


class Contact(BaseModel):
    name: str
    address: str
    phone: str
    email: str
    linkedin: Optional[HttpUrl]


class SkillSet(BaseModel):
    highlights: List[str]
    technical: List[str]


class Experience(BaseModel):
    title: str
    company: str
    start: str
    end: str
    bullets: List[str]


class Education(BaseModel):
    degree: str
    institution: str
    location: Optional[str]


class Language(RootModel):
    root: List[str]

class Interest(RootModel):
    root: List[str]

class CV(BaseModel):
    contact: Contact
    skills: SkillSet
    languages: Language
    experience: List[Experience]
    education: List[Education]
    interests: Interest
