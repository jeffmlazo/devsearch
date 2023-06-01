# from .models import ModelName

# # all() - Retrieves all objects from table
# querySet = ModelName.objects.all()

# # get(attribute='value') - Retrieve a single object based on matched attribute
# queryItem = ModelName.objects.get(attribute='value')

# # filter(attribute='value') - Returns all items from the table that match a particular attribute value
# querySet = ModelName.object.filter(attribute='value').filter(attribute__startswith='value').filter(
#     attribute__contains='value').filter(attribute__icontains='value').filter(attribute__gt='value').filter(attribute__gte='value').filter(attribute__lt='value').filter(attribute__lte='value')

# # exlude(attribute='value') - Excludes any object matching a particular filter
# querySet = ModelName.object.exclude(attribute='value')

# # order_by() - Order a queryset by a particular attribute. Multiple parameters are allowed
# querySet = ModelName.object.filter(
#     title="first project").order_by('value1', 'value2')

# # order can be reversed by adding "-" before the attribute name
# querySet = ModelName.object.filter(
#     title="first project").order_by('-value1', '-value2')

# # create() - Create an instance of a model
# item = ModelName.objects.create(attribute='value')

# # save() - Save changes made to a particular object
# item = ModelName.objects.get(attribute='value')
# item.title = "New Value"
# item.save()

# # delete() - Deletes a particular object
# item = ModelName.objects.last()
# item.delete()

# # Query Models Children
# item = ModelName.object.first()
# item.childmodel_set.all()

# # Query ManyToMany Fields
# item = ModelName.object.first()
# item.relationshipname.all()

# # Add ManyToMany Field
# item = ModelName.object.first()
# otherItem = OtherModule.objects.create(attribute='value')
# item.relationshipname.add(otheritem)
