from pydantic import BaseModel, validator

from ._commons import Image, MultiLanguageText
from ._mixins import DBModel



class SellerTranslations(BaseModel):
    title: MultiLanguageText = None
    description: MultiLanguageText = None


class SellerBase(BaseModel):
    name: str = None
    translations: SellerTranslations = None
    logo: Image = None

    class Config:
        schema_extra = {
            'example': {
                'name': 'My company',
                'translations': {
                    'title': {
                        'en': 'My awesome company',
                        'fr': 'Ma super entreprise',
                        'es': 'Mi increible compañia'
                    },
                    'description': {
                        'en': 'Our motto: We are great, you are great!',
                        'fr': 'Notre devise : On est super, vous êtes super !',
                        'es': 'Nuestro lema: ¡Somos geniales, tú eres genial!'
                    }
                },
                'logo': {
                    'url': 'https://images.unsplash.com/photo-1531973576160-7125cd663d86?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80',
                    'description': {
                        'en': 'My company logo',
                        'fr': 'Logo de mon entreprise',
                        'es': 'El logo de mi empresa'
                    }
                }
            }
        }


class SellerToInsert(SellerBase):
    name: str


class SellerToUpdate(SellerBase):
    @validator('name')
    def prevent_none(cls, v):
        assert v is not None and v != '', 'Name may not be None or empty string'
        return v


class SellerOut(DBModel, SellerBase):
    pass
