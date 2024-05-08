from pydantic import BaseModel
from typing import Optional
from typing import List
import time

class Lead_Labels (BaseModel):
    company: str
    team: List[str]
    amount: int
    duration: str
    capacity: str

entity_labels = [
    "team",
    "developer",
    "technology",
    "tool",
    "amount",
    "duration",
    "capacity",
    "company",
    "currency"
]

def set_start () -> time:
    return time.time()

def audit_elapsedtime(function: str, start: time):
    end = time.time()
    elapsedtime = end-start
    print("------------------")
    print(f"[{function}] Elapsed time: {elapsedtime}")
    print("------------------")
    return elapsedtime