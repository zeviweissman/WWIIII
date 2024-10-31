from app.gql.Query import Query
from flask import Flask
from graphene import Schema
from flask_graphql import GraphQLView


schema = Schema(query=Query)
app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True
    )
)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)