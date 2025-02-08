from pet_game import Pet

def test_pet_initialization():
    pet = Pet('gifs/dasad.gif', 10)
    assert pet.speed == 10, "The initial speed is not set correctly"
    assert pet.gif_path == 'gifs/dasad.gif', "The GIF path is not set correctly"
    pet.window.destroy()

def test_pet_speed_up():
    pet = Pet('gifs/dasad.gif', 10)
    pet.speed_up(None)
    assert pet.speed == 5, "The speed did not increase correctly"
    pet.window.destroy()

def test_pet_slow_down():
    pet = Pet('gifs/dasad.gif', 5)
    pet.slow_down(None)
    assert pet.speed == 10, "The speed did not decrease correctly"
    pet.window.destroy()
