#
# def insertUserMutationStr(email, name, phone, slackUserId, title):
#     query = """
#     mutation createUser($email: String, $name: String, $phone: String, $slackUserId: String, $title: String) {
#         insert_user_one(object: {email: $email, name: $name, phone: $phone, slackUserId: $slackUserId, title: $title}) {
#             email
#             id
#             name
#             phone
#             slackUserId
#             title
#         }
#     }
#     """
#     veriables = {
#         "email": email,
#         "name": name,
#         "phone": phone,
#         "slackUserId": slackUserId,
#         "title": title
#     }
#     return query, veriables
#
#
# def getUserBySlackUserId(slackUserId):
#     query = """
#     query getUserslackUserId($_eq: String) {
#         user(where: {slackUserId: {_eq: $_eq}}) {
#             email
#             id
#             name
#             phone
#             slackUserId
#             title
#         }
#     }
#     """
#     veriables = {
#         "_eq": slackUserId
#     }
#     return query, veriables
#
#
# def updateUser(id, email, name, phone, slackUserId, title):
#     query = """
#     mutation updateUser($id: Int!, $email: String, $name: String, $phone: String, $slackUserId: String, $title: String) {
#         update_user_by_pk(pk_columns: {id: $id}, _set: {email: $email, name: $name, phone: $phone, slackUserId: $slackUserId, title: $title}) {
#             email
#             id
#             name
#             phone
#             slackUserId
#             title
#         }
#     }
#     """
#     veriables = {
#         "id": id,
#         "email": email,
#         "name": name,
#         "phone": phone,
#         "slackUserId": slackUserId,
#         "title": title
#     }
#     return query, veriables
#
#
# def updateUserEmail(id, email):
#     query = """
#     mutation updateUser($id: Int!, $email: String) {
#         update_user_by_pk(pk_columns: {id: $id}, _set: {email: $email}) {
#             email
#             id
#             name
#             phone
#             slackUserId
#             title
#         }
#     }
#     """
#     veriables = {
#         "id": id,
#         "email": email
#     }
#     return query, veriables
#
#
# def updateUserName(id, name):
#     query = """
#     mutation updateUser($id: Int!, $name: String) {
#         update_user_by_pk(pk_columns: {id: $id}, _set: {name: $name}) {
#             email
#             id
#             name
#             phone
#             slackUserId
#             title
#         }
#     }
#     """
#     veriables = {
#         "id": id,
#         "name": name
#     }
#     return query, veriables
#
#
# def updateUserPhone(id, phone):
#     query = """
#     mutation updateUser($id: Int!, $phone: String) {
#         update_user_by_pk(pk_columns: {id: $id}, _set: {phone: $phone}) {
#             email
#             id
#             name
#             phone
#             slackUserId
#             title
#         }
#     }
#     """
#     veriables = {
#         "id": id,
#         "phone": phone,
#     }
#     return query, veriables
#
#
# def updateUserTitle(id, title):
#     query = """
#     mutation updateUser($id: Int!, $title: String) {
#         update_user_by_pk(pk_columns: {id: $id}, _set: {title: $title}) {
#             email
#             id
#             name
#             phone
#             slackUserId
#             title
#         }
#     }
#     """
#     veriables = {
#         "id": id,
#         "title": title
#     }
#     return query, veriables
#
