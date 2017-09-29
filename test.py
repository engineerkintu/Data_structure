import os

from flask import abort, url_for

from app.models import User, Recipe, RecipeCategory

class TestModels(TestBase):

    def test_add_user(self):
        """
        Test number of records in User table
        """
        user = User
        user.add_user("gh@g.com","hj","lk","gdtt")     
        self.assertEqual(user.email, "gh@g.com")

    def test_add_recipe_category(self):
        """
        Test number of records in Recipe table
        """
        category = RecipeCategory
        

        # create test recipe_category
        category.add_category("Rolex","Chapati and egg")

        self.assertEqual(category.__len__(), 1)

    def test_add_recipe(self):
        """
        Test number of records in Recipes table
        """

        # create test recipe
        recipe = Recipe
        recicipeadd_recipe("Mugoyo","Sweet potato and beans","boil and mingle", "4 plates","4 people",1,2)

        self.assertEqual(recipe.__len__(), 1)

  
if __name__ == '__main__':
    unittest.main()
