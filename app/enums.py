from enum import IntEnum, unique


@unique
class FrameTypes(IntEnum):
    Frame = -1
    Treadmill = 0

    @classmethod
    def is_valid_frame_type(cls, selected_frame_type):
        return FrameTypes.Frame.value != selected_frame_type


@unique
class Genders(IntEnum):
    Gender = -1
    Male = 0
    Female = 1
    Other = 2

@unique
class WorkoutState(IntEnum):
    Initializing = 0
    Started = 1
    Paused = 2
    Ended = 3
