from dataclasses import dataclass, field

# tag::CLUBMEMBER[]
@dataclass
class ClubMember:
    name: str = 'a'
    guests: list = field(default_factory=list)
# end::CLUBMEMBER[]
