from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired

from ..models import Recipe, RecipeCategory, User


class AddRecipesForm(FlaskForm):
    """
    Form for chef to enter recipe
    """

    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    people_served = StringField('Number of Plates')
    quantity = StringField('Quantity')
    ingredient = StringField('Ingredient')
    making_steps = StringdField('Making Steps')
    category = StringField('Category')
    cook = StringField('Cook')
    submit = SubmitField('Submit')

class EditRecipeForm(FlaskForm):
    """
    Form for the chef to edit recipe
    """
    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    people_served = StringField('Number of Plates')
    quantity = StringField('Quantity')
    ingredient = StringField('Ingredient')
    making_steps = StringdField('Making Steps')
    category = StringField('Category')
    cook = StringField('Cook')
    submit = SubmitField('Save')


    
class AddRecipeCategoryForm(FlaskForm):
    
    """
    Form for the chef to enter recipe category
    """
    category_name = StringField('Category Name', validators = [DataRequired])
    details = StringField('Details')
   
    submit = SubmitField('Submit')


class EditRecipeCategory(FlaskForm):
    
    """
    Form for chef to edit recipe category
    """
    category_name = StringField('Category Name', validators = [DataRequired])
    details = StringField('Details')
    submit = SubmitField('Save')
    


