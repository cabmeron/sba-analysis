from abc import ABC
from dataclasses import dataclass

class DepartmentMaps(ABC):
    nasa: int
    department_of_energy: int
    department_of_h_and_h: int
    department_of_defense: int
    nuclear_reg_commission: int
    department_of_commerce: int
    department_of_education: int
    department_of_agriculture: int
    department_of_the_interior: int
    department_of_homeland_sec: int
    department_of_transporation: int
    national_science_foundation: int
    enviromental_protection_agency: int

@dataclass
class PI:
    name: str
    phone: str
    email: str
    education_level: str

@dataclass
class Award:
    pi: PI
    phase: str
    agency: str
    program: str
    topic_code: str
    award_title: str
    award_year: int
    award_amount: int


@dataclass
class Company:
    city: str
    name: str
    state: str
    website: str
    address: str
    zip_code: str