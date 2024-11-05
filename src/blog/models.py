from datetime import datetime

from mongoengine import (DateTimeField, Document, EmbeddedDocument, EmbeddedDocumentField,
                         IntField, ListField, StringField)


class Blog(EmbeddedDocument):
    name = StringField(max_length=255)
    text = StringField()
    author = StringField(max_length=255)
    rating = IntField(default=10)


class Entity(Document):
    blog = ListField(EmbeddedDocumentField(Blog))
    timestamp = DateTimeField(default=datetime.now())
    last_update = DateTimeField(default=datetime.now())
    headline = StringField(max_length=255)

    def __str__(self):
        return f"{self.headline}"
