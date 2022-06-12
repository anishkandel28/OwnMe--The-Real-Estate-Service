from django.forms import ModelForm
from .models import AddListing
from django import forms


#Create add listings form

class AddListingForm(ModelForm):
    class Meta:
					model=AddListing
					fields=('listing_type','name', 'price','bedroom', 'bathroom', 'kitchen', 'description','condition','owner', 'owner_docs_first','owner_docs_second','owner_docs_third', 'email', 'location','phone', 'listing_image_first','listing_image_second', 'listing_image_third')
					labels = {
			'listing_type': 'Listing Type',
			'name': 'Listing Name',
			'price': 'Listing Price',
			'bedroom': 'Number of Bedrooms',
			'bathroom': 'Number of Bathrooms',
			'kitchen': 'Number of Kitchens',
			'description': 'Listing Description',	
			'condition': 'Listing Condition',
			'owner': 'Listing Owner Name',
			'owner_doc_first': 'Owner Docs',	
			'owner_doc_second': 'Owner Docs',
			'owner_doc_third': 'Owner Docs',	
			'email': 'Email Address',
			'location': 'Listing Location',
			'phone': 'Contact Number',
			'listing_image_first': 'Listing Image',
			'listing_image_first': 'Listing Image',
			'listing_image_first':'Listing Image'
		}
					
					widgets = {
						'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'listings name'}),
						'price': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Listing price'}),
						'owner': forms.TextInput(attrs={'class':'form-control', 'placeholder':'owner name'}),
						'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
						'description':forms.TextInput(attrs={'class':'form-control', 'placeholder':'description', 'cols':80, 'rows':20}),
						'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'phone'}),
						'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'location'}),
		}