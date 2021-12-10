from django.shortcuts import redirect

def redirect_view(request):
	response = redirect('/show_mri')
	return response