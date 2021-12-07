from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def get_image_path(patient_id,mri_type,slice_num):
	pt = 'images/'+patient_id + '/' \
		+ mri_type +'/'\
		+ mri_type+'-slice'+str(slice_num).zfill(2)+'.png'
	return pt
# Create your views here.
def index(request):
	template = loader.get_template('show_mri/index.html')
	patient_list = {
	'00000','00001','00005','01010',
	}

	col1_image_path=[]
	col2_image_path=[]
	col3_image_path=[]
	col4_image_path=[]
	patient_id='00000'
	mri_type='FLAIR'

	for n in range(8):
		pt = get_image_path(patient_id,mri_type,n)
		col1_image_path.append(pt)
	for n in range(8,16):
		pt = get_image_path(patient_id,mri_type,n)
		col2_image_path.append(pt)
	for n in range(16,24):
		pt = get_image_path(patient_id,mri_type,n)
		col3_image_path.append(pt)
	for n in range(24,32):
		pt = get_image_path(patient_id,mri_type,n)
		col4_image_path.append(pt)

	context ={
		'patient_list' : patient_list,
		'col1_image_path':    col1_image_path,
		'col2_image_path':    col2_image_path,
		'col3_image_path':    col3_image_path,
		'col4_image_path':    col4_image_path,
	}

	return HttpResponse(template.render(context,request))