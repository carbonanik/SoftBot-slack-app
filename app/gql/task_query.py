def insert_task(title, description, dueDate, userId):

    query = """
    mutation insertTask($description: String, $dueDate: timestamp, $title: String, $userId: Int) {
        insert_task_one(object: {description: $description, dueDate: $dueDate, title: $title, userId: $userId}) {
            description
            dueDate
            id
            title
            userId
        }
    }
    """
    veriables = {
        "description": description,
        "dueDate": dueDate,  # 2022-09-08
        "title": title,
        "userId": userId
    }
    return query, veriables


def get_all_task():
    query = """
    query getAllTask {
        task {
            description
            dueDate
            id
            title
            userId
        }
    }

    """
    veriables = {}
    return query, veriables
