from django.core.mail import send_mail, BadHeaderError, send_mass_mail
# from django.core.mail .import send_mass_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def emailView(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			entreprise= form.cleaned_data['entreprise']
			ville_depart=form.cleaned_data['ville_depart']
			ville_arrivee=form.cleaned_data['ville_arrivee']
			date_depart=form.cleaned_data['date_depart']
			date_retour=form.cleaned_data['date_retour']
			nombre_passager=form.cleaned_data['nombre_passager']
			classe=form.cleaned_data['classe']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			ligne0="Une de société recherche le billet d'avion, ci-dessous le detail:"
			ligne1="Entreprise :"+entreprise
			ligne2="ville de depart : "+ville_depart
			ligne3="ville d'arrivée : "+ville_arrivee
			ligne4="date de depart : "+date_depart
			ligne5="date de retour : "+date_retour
			ligne6="nombre de passager : "+nombre_passager
			ligne7="Type de classe : "+classe
			# ligne8="Email du demandeur : "+from_email
			All=ligne0+"\n"+ligne1+"\n"+ligne2+"\n"+ligne3+"\n"+ligne4+"\n"+ligne5+"\n"+ligne6+"\n"+ligne7

			# collect=subject+entreprise+ville_depart+ville_arrivee+date_depart+date_retour+nombre_passager+classe+from_email)
			try:
				send_mail(subject, All+"\n"+message, from_email,['reservationbillet@approeco.net','heritier.bivuandu@approeco.net'])
				# datatuple = (
				# ('subject', 'message', 'from_email', ['reservationbillet@approeco.net']),
				# ('subject', 'message', 'from_email', ['heritier.bivuandu@approeco.net']),
						# )
				# send_mass_mail(datatuple)

			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('success')
	return render(request, "email.html", {'form': form})

def successView(request):
	return HttpResponse('Votre demande a été envoyer.')