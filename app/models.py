from flask_login import UserMixin
from wekzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class User(object):
    """
    Create a User table
    """

    user_id = 0
    
    def __init__(self):
        self.email=""
        self.username=""
        self.last_name=""
        self.password_hash=""
        user_id += 1
    

    def add_user(self,  email,username,last_name,password):
        self.email=email
        self.username=username
        self.last_name=last_name
        self.password_hash=password
       
        

  


class RecipeCategory(object):
    
   
    """
    Create a Recipe Category data source
    """

    def __init__(self):
        
        categories ={}
    
    def add_category(self,name,description):
        self.categories[name]=description

    def delete_category(self,name):
        if name is in self.categories:
            self.categories.__delete__(name)

   
class Recipe(object):
    
    """
    Create a Recipe data source
    """

    def __init__(self):
        recipes = {}

    def add_recipe(self,name,ingredient,steps,quantity,people,cook,category):
        self.recipes[name]=[name,ingredient,steps,quantity,people,cook,category]

    def delete_recipe(self,name):
        if name is in self.recipes:
            self.recipes.__delete__(name)
            
        

   


    
        
    
    
    
        
    

    
