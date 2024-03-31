from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    """Thanks for the schema we don't have to check incoming data in our View"""
    id = fields.Str(dump_only=True)    # used only for sending back to the client
    name = fields.Str(required=True)    # is required for both serialization and deserialization
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class ItemUpdateSchema(Schema):    # both are optional
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
