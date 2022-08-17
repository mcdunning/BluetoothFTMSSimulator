from flask import render_template
from werkzeug.utils import redirect

from app import app
from app.data_models import BLEDeviceData, UserData, WorkoutData, FrameData
from app.enums import FrameTypes, Genders
from app.forms import FrameSelectionForm, WorkoutSelectionForm


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

    return render_template('index.html',
                           title='Home',
                           ble_device=BLEDeviceData.get_data_model(),
                           user_data=UserData.get_data_model(),
                           fitness_device=WorkoutData.get_data_model())


@app.route('/frame_selection', methods=['GET', 'POST'])
def frame_selection():
    form = FrameSelectionForm(selected_frame_id=FrameData.selected_frame)
    form.selected_frame_id.choices = [(frame_type.value, frame_type.name) for frame_type in FrameTypes]

    if form.validate_on_submit():
        FrameData.selected_frame = form.selected_frame_id.data
        return redirect('/workout_selection')

    return render_template('frame_selection.html',
                           title='Frame Selection',
                           form=form)


@app.route('/workout_selection', methods=['GET', 'POST'])
def workout_selection():
    form = WorkoutSelectionForm(user_data_form=dict(age=UserData.age,
                                                    genders=UserData.gender,
                                                    weight=UserData.weight),
                                frame_data_form=dict(workout_time=WorkoutData.workout_time,
                                                     speed=WorkoutData.speed,
                                                     incline=WorkoutData.incline,
                                                     resistance=WorkoutData.resistance))
    form.user_data_form.genders.choices = [(gender.value, gender.name) for gender in Genders]

    # This call may cause rendering and/or validation problems in the future.
    # Seems to just remove the fields based on selected frame types which is the desired outcome.
    if FrameTypes.Treadmill.value == FrameData.selected_frame:
        form.frame_data_form.__delitem__('resistance')
    else:
        form.frame_data_form.__delitem__('speed')
        form.frame_data_form.__delitem__('incline')

    if form.start_workout.data and form.validate_on_submit():
        return redirect('/index')
    elif form.frame_selection.data:
        return redirect('/frame_selection')

    return render_template('workout_selection.html',
                           title="Workout Selection",
                           form=form)
