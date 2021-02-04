from ariadne import ObjectType

query = ObjectType("Query")


@query.field("hello")
def hello(_, info):
    return "hello"
