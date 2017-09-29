# app/chef/views.py
from flask import abort, flash, redirect, render_template, url_for
form flask_login import current_user, login_required

from flask import render_template
from flask_login import login_required

from . import chef
from forms import AddRecipesForm, EditRecipesForm, AddCategoryForm, EditCategoryForm
 
from .. import db
from ..models import Recipe, RecipeCategory, User

recipe = Recipe
category = RceipeCategory


def check_chef():
    
    """
    Prevent non-chefs from accessing the page
    """
    if not current_user.is_chef:
        abort(403)

# Recipe views
@chef.route('/recipes', methods=['GET', 'POST'])
@login_required
def list_recipes():
    """
    List all recipes
    """

    check_recipe()

    recipes = 

    return render_template('chef/recipes.html',
                           recipes=recipes, title="Recipes")

@chef.route('/recipes', methods=['GET', 'POST'])
@login_required
def add_recipe():
    """
    Add recipes
    """
    check_chef()

    add_recipe = True

    form = RecipeForm()
    if form.validate_on_submit():
    
        
        recipe.add_recipe(form.recipe_name.data,form.ingredient.data,
                        form.making_steps.data,form.quantity.data,
                        form.people_served.data,form.cook.data,
                        form.category.data)
        try:
            
            
            flash('You have successfully added a new recipe.')
        except:
            # in case recipe name already exists
            flash('Error: recipe name already exists.')

        # redirect to recipes page
        return redirect(url_for('chef.list_recipes'))

    # load recipes template
    return render_template('chef/recipes.html', action="Add",
                           add_recipe=add_recipe, form=form,
                           title="Add Recipe")

@chef.route('/recipes/edit/<int:recipe_id>', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    """
    Edit a recipe
    """

    check_chef()

    add_recipe = False

    if recipe_name is in recipe:
        recipe.delete_recipe(recipe_name)
        add_recipe(form.recipe_name.data,form.ingredient.data,
                        form.making_steps.data,form.quantity.data,
                        form.people_served.data,form.cook.data,
                        form.category.data)
        
        
    
        flash('You have successfully edited the recipe.')

        # redirect to the recipe
        return redirect(url_for('chef.list_recipes'))

        

        return render_template('chef/recipe.hml', action="Edit",
                               add_recipe=add_recipe, form=form,
                               recipe=recipe, title="Edit Recipe")

@admin.rout('/recipes/delete<int:id2>', methods=['GET', 'POST'])
@login_required
def delete_recipe(id2):
    
    """
    Delete a recipe from the database
    """
    chek_chef()

    recipe.delete_recipe(name)
    flash('You have successfully deleted a recipe.')

    # redirect to the recipes page
    return render_template(title="Delete Recipe")
    return redirect(url_for('chef.list_recipes'))
    

# Recipe Category Views
@chef.route('/recipe_categories', methods=['GET', 'POST'])

def list_recipe_categories():
    """
    List all recipe categories
    """

    check_recipe_category()

    recipe_categories = RecipeCategory.query.all()

    return render_template('admin/recipe_category.html',
                           recipe_categories=recipe_categories, title="Recipe Categories")

@chef.route('/recipe_categories', methods=['GET', 'POST'])

def add_recipe_category():
    """
    Add a recipe category
    """
    check_chef()

    add_recipe_category = True

    form = RecipeCategoryForm()
    if form.validate_on_submit():
        category.add_category(form.recipe_name.data,form.details.data)
        try:
            #add recipe to the database
            flash('You have successfully added a new recipe category.')
        except:
            # in case recipe category name already exists
            flash('Error: recipe category name already exists.')

        # redirect to recipe categories page
        return redirect(url_for('chef.list_recipe_categories'))

    # load recipe categories template
    return render_template('chef/recipe_categories.html', action="Add",
                           add_recipe_category=add_recipe_category, form=form,
                           title="Add Recipe Category")

@chef.route('/recipes_categories/edit/<int:cat_id>', methods=['GET', 'POST'])

def edit_recipe_category(cat_name):
    """
    Edit a recipe category
    """

    check_chef()

    add_recipe_category = False

    if cat_name is in category:
        category.delete_category(cat_name)
        category.add_category(form.recipe_name.data,form.details.data)
        
    form = Recipe_on_submit():
        if form.validate_on_submit():
            edit_category(form.category_name.data,form.details.data)
            flash('You have successfully edited the recipe category.')

            # redirect to the recipe
            return redirect(url_for('chef.list_recipe_categories'))

        form.category_name.data = recipe_category.category_name
        form.details = form.user

        return render_template('chef/recipe_category.hml', action="Edit",
                               add_recipe_category=add_recipe_category, form=form,
                               recipe_category=recipe_category, title="Edit Recipe Category")

    

@chef.rout('/recipe_categories/delete<int:id2>', methods=['GET', 'POST'])

def delete_recipe_category(name):
    
    """
    Delete a recipe category from the database
    """
    chek_chef()

    delete_category(name)
    flash('You have successfully deleted a recipe category.')

    # redirect to the recipe categories page
    return render_template(title="Delete Recipe Category")
    return redirect(url_for('chef.list_recipe_categores'))
    

            

