import sender_stand_request
import data


def get_kit_body(name):
 kit_body = {
     'name': name
 }
 return kit_body


def positive_assert(name, expected):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_kit_for_user(kit_body)
    assert response.status_code == 201
    assert name == expected


def test_1_letter_name_get_success_response():
    name = data.test_1_letter_positive
    expected = 'A'
    positive_assert(name, expected)


def test_511_letter_name_get_success_response():
    name = data.test_511_letter_positive
    expected = 'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC'
    positive_assert(name, expected)


def test_character_special_name_get_success_response():
    name = data.test_character_special_positive
    expected = '%$·"!"·'
    positive_assert(name, expected)


def test_spaces_in_name_get_success_response():
    name = data.test_spaces_positive
    expected = 'A aaa'
    positive_assert(name, expected)


def test_numbers_in_name_get_success_response():
    name = data.test_numbers_positive
    expected = '123'
    positive_assert(name, expected)


def negative_assert(name, expected):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_kit_for_user(kit_body)
    assert response.status_code == 400
    assert name == expected


def test_name_is_0_characters_get_error_response():
    name = data.test_0_characters_negative
    expected = ""
    negative_assert(name, expected)


def test_512_letter_in_name_get_error_response():
    name = data.test_512_letter_negative
    expected = 'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD'
    negative_assert(name, expected)


def test_parameter_not_in_solicitude_get_error_response():
    name = data.test_invalid_parameter
    expected = '{}'
    negative_assert(name, expected)


def test_number_in_name_get_error_response():
    name = data.test_number_negative
    expected = '123'
    negative_assert(name, expected)
