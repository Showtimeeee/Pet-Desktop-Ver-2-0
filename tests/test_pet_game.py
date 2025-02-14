from pet_game import Pet

def test_pet_initialization():
    pet = Pet('gifs/dasad.gif', 10)
    assert pet.speed == 10
    assert pet.gif_path == 'gifs/dasad.gif'
    pet.window.destroy()

def test_pet_speed_up():
    pet = Pet('gifs/dasad.gif', 10)
    pet.speed_up(None)
    assert pet.speed == 5
    pet.window.destroy()

def test_pet_slow_down():
    pet = Pet('gifs/dasad.gif', 5)
    pet.slow_down(None)
    assert pet.speed == 10
    pet.window.destroy()

def test_quit_program():
    pet = Pet('gifs/dasad.gif', 10)
    pet.quit_program()
    assert pet.window.winfo_exists() == 0

def test_frame_change():
    pet = Pet('gifs/dasad.gif', 10)
    initial_frame_index = pet.frame_index
    pet.changetime(pet.moveright)
    assert pet.frame_index != initial_frame_index
    pet.window.destroy()
