from django.test import TestCase

from database.models import (User, Pet)
from database.forms import (PetListingForm)

# Create your tests here.

class MyTestCase(TestCase):
    def setUp(self):
        #Create global users for testing
        user1 = User.objects.create_user(username="mike", password="example",
            email="example@text.com")
        self.global_user1 = user1


#Tests for the form to create an auction listing
class CreatePetFormTest(MyTestCase):
    #Test to ensure a user is able to create an pet listing providing all fields
    def test_valid_pet_creation(self):
        user = self.global_user1
        name = "MyPet"
        color = "8-Bit"
        species = "Acara"
        converted = True
        level = 1
        health = 10
        strength = 10
        defence = 10
        movement = 10
        custom = False
        notes = "Hello there"
        data = {'name': name, 'color': color, 'species' = species,
            'converted': converted, 'level': level, 'health': health,
            'strength': strength, 'defence': defence, 'movement': movement,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertTrue(form.is_valid())

    #Test to ensure a user is not able to create an pet listing if name is blank
    def test_invalid_pet_creation_no_name(self):
        user = self.global_user1
        color = "8-Bit"
        species = "Acara"
        converted = True
        level = 1
        health = 10
        strength = 10
        defence = 10
        movement = 10
        custom = False
        notes = "Hello there"
        data = {'color': color, 'species' = species,
            'converted': converted, 'level': level, 'health': health,
            'strength': strength, 'defence': defence, 'movement': movement,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertFalse(form.is_valid())

    #Test to ensure a user is not able to create an pet if name is longer than
    #20 characters
    def test_invalid_pet_creation_name_too_long(self):
        user = self.global_user1
        name = "MyPetIsSoSoSoPrettyPleaseOffer"
        color = "8-Bit"
        species = "Acara"
        converted = True
        level = 1
        health = 10
        strength = 10
        defence = 10
        movement = 10
        custom = False
        notes = "Hello there"
        data = {'name': name, 'color': color, 'species' = species,
            'converted': converted, 'level': level, 'health': health,
            'strength': strength, 'defence': defence, 'movement': movement,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertFalse(form.is_valid())

    #Test to ensure a user is not able to create an pet listing if name contains
    #characters other than letters and numbers
    def test_invalid_pet_creation_special_chracters(self):
        user = self.global_user1
        name = "My@Pet!"
        color = "8-Bit"
        species = "Acara"
        converted = True
        level = 1
        health = 10
        strength = 10
        defence = 10
        movement = 10
        custom = False
        notes = "Hello there"
        data = {'name': name, 'color': color, 'species' = species,
            'converted': converted, 'level': level, 'health': health,
            'strength': strength, 'defence': defence, 'movement': movement,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertFalse(form.is_valid())

    #Test to ensure a user is not able to create an pet listing if color is not submitted
    def test_invalid_pet_creation_color_missing(self):
        user = self.global_user1
        name = "MyPet"
        species = "Acara"
        converted = True
        level = 1
        health = 10
        strength = 10
        defence = 10
        movement = 10
        custom = False
        notes = "Hello there"
        data = {'name': name, 'species' = species,
            'converted': converted, 'level': level, 'health': health,
            'strength': strength, 'defence': defence, 'movement': movement,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertFalse(form.is_valid())

    #Test to ensure a user is not able to create an pet listing if species is not submitted
    def test_invalid_pet_creation_species_missing(self):
        user = self.global_user1
        name = "MyPet"
        color = "8-Bit"
        converted = True
        level = 1
        health = 10
        strength = 10
        defence = 10
        movement = 10
        custom = False
        notes = "Hello there"
        data = {'name': name, 'color': color,
            'converted': converted, 'level': level, 'health': health,
            'strength': strength, 'defence': defence, 'movement': movement,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertFalse(form.is_valid())

    #Test to ensure a user is able to create an pet listing if converted is unchecked
    def test_valid_pet_creation_unconverted(self):
        user = self.global_user1
        name = "MyPet"
        color = "8-Bit"
        species = "Acara"
        converted = False
        level = 1
        health = 10
        strength = 10
        defence = 10
        movement = 10
        custom = False
        notes = "Hello there"
        data = {'name': name, 'color': color, 'species' = species,
            'converted': converted, 'level': level, 'health': health,
            'strength': strength, 'defence': defence, 'movement': movement,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertTrue(form.is_valid())

    #Test to ensure a user is able to create an pet listing if level is not submitted
    def test_valid_pet_creation_level_missing(self):
        user = self.global_user1
        name = "My@Pet!"
        color = "8-Bit"
        species = "Acara"
        converted = False
        health = 10
        strength = 10
        defence = 10
        movement = 10
        custom = False
        notes = "Hello there"
        data = {'name': name, 'color': color, 'species' = species,
            'converted': converted, 'health': health,
            'strength': strength, 'defence': defence, 'movement': movement,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertTrue(form.is_valid())

    #Test to ensure a user is able to create an pet listing if health is not submitted
    def test_valid_pet_creation_health_missing(self):
        user = self.global_user1
        name = "My@Pet!"
        color = "8-Bit"
        species = "Acara"
        converted = False
        level = 1
        strength = 10
        defence = 10
        movement = 10
        custom = False
        notes = "Hello there"
        data = {'name': name, 'color': color, 'species' = species,
            'converted': converted, 'level': level,
            'strength': strength, 'defence': defence, 'movement': movement,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertTrue(form.is_valid())

    #Test to ensure a user is able to create an pet listing if strength is not submitted
    def test_valid_pet_creation_strength_missing(self):
        user = self.global_user1
        name = "My@Pet!"
        color = "8-Bit"
        species = "Acara"
        converted = False
        level = 1
        health = 10
        defence = 10
        movement = 10
        custom = False
        notes = "Hello there"
        data = {'name': name, 'color': color, 'species' = species,
            'converted': converted, 'level': level, 'health': health,
            'defence': defence, 'movement': movement,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertTrue(form.is_valid())

    #Test to ensure a user is able to create an pet listing if defence is not submitted
    def test_valid_pet_creation_defence_missing(self):
        user = self.global_user1
        name = "My@Pet!"
        color = "8-Bit"
        species = "Acara"
        converted = False
        level = 1
        health = 10
        strength = 10
        movement = 10
        custom = False
        notes = "Hello there"
        data = {'name': name, 'color': color, 'species' = species,
            'converted': converted, 'level': level, 'health': health,
            'strength': strength, 'movement': movement,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertTrue(form.is_valid())

    #Test to ensure a user is able to create an pet listing if movement is not submitted
    def test_valid_pet_creation_movement_missing(self):
        user = self.global_user1
        name = "My@Pet!"
        color = "8-Bit"
        species = "Acara"
        converted = False
        level = 1
        health = 10
        strength = 10
        defence = 10
        movement = 10
        custom = False
        notes = "Hello there"
        data = {'name': name, 'color': color, 'species' = species,
            'converted': converted, 'level': level, 'health': health,
            'strength': strength, 'defence': defence, 'movement': movement,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertTrue(form.is_valid())

    #Test to ensure a user is able to create an pet listing if custom is checked
    def test_valid_pet_creation_custom_checked(self):
        user = self.global_user1
        name = "My@Pet!"
        color = "8-Bit"
        species = "Acara"
        converted = False
        level = 1
        health = 10
        strength = 10
        defence = 10
        movement = 10
        custom = True
        notes = "Hello there"
        data = {'name': name, 'color': color, 'species' = species,
            'converted': converted, 'level': level, 'health': health,
            'strength': strength, 'defence': defence, 'movement': movement,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertTrue(form.is_valid())

    #Test to ensure a user is able to create an pet listing if notes are not submitted
    def test_valid_pet_creation_level_missing(self):
        user = self.global_user1
        name = "My@Pet!"
        color = "8-Bit"
        species = "Acara"
        converted = False
        level = 1
        health = 10
        strength = 10
        defence = 10
        movement = 10
        custom = False
        data = {'name': name, 'color': color, 'species' = species,
            'converted': converted, 'level': level, 'health': health,
            'strength': strength, 'defence': defence, 'movement': movement,
            'custom': custom}
        form = PetListingForm(data=data, user=user)
        self.assertTrue(form.is_valid())

    #Test to ensure a user is not able to create an pet listing if any of the
    #integer fields are negative
    def test_invalid_pet_creation_negative_ints(self):
        user = self.global_user1
        name = "My@Pet!"
        color = "8-Bit"
        species = "Acara"
        converted = False
        level = 1
        health = 10
        strength = 10
        defence = 10
        movement = 10
        custom = False
        notes = "Hello there"
        data = {'name': name, 'color': color, 'species' = species,
            'converted': converted, 'level': -1, 'health': health,
            'strength': strength, 'defence': defence, 'movement': movement,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertFalse(form.is_valid())
        data = {'name': name, 'color': color, 'species' = species,
            'converted': converted, 'level': level, 'health': -1,
            'strength': strength, 'defence': defence, 'movement': movement,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertFalse(form.is_valid())
        data = {'name': name, 'color': color, 'species' = species,
            'converted': converted, 'level': level, 'health': health,
            'strength': -2, 'defence': defence, 'movement': movement,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertFalse(form.is_valid())
        data = {'name': name, 'color': color, 'species' = species,
            'converted': converted, 'level': level, 'health': health,
            'strength': strength, 'defence': -3, 'movement': movement,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertFalse(form.is_valid())
        data = {'name': name, 'color': color, 'species' = species,
            'converted': converted, 'level': level, 'health': health,
            'strength': strength, 'defence': defence, 'movement': -4,
            'custom': custom, 'notes': notes}
        form = PetListingForm(data=data, user=user)
        self.assertFalse(form.is_valid())

    #Test to ensure that name field help text is correct
    def test_pet_creation_name_help_text(self):
        user = self.global_user1
        form = PetListingForm(user=user)
        self.assertEqual(form.fields['name'].help_text, "Enter pet's name.")

    #Test to ensure that notes field help text is correct
    def test_pet_creation_note_help_text(self):
        user = self.global_user1
        form = PetListingForm(user=user)
        self.assertEqual(form.fields['notes'].help_text, "Add in any notes about the pet here.")
