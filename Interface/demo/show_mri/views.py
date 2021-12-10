from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings

import csv
import os


def get_image_path(patient_id,mri_type,slice_num):
	pt = 'images/'+patient_id + '/' \
		+ mri_type +'/'\
		+ mri_type+'-slice'+str(slice_num).zfill(2)+'.png'
	return pt

def check_dir_exist(dname):
	path_to_dir = 'show_mri/static/images/'+dname
	if os.path.exists(os.path.join(settings.BASE_DIR ,path_to_dir )):
		return True
	else:
		return False

def get_patient_list():
	path_to_label = 'show_mri/static/show_mri/train_labels.csv'
	csvfile=open( os.path.join(settings.BASE_DIR ,path_to_label )   )
	a = csv.reader(csvfile)
	id_label = {}
	for v in a:
		if check_dir_exist(v[0]):
			id_label[v[0]] =v[1]
	csvfile.close()
	return id_label;


def mritype_radio_status(mri_type):
	if mri_type=='FLAIR':
		return ['checked','','','']
	if mri_type=='T1w':
		return ['','checked','','']
	if mri_type=='T2w':
		return ['','','checked','']
	if mri_type=='T1wCE':
		return ['','','','checked']
	return ['checked','','','']


def gen_image_num_list(sampling):
	if sampling=='m32':
		return range(16,48,1)
	else:  #sampling=='d32':
		return range(0,64,2)

# Create your views here.
def index(request):
	if request.method == 'POST':
		template = loader.get_template('show_mri/index.html')
		patient_id = request.POST['patient-id']
		mri_type = request.POST['MRI-type']	
		patient_dict = get_patient_list();
		patient_list = list(patient_dict.keys())

		col1_image_path=[]
		col2_image_path=[]
		col3_image_path=[]
		col4_image_path=[]
		#patient_id='00177'
		sta = request.POST['Sampling']
		image_num_list = gen_image_num_list(sta)
		score = patient_dict[patient_id]
		for n in range(8):
			pt = get_image_path(patient_id,mri_type,image_num_list[n])
			col1_image_path.append(pt)
		for n in range(8,16):
			pt = get_image_path(patient_id,mri_type,image_num_list[n])
			col2_image_path.append(pt)
		for n in range(16,24):
			pt = get_image_path(patient_id,mri_type,image_num_list[n])
			col3_image_path.append(pt)
		for n in range(24,32):
			pt = get_image_path(patient_id,mri_type,image_num_list[n])
			col4_image_path.append(pt)
		mri_radio = mritype_radio_status(mri_type)
		print('###########################################')
		print(sta)
		print('###########################################')

		context ={
			'patient_list' : patient_list,
			'MGMT_score'   : score,
			'col1_image_path':    col1_image_path,
			'col2_image_path':    col2_image_path,
			'col3_image_path':    col3_image_path,
			'col4_image_path':    col4_image_path,
			'radio_flair_checked'	 :    mri_radio[0],
			'radio_t1w_checked'	     :    mri_radio[1],
			'radio_t2w_checked'	     :    mri_radio[2],
			'radio_t1wce_checked'	 :    mri_radio[3],
			'PID'					 :  patient_id,
			'STA'					 :  sta,
		}

		pass
	else:
		template = loader.get_template('show_mri/index.html')
		patient_dict = get_patient_list();
		patient_list = list(patient_dict.keys())

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
			'MGMT_score'   : '0~1',
			'col1_image_path':    col1_image_path,
			'col2_image_path':    col2_image_path,
			'col3_image_path':    col3_image_path,
			'col4_image_path':    col4_image_path,
			'radio-flair-checked'	 :    'checked',
			'radio-t1w-checked'	 	:    '',
			'radio-t2w-checked'	 	:    '',
			'radio-t1wce-checked'	 :  '',
			'PID'					 :  '00000',
			'STA'					 :  'm32',
		}

	return HttpResponse(template.render(context,request))

def aboutpage(request):
	template = loader.get_template('show_mri/about.html')
	context = {  'YAY' : 'YAY',
			}

	return HttpResponse(template.render(context,request))