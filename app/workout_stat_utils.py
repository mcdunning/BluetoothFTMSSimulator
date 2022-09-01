

class WorkoutStatUtils:

    MIN_WORKOUT_TIME = 5
    MAX_WORKOUT_TIME = 120

    MIN_SPEED = 0.0
    MAX_SPEED = 12.0
    SPEED_INCREMENT = 0.5

    MIN_INCLINE = 0.0
    MAX_INCLINE = 25.0
    INCLINE_INCREMENT = 0.5

    MIN_RESISTANCE = 0
    MAX_RESISTANCE = 50
    RESISTANCE_INCREMENT = 1

    @staticmethod
    def calculate_pace(speed: float) -> float:
        return speed / 60
