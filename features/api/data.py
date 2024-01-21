from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Odd:
    date: int
    over_under: Optional[float]
    spread_line2: Optional[float]
    provider: str
    spread_line1: Optional[float]
    over_under_line_over: Optional[float]
    over_under_line_under: Optional[float]
    money_line2: Optional[float]
    spread: Optional[float]
    money_line1: Optional[float]
    url: Optional[str]


@dataclass
class Result:
    game_id: int
    date: int
    team2id: int
    points_level: str
    team2initials: str
    team1color: str
    points: int
    team1name: str
    team2city: str
    team1city: str
    odds: List[Odd]
    team2color: str
    league_code: str
    team1id: int
    location: str
    team2name: str
    time: int
    team1initials: str
    high_points: int
    sport: str
    headline: Optional[str]


@dataclass
class Meta:
    code: int
    count: int
    description: str


@dataclass
class Root:
    meta: Meta
    results: List[Result]
