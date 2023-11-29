import sender_stand_request
import data

def get_kit_body(name):

    kit_body = {
        'name': "Mi conjunto"
    }

    return kit_body


def positive_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_kit_for_user(kit_body)

    assert response.status_code == 201


def test_1_letter_name_get_success_response():
    name = "data.test_1_letter_positive"
    positive_assert(data.test_1_letter_positive)

    assert data.test_1_letter_positive == 'A'


def test_511_letter_name_get_success_response():
    name = "data.test_511_letter_positive"
    positive_assert(data.test_511_letter_positive)

    assert data.test_511_letter_positive == 'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC'

def test_character_special_name_get_success_response():
    name = "data.test_character_special_positive"
    positive_assert(data.test_character_special_positive)

    assert data.test_character_special_positive == '%$·"!"·'

def test_spaces_in_name_get_success_response():
    name = "data.test_spaces_positive"
    positive_assert(data.test_spaces_positive)

    assert data.test_spaces_positive == 'A aaa'

def test_numbers_in_name_get_success_response():
    name = "data.test_numers_positive"
    positive_assert(data.test_numers_positive)

    assert data.test_numers_positive == '123'



def negative_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_kit_for_user(kit_body)

    assert response.status_code == 400
def test_name_is_0_characters_get_error_response():
    name = "data.test_0_characters_negative"
    negative_assert(data.test_0_characters_negative)

    assert data.test_0_characters_negative == ""

def test_512_letter_in_name_get_error_response():
    name = "data.test_512_letter_negative"
    negative_assert(data.test_512_letter_negative)

    assert data.test_512_letter_negative == 'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")'
def test_parameter_not_in_solicitude_get_error_response():
    name = "data.test_invalid_parameter"
    negative_assert(data.test_invalid_parameter)

    assert data.test_invalid_parameter == '{}'

def test_number_in_name_get_error_response():
    name = "data.test_number_negative"
    negative_assert(data.test_number_negative)

    assert data.test_number_negative == '123'