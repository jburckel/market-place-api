from ._commons import TreeObjectIdStr

class ProductCategoryTranslations(BaseModel):
    name: MultiLanguageText = None
    description: MultiLanguageTest = None


class ProductCategoryBase(BaseModel):
    parentProductCategoryId: TreeObjectIdStr = None # None is root category
    name: str = None
    translations: ProductCategoryTranslations = None
    images: List[Image] = None


class ProductCategoryToInsert(BaseModel):
    name: str


class ProductCategoryToUpdate(BaseModel):
    pass


class ProductCategoryOut(DBModel, ProductCategoryBase):
    pass
