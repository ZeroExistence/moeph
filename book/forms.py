from django import forms

class SearchForm(forms.Form):
	q = forms.CharField(label='Search Book', max_length=100)

	def query(self):
		data = self.cleaned_data['q']
		return data