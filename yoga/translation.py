from modeltranslation.translator import TranslationOptions, translator



from shop.models import Category,Product



class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)



class ProductTranslationOptions(TranslationOptions):
    fields = ("name",)



translator.register(Category,CategoryTranslationOptions)
translator.register(Product,ProductTranslationOptions)
