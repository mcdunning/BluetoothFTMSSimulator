import abc

from app.enums import Genders, FrameTypes


class FrameSimulatorDataModelInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_data_model') and
                callable(subclass.get_data_model) or
                NotImplemented)

    @staticmethod
    @abc.abstractmethod
    def get_data_model() -> dict:
        """Create a dictionary of the contents in the data model"""
        raise NotImplementedError


class FrameData(FrameSimulatorDataModelInterface):
    selected_frame = FrameTypes.Frame.value
    workout_state = 0

    @staticmethod
    def get_data_model() -> dict:
        return {'selected_frame': FrameData.selected_frame}


class BLEDeviceData(FrameSimulatorDataModelInterface):
    device_name = ""

    @staticmethod
    def get_data_model() -> dict:
        return {'device_name': BLEDeviceData.device_name}


class UserData(FrameSimulatorDataModelInterface):
    MIN_AGE = 13
    DEFAULT_WEIGHT = 150.0

    first_name = ""
    last_name = ""
    gender = Genders.Male.value
    age = MIN_AGE
    weight = DEFAULT_WEIGHT

    @staticmethod
    def get_data_model() -> dict:
        return {'first_name': UserData.first_name,
                'last_name': UserData.last_name,
                'gender': {UserData.gender: Genders.value(UserData.gender)},
                'age': UserData.age,
                'weight': UserData.weight}


class WorkoutData(FrameSimulatorDataModelInterface):
    default_workout_time = 30

    workout_time = default_workout_time
    elapsed_time = 0
    remaining_time = 0

    speed = 0
    incline = 0.0
    pace = 0
    resistance = 0

    @staticmethod
    def get_data_model() -> dict:
        return {'workout_time': WorkoutData.workout_time,
                'elapsed_time': WorkoutData.elapsed_time,
                'remaining_time': WorkoutData.workout_time - WorkoutData.elapsed_time,
                'speed': WorkoutData.speed,
                'incline': WorkoutData.incline,
                'pace': WorkoutData.pace,
                'resistance': WorkoutData.resistance}
