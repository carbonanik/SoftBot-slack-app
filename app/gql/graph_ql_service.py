# from python_graphql_client import GraphqlClient
#
#class GraphQLService:
#
#    instance = None
#    client: GraphqlClient = GraphqlClient(
#        headers= {
#            "content-type": "application/json",
#            "x-hasura-admin-secret": "EPgRzP2u3Yi9PPCx5tWMyDS5cOt6Yfzn4P7ECwKWCWszqPDbIAOixdoJdAD3zCmd"
#        },
#        endpoint="https://fit-hagfish-80.hasura.app/v1/graphql")
#
#    def __new__(cls, *args, **kwargs):
#        if not isinstance(cls.instance, cls):
#            cls.instance = object.__new__(cls)
#        return cls.instance
#
#    def preformQuery(self, query, variables) :
#        data = self.client.execute(query=query, variables=variables)
#        return data
