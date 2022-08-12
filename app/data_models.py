import abc


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


class BLEDeviceData(FrameSimulatorDataModelInterface):
    device_name = ""

    @staticmethod
    def get_data_model() -> dict:
        return {'device_name': BLEDeviceData.device_name}


class UserData(FrameSimulatorDataModelInterface):
    first_name = ""
    last_name = ""
    gender = ""
    age = 0
    weight = 150.0

    @staticmethod
    def get_data_model() -> dict:
        return {'first_name': UserData.first_name,
                'last_name': UserData.last_name,
                'gender': UserData.gender,
                'age': UserData.age,
                'weight': UserData.weight}


class WorkoutData(FrameSimulatorDataModelInterface):
    workout_time = 0
    elapsed_time = 0
    remaining_time = 0

    speed = 0
    incline = 0.0
    pace = 0

    @staticmethod
    def get_data_model() -> dict:
        return {'workout_time': WorkoutData.workout_time,
                'elapsed_time': WorkoutData.elapsed_time,
                'remaining_time': WorkoutData.workout_time - WorkoutData.elapsed_time,
                'speed': WorkoutData.speed,
                'incline': WorkoutData.incline,
                'pace': WorkoutData.pace}
