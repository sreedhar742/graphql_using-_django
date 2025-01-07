import graphene
from graphene_django import DjangoObjectType
from ingredients.models import Category, Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")
    
    def resolve_ingredients(self, info):
        return self.ingredients.all()

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")

    @classmethod
    def get_node(cls, info, id):
        try:
            return cls._meta.model.objects.get(id=id)
        except cls._meta.model.DoesNotExist:
            return None

class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        return [
            {
                'id': ingredient.id,
                'name': ingredient.name,
                'notes': ingredient.notes,
                'category': ingredient.category.id if ingredient.category else None
            }
            for ingredient in Ingredient.objects.select_related("category").all()
        ]

    def resolve_category_by_name(root, info, name):
        try:
            category = Category.objects.get(name=name)
            return {
                'id': category.id,
                'name': category.name,
                'ingredients': list(category.ingredients.values('id', 'name', 'notes'))
            }
        except Category.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)