import order_create


def test_order_and_track_create():
    response = order_create.get_track()
    return response.status_code == 200


#Шешин Евгений Диплом 15_qa-plus_project_venus