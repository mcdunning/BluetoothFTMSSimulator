import wtforms
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, ValidationError, IntegerField, validators, FormField, \
    DecimalField

from app.data_models import UserData
from app.enums import FrameTypes, Genders
from app.workout_stat_utils import WorkoutStatUtils


def validate_selected_frame(form, field):
    if not FrameTypes.is_valid_frame_type(field.data):
        raise ValidationError("The selected frame type is invalid")


def validate_selected_gender(form, field):
    if not Genders.is_valid_gender(field.data):
        raise ValidationError("The selected gender is invalid")


class FrameSelectionForm(FlaskForm):
    selected_frame_id = SelectField('Frame Type:', coerce=int, validators=[validate_selected_frame])
    workout_selection = SubmitField('Workout Selection')


class UserDataForm(wtforms.Form):
    age = IntegerField('Age:', validators=[validators.InputRequired(),
                                           validators.NumberRange(min=UserData.MIN_AGE)])
    genders = SelectField('Gender:', coerce=int, validators=[validate_selected_gender])
    weight = IntegerField('Weight:', validators=[validators.InputRequired()])


class FrameDataForm(wtforms.Form):
    workout_time = IntegerField('Workout Time:',
                                validators=[validators.InputRequired(),
                                            validators.NumberRange(min=WorkoutStatUtils.MIN_WORKOUT_TIME,
                                                                   max=WorkoutStatUtils.MAX_WORKOUT_TIME)])
    speed = IntegerField('Speed:',
                         validators=[validators.InputRequired(),
                                     validators.NumberRange(min=WorkoutStatUtils.MIN_SPEED,
                                                            max=WorkoutStatUtils.MAX_SPEED)])
    incline = DecimalField('Incline:',
                           validators=[validators.InputRequired(),
                                       validators.NumberRange(min=WorkoutStatUtils.MIN_INCLINE,
                                                              max=WorkoutStatUtils.MAX_INCLINE)])
    resistance = IntegerField('Resistance:',
                              validators=[validators.InputRequired(),
                                          validators.NumberRange(min=WorkoutStatUtils.MIN_RESISTANCE,
                                                                 max=WorkoutStatUtils.MAX_RESISTANCE)])

    def __init__(self, *args, **kwargs):
        super(FrameDataForm, self).__init__(*args, **kwargs)
        if FrameTypes.Treadmill.value == kwargs.get('selected_frame'):
            del self.resistance
        else:
            del self.speed
            del self.incline


class WorkoutSelectionForm(FlaskForm):
    user_data_form = FormField(UserDataForm, separator="_")
    frame_data_form = FormField(FrameDataForm, separator="_")
    frame_selection = SubmitField('Frame Selection')
    start_workout = SubmitField('Start Workout')
