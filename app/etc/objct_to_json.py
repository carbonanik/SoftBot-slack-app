import json
from queue import Empty


def convert_obj(obj):
    jsonStr = json.dumps(obj)
    return jsonStr, 100, "sadhfkjas"

print(convert_obj(
{'errors': [{'extensions': {'code': 'unexpected', 'internal': {'arguments': ['(Oid 114,Just ("{\\"x-hasura-role\\":\\"admin\\"}",Binary))', '(Oid 25,Just ("U02NVERT65B",Binary))'], 'error': {'description': None, 'exec_status': 'FatalError', 'hint': None, 'message': 'column user.slackId does not exist', 'status_code': '42703'}, 'prepared': True, 'statement': 'SELECT  coalesce(json_agg("root" ), \'[]\' ) AS "root" FROM  (SELECT  row_to_json((SELECT  "_e"  FROM  (SELECT  "_root.base"."email" AS "email", "_root.base"."id" AS "id", "_root.base"."name" AS "name", "_root.base"."phone" AS "phone", "_root.base"."slackId" AS "slackId", "_root.base"."title" AS "title"       ) AS "_e"      ) ) AS "root" FROM  (SELECT  *  FROM "public"."user"  WHERE (("public"."user"."slackId") = (($2)::text))     ) AS "_root.base"      ) AS "_root"       /* request_id=e25f1f24a986f0caceb53c7181e31648, field_name=user, parameterized_query_hash=18f103b87ae4a44fe306bd0ef6b30e1d14301917 */'}, 'path': '$'}, 'message': 'database query error'}]}
))


# name = ""
# name2 = "b"

# name3 = name if name else name2

# print(name3)

{
    'errors': [
        {
            'extensions': {
                'code': 'unexpected', 
                'internal': {
                    'arguments': [
                        '(Oid 114,Just ("{\\"x-hasura-role\\":\\"admin\\"}",Binary))', 
                        '(Oid 25,Just ("U02NVERT65B",Binary))'
                    ], 
                    'error': {
                        'description': None, 
                        'exec_status': 'FatalError', 
                        'hint': None, 
                        'message': 'column user.slackId does not exist', 
                        'status_code': '42703'
                    }, 
                    'prepared': True, 
                    'statement': 'SELECT  coalesce(json_agg("root" ), \'[]\' ) AS "root" FROM  (SELECT  row_to_json((SELECT  "_e"  FROM  (SELECT  "_root.base"."email" AS "email", "_root.base"."id" AS "id", "_root.base"."name" AS "name", "_root.base"."phone" AS "phone", "_root.base"."slackId" AS "slackId", "_root.base"."title" AS "title"       ) AS "_e"      ) ) AS "root" FROM  (SELECT  *  FROM "public"."user"  WHERE (("public"."user"."slackId") = (($2)::text))     ) AS "_root.base"      ) AS "_root"       /* request_id=e25f1f24a986f0caceb53c7181e31648, field_name=user, parameterized_query_hash=18f103b87ae4a44fe306bd0ef6b30e1d14301917 */'}, 'path': '$'}, 'message': 'database query error'
                }
            ]
}