# Django GraphQL Cookbook

A sample Django application demonstrating GraphQL implementation using Graphene-Django.

## Project Overview

This project is a simple ingredient management system where ingredients belong to categories. It demonstrates how to:
- Set up GraphQL with Django
- Define GraphQL schemas
- Create data models
- Handle queries
- Return JSON responses

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install django graphene-django
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

## GraphQL API

Access the GraphQL interface at: `http://localhost:8000/graphql`

### Sample Queries

Query all ingredients:
```graphql
query {
  allIngredients {
    id
    name
    notes
    category {
      name
    }
  }
}
```

Query category by name:
```graphql
query {
  categoryByName(name: "Dairy") {
    id
    name
    ingredients {
      id
      name
      notes
    }
  }
}
```

## Project Structure

- `cookbook/` - Main project directory
  - `schema.py` - GraphQL schema definitions
  - `settings.py` - Django settings
  - `urls.py` - URL configurations
- `ingredients/` - Django app
  - `models.py` - Data models
  - `admin.py` - Admin interface configuration

## Models

- `Category`: Represents ingredient categories
  - Fields: name
- `Ingredient`: Represents individual ingredients
  - Fields: name, notes, category (ForeignKey)

## Technology Stack

- Django 5.1
- Graphene-Django
- SQLite3

## Contributing

Feel free to submit issues and enhancement requests.
