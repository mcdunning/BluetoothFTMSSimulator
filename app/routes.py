from flask import render_template
from app import app
from app.data_models import BLEDeviceData, UserData, WorkoutData, FrameData


@app.route('/')
@app.route('/index')
def index():
    BLEDeviceData.device_name = "phone1"

    UserData.first_name = "Matt"
    UserData.last_name = "Dunning"
    UserData.gender = "male"
    UserData.age = "41"
    UserData.weight = "205"

    WorkoutData.workout_time = 30
    WorkoutData.elapsed_time = 0
    WorkoutData.speed = 6
    WorkoutData.incline = 1.0
    WorkoutData.pace = 10

    return render_template('frame_selection.html',
                           title='Frame Selection',
                           frame_types=FrameData.get_data_model())
