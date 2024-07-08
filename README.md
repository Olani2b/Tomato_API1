# Tomato API

Welcome to the Tomato API project! This application provides a simple and efficient way to manage restaurants, recipes, and ingredients. The API is built using Django and Django REST Framework, and it includes comprehensive API documentation and Docker support.

## Table of Contents

- [About the App](#about-the-app)
- [Models](#models)
- [API Endpoints](#api-endpoints)
- [Setup and Installation](#setup-and-installation)
- [Running with Docker](#running-with-docker)
- [Accessing the APIs](#accessing-the-apis)
- [API Documentation](#api-documentation)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## About the App

The Tomato API allows users to create and manage restaurants, recipes, and ingredients. Each restaurant can have multiple recipes, and each recipe can include multiple ingredients. The application provides endpoints to filter data based on specific criteria, such as recipes containing a specific ingredient or restaurants offering a specific recipe.

## Models

### Ingredient

Represents an individual ingredient.

- **Fields:**
  - `name`: A string representing the name of the ingredient.

### Recipe

Represents a recipe, which can have multiple ingredients.

- **Fields:**
  - `name`: A string representing the name of the recipe.
  - `ingredients`: A many-to-many relationship to the `Ingredient` model.

### Restaurant

Represents a restaurant, which can have multiple recipes.

- **Fields:**
  - `name`: A string representing the name of the restaurant.
  - `recipes`: A many-to-many relationship to the `Recipe` model.

## API Endpoints

### Ingredient Endpoints

- **List all ingredients:**
  - `GET /api/ingredients/`
- **Create a new ingredient:**
  - `POST /api/ingredients/`
- **Retrieve an ingredient:**
  - `GET /api/ingredients/{id}/`
- **Update an ingredient:**
  - `PUT /api/ingredients/{id}/`
- **Delete an ingredient:**
  - `DELETE /api/ingredients/{id}/`
- **List ingredients by recipe name:**
  - `GET /api/ingredients/by-recipe/{recipe_name}/`
- **List ingredients by restaurant name:**
  - `GET /api/ingredients/by-restaurant/{restaurant_name}/`

### Recipe Endpoints

- **List all recipes:**
  - `GET /api/recipes/`
- **Create a new recipe:**
  - `POST /api/recipes/`
- **Retrieve a recipe:**
  - `GET /api/recipes/{id}/`
- **Update a recipe:**
  - `PUT /api/recipes/{id}/`
- **Delete a recipe:**
  - `DELETE /api/recipes/{id}/`
- **List recipes by restaurant name:**
  - `GET /api/recipes/by-restaurant/{restaurant_name}/`
- **List recipes by ingredient name:**
  - `GET /api/recipes/by-ingredient/{ingredient_name}/`

### Restaurant Endpoints

- **List all restaurants:**
  - `GET /api/restaurants/`
- **Create a new restaurant:**
  - `POST /api/restaurants/`
- **Retrieve a restaurant:**
  - `GET /api/restaurants/{id}/`
- **Update a restaurant:**
  - `PUT /api/restaurants/{id}/`
- **Delete a restaurant:**
  - `DELETE /api/restaurants/{id}/`
- **List restaurants by recipe name:**
  - `GET /api/restaurants/by-recipe/{recipe_name}/`

## Setup and Installation

### Prerequisites

- Python 3.x
- Docker (optional, for containerization)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Olani2b/Tomato_API1.git
   cd <repository_directory>
2. **Create a virtual environment and activate it:**
   python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

