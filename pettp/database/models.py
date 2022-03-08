from django.db import models
from django.contrib.auth.models import User

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
#Variables: User, name, color, species, converted, level, health, strength,
#   defence, movement, custom, notes

#Shuffle model
#Variables: Host, shuffleType, potLimit, minPets, startTime, endTime

#Listing model
#Variables: User, pet, notes, expirationDate

#Trade subclass model
#Variables: openToAllOffers, openToConvertedsOnly, openToUCsOnly

#Shuffle Listing subclass model
#Variables: Shuffle, openToUCsOnly

#Offer model
#Variables: Trade, pets, user(?), notes, accpetedOffer

#Bid model
#Variables: ShuffleListing, pets, user(?), notes, winningBid

#Conversation model
#Variables: Sender, receiver, topic, unread

#Message model
#Variables: Conversation, author, content, sentDate, unread

#Notification model
#Variables: User, content, type, creationDate, unread

#Offer Notification subclass model
#Variables: Trade, offer

#Bid Notification subclass model
#Variables: ShuffleListing, bid

#Acceptance Notification model
#Variables: Listing, acceptedPet
