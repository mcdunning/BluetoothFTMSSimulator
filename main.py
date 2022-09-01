from app import app
from app.data_models import BLEDeviceData, UserData, WorkoutData

bleDeviceData = BLEDeviceData()
userData = UserData()
workoutData = WorkoutData()

if __name__ == '__main__':
    app.run()
