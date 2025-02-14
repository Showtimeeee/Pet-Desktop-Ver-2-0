from select_pet import update_speed_label


def test_update_speed_label():
    assert update_speed_label(10) == "Скорость питомца: 10"
    assert update_speed_label(20) == "Скорость питомца: 20"
    assert update_speed_label(1) == "Скорость питомца: 1"
    assert update_speed_label(50) == "Скорость питомца: 50"
    assert update_speed_label(0) == "Скорость питомца: 0"
    assert update_speed_label(25) == "Скорость питомца: 25"
    assert update_speed_label(33) == "Скорость питомца: 33"

def test_update_speed_label_boundary_values():
    assert update_speed_label(-1) == "Скорость питомца: -1"
    assert update_speed_label(51) == "Скорость питомца: 51"
    assert update_speed_label(999) == "Скорость питомца: 999"
    assert update_speed_label(1000) == "Скорость питомца: 1000"

###
def test_update_speed_label_special_characters():
    assert update_speed_label("!@#") == "Скорость питомца: !@#"
    assert update_speed_label("") == "Скорость питомца: "
