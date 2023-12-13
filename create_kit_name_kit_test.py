import sender_stand_request
import data
#функция на замену значения  впараметре name
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

#функция для позитивной проверки
def positive_assert(name):
    user_token = sender_stand_request.get_new_user_token(data.body_of_user)
    kit_body = get_kit_body(name)
    kit_responce = sender_stand_request.post_new_client_kit(kit_body, user_token)
    assert kit_responce.status_code == 201
    assert kit_responce.json()["name"] == name

#функция для негативной проверки
def negative_assert(name):
    user_token = sender_stand_request.get_new_user_token(data.body_of_user)
    kit_body = get_kit_body(name)
    kit_responce = sender_stand_request.post_new_client_kit(kit_body, user_token)
    assert kit_responce.status_code == 400

#проверки по чек-листу

# Допустимое количество символов (1):
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

# Допустимое количество символов (511):
def test_create_kit_511_letter_in_name_get_success_responce():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Количество символов меньше допустимого (0):
def test_create_kit_0_symbol_in_name_get_mistake():
    negative_assert("")

# Количество символов больше допустимого (512)
def test_create_kit_512_symbol_in_name_get_mistake():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Допустимые символы (латиница)
def test_create_kit_eng_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Допустимые символы (кирилица)
def test_create_kit_rus_letter_in_name_get_success_response():
    positive_assert("Мария")

# Допустимые символы (спецсимволы)
def test_create_kit_special_characters_in_name_get_success_response():
    positive_assert(" \"№%@ \",")

# Допустимые символы (пробел)
def test_create_kit_space_in_name_get_success_response():
    positive_assert("Человек и КО")

# Допустимые символы (цифры)
def test_create_kit_number_get_success_response():
    positive_assert("123")

# Проверка отсутсвия параметра
def test_create_kit_no_parameter_in_name_get_mistake():
    kit_body = {}
    user_token = sender_stand_request.get_new_user_token(data.body_of_user)
    kit_responce = sender_stand_request.post_new_client_kit(kit_body, user_token)
    assert kit_responce.status_code == 400

# Недопустимый тип параметра (число)
def test_create_kit_different_parameter_type_in_name_get_mistake():
    negative_assert(123)