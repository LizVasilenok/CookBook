from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import engine, SessionLocal, Base

# Create tables
Base.metadata.create_all(bind=engine)

# Create a database session
db = SessionLocal()

# Check if there are any users
user_count = db.query(models.User).count()
if user_count == 0:
    print("Creating demo user...")
    user_data = schemas.UserCreate(
        username="demo",
        email="demo@example.com",
        password="password123"
    )
    user = crud.create_user(db=db, user=user_data)
    
    # Create some sample recipes
    print("Creating sample recipes...")
    recipes = [
        schemas.RecipeCreate(
            title="Spaghetti Carbonara",
            description="A classic Italian pasta dish",
            ingredients="Spaghetti, Eggs, Bacon, Parmesan cheese, Black pepper",
            instructions="1. Cook pasta al dente. 2. Cook bacon until crispy. 3. Beat eggs with cheese. 4. Mix everything together."
        ),
        schemas.RecipeCreate(
            title="Chicken Curry",
            description="A flavorful Indian-inspired curry",
            ingredients="Chicken, Onion, Garlic, Curry powder, Coconut milk, Tomatoes",
            instructions="1. Sauté onions and garlic. 2. Add chicken and brown. 3. Add spices and tomatoes. 4. Simmer with coconut milk."
        ),
        schemas.RecipeCreate(
            title="Greek Salad",
            description="A refreshing Mediterranean salad",
            ingredients="Cucumber, Tomatoes, Red onion, Feta cheese, Olives, Olive oil, Lemon juice",
            instructions="1. Chop vegetables. 2. Mix everything in a bowl. 3. Add cheese and olives. 4. Dress with olive oil and lemon juice."
        )
    ]
    
    for recipe_data in recipes:
        crud.create_user_recipe(db=db, recipe=recipe_data, user_id=user.id)
    
    print("Demo data created successfully!")
else:
    print("Demo data already exists. Skipping...")

# Close the session
db.close() 