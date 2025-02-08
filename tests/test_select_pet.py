from select_pet import update_speed_label

def test_update_speed_label():
    assert update_speed_label(10) == "Скорость пета: 10", "The speed label was not updated correctly"
    assert update_speed_label(20) == "Скорость пета: 20", "The speed label was not updated correctly"
