from app.data_models import WorkoutData


def calculate_pace():
    WorkoutData.pace = WorkoutData.speed / 60


class CardioFrames:
    min_workout_time = 5
    max_workout_time = 120

    def __init__(self, workout_time):
        if self.min_workout_time <= workout_time <= self.max_workout_time:
            WorkoutData.workout_time = workout_time

    def start_workout(self):
        # todo:  Need to implement this
        pass


class Treadmill(CardioFrames):
    max_speed = 12
    min_speed = 0
    speed_increment = 0.5

    max_incline = 25
    min_incline = 0
    incline_increment = 0.1

    def __init__(self, workout_time, initial_speed, initial_incline):
        super().__init__(workout_time)
        WorkoutData.speed = initial_speed
        WorkoutData.incline = initial_incline

        calculate_pace()

    def adjust_speed(self, increment_up):
        if increment_up:
            if WorkoutData.speed + self.speed_increment <= self.max_speed:
                WorkoutData.speed = WorkoutData.speed + self.speed_increment
        else:
            if self.min_speed <= WorkoutData.speed - self.speed_increment:
                WorkoutData.speed = WorkoutData.speed - self.speed_increment

        calculate_pace()

    def set_speed(self, new_speed):
        if self.min_speed <= new_speed <= self.max_speed:
            WorkoutData.speed = new_speed

            calculate_pace()

    def adjust_incline(self, increment_up):
        if increment_up:
            if WorkoutData.incline + self.incline_increment <= self.max_incline:
                WorkoutData.incline = WorkoutData.incline + self.incline_increment
        else:
            if self.min_incline <= WorkoutData.incline - self.incline_increment:
                WorkoutData.incline = WorkoutData.incline - self.incline_increment

    def set_incline(self, new_incline):
        if self.min_incline <= new_incline <= self.max_incline:
            WorkoutData.incline = new_incline
