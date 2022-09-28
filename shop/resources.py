from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from .models import Product, Category


#class PersonDetailsAdminResource(resources.ModelResource):
    #user = fields.Field(column_name='user', attribute='user', widget=ForeignKeyWidget(User, field='username'))
    #country = fields.Field(column_name='country', attribute='country', widget=ForeignKeyWidget(Country, field='name'))
    #hobby = fields.Field(column_name='hobby', attribute='hobby', widget=ManyToManyWidget(Hobby, field='name'))
    #skill = fields.Field(column_name='skill', attribute='skill', widget=ManyToManyWidget(model=Skill,field='name'))


class CategoryResource(resources.ModelResource):

    class Meta:
        model=Category

        fields = ('id', 'name')


class ProductResource(resources.ModelResource):
    category_id = fields.Field(
        column_name='category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'name'))

    class Meta:
        model = Product



        fields = ('id','image', 'name','category_id','product_no','stock','price')

