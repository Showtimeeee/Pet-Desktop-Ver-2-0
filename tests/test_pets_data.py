import os
import pets_data

def test_pets_data():
    expected_pets = [
        ("Мопс", os.path.join('gifs', 'dasad.gif')),
        ("Пингвин", os.path.join('gifs', 'Z5cP.gif')),
        ("Пикачу", os.path.join('gifs', '6vw5.gif')),
        ("Котик", os.path.join('gifs', '6no.gif')),
        ("Гомер", os.path.join('gifs', '6md.gif')),
        ("НЛО", os.path.join('gifs', 'Vp3M.gif')),
        ("Феникс", os.path.join('gifs', 'ARm.gif')),
        ("Бабочка", os.path.join('gifs', '2N06.gif')),
        ("Приобрести", os.path.join('gifs', 'buy.gif'))
    ]
    assert pets_data.pets == expected_pets
