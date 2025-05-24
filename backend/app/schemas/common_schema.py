from enum import Enum


class IFriendshipStatusEnum(str, Enum):
    pending: str = "pending"
    accepted: str = "accepted"
    declined: str = "declined"
    blocked: str = "blocked"


class ITaskStatusEnum(str, Enum):
    not_started: str = "not started"
    in_progress: str = "in progress"
    completed: str = "completed"
    cancelled: str = "cancelled"


class ITaskPriorityEnum(str, Enum):
    extreme: str = "extreme"
    moderate: str = "moderate"
    low: str = "low"
