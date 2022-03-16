from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# Model Template
"""class MyModelName(models.Model):
    #A typical class defining a model, derived from the Model class.

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ...

    # Metadata
    class Meta:
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        #Returns the url to access a particular instance of MyModelName.
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        #String for representing the MyModelName object (in Admin site etc.).
        return self.my_field_name"""

#Pet model
#Fields: User, name, color, species, converted, level, health, strength,
#   defence, movement, custom, notes
class Pet(models.Model):
    #Add in the rest of the colors later
    EIGHTBIT = "8-Bit"
    AGUEENA = "Agueena"
    ALIEN = "Alien"
    BABY = "Baby"
    COLOR_CHOICES = (
        (EIGHTBIT, '8-Bit'),
        (AGUEENA, 'Agueena'),
        (ALIEN, 'Alien'),
        (BABY, 'Baby'),
    )
    #Add in the rest of the species later
    ACARA = "Acara"
    AISHA = "Aisha"
    BLUMAROO = "Blumaroo"
    BORI = "Bori"
    SPECIES_CHOICES = (
        (ACARA, 'Acara'),
        (AISHA, 'Aisha'),
        (BLUMAROO, 'Blumaroo'),
        (BORI, 'Bori'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pet")
    name = models.CharField(max_length=20, help_text="Enter pet's name.")
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default=EIGHTBIT)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES, default=ACARA)
    converted = models.BooleanField(default=True)
    level = models.IntegerField(default=1,
        verbose_name="Level",
        validators=[MinValueValidator(-1), MaxValueValidator(5000)])
    health = models.IntegerField(default=1,
        verbose_name="Hit Points",
        validators=[MinValueValidator(-1), MaxValueValidator(100000)])
    strength = models.IntegerField(default=1,
        verbose_name="Strength",
        validators=[MinValueValidator(-1), MaxValueValidator(100000)])
    defence = models.IntegerField(default=1,
        verbose_name="Defence",
        validators=[MinValueValidator(-1), MaxValueValidator(100000)])
    movement = models.IntegerField(default=1,
        verbose_name="Movement",
        validators=[MinValueValidator(-1), MaxValueValidator(100000)])
    custom = models.BooleanField(default=False)
    notes = models.TextField(max_length=500, blank=True, verbose_name="Notes",
        help_text="Add in any notes about the pet here.", default="None")
    verified = models.BooleanField(default=False)

    # Methods
    def get_absolute_url(self):
        #Returns the url to access a particular instance of Pet.
        return reverse('pet-detail', args=[str(self.id)])

    def __str__(self):
        #String for representing the Pet object.
        return f'{self.name} the {self.color} {self.species}'

#Shuffle model
#Fields: Host, shuffleType, potLimit, minPets, startTime, endTime

#Listing model
#Fields: User, pet, notes, expirationDate

#Trade subclass model
#Fields: openToAllOffers, openToConvertedsOnly, openToUCsOnly

#Shuffle Listing subclass model
#Fields: Shuffle, openToUCsOnly

#Offer model
#Fields: Trade, pets, user(?), notes, accpetedOffer

#Bid model
#Fields: ShuffleListing, pets, user(?), notes, winningBid

#Conversation model
#Fields: Sender, receiver, topic, unread

#Message model
#Fields: Conversation, author, content, sentDate, unread

#Notification model
#Fields: User, content, type, creationDate, unread

#Offer Notification subclass model
#Fields: Trade, offer

#Bid Notification subclass model
#Fields: ShuffleListing, bid

#Acceptance Notification model
#Fields: Listing, acceptedPet
