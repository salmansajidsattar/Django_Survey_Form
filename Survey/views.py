from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from .models import Question,Modern_Home,Sales_team,Finished_Inventory,Builder_Data
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from json import loads as jsonloads
from PIL import Image as Img
import PIL
import os
from django.template.loader import get_template 
from django.template import Context
import numpy as np
import json
from Survey import cuatom_function
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer,Image
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
import reportlab
from Survey import data,helper
from Django_Survey_Form import settings
from reportlab.lib.utils import ImageReader
from django.core.files.uploadedfile import TemporaryUploadedFile
import shutil
from reportlab.lib import utils
import tempfile
from io import BytesIO

Question_num=Question.objects.all()
Modern_num=Modern_Home.objects.all()
Sales_team_num=Sales_team.objects.all()
Finished_Inventory_num=Finished_Inventory.objects.all()
temp_dir = None
pdf_file_temp_dir=None
builder=None
inspected_by=None
def index(request):
    global temp_dir
    temp_dir=tempfile.mkdtemp()
    data={"Question":Question_num,"Modern_Home":Modern_num,"Sales_team":Sales_team_num,"Finished_Inventory":Finished_Inventory_num}
    return render(request,'index.html',context=data)


@csrf_exempt
def Temp_data(request):
    global temp_dir
    print("temp_dir",temp_dir)
    if request.method == 'POST':
        front_images_pixel=[]
        address=request.POST.get('address')
        front_images=request.FILES.getlist('front_images')
        # print("len(front_images)",len(front_images))
        if(len(front_images)!=0):
            for image_path in front_images:
                temp_file_path = image_path.temporary_file_path()
                print(temp_file_path)
                destination_path = os.path.join(temp_dir+'/temp_images/'+str(address)+'/front_images',str(image_path.name))
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(temp_file_path, destination_path)

        front_notes=request.POST.get('front_notes')
        Interior_images=request.FILES.getlist('Interior_images')
        if(len(Interior_images)!=0):
            for image_path in Interior_images:
                temp_file_path = image_path.temporary_file_path()
                print(temp_file_path)
                destination_path = os.path.join(temp_dir+'/temp_images/'+str(address)+'/Interior_images',str(image_path.name))
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(temp_file_path, destination_path)

        Interior_notes=request.POST.get('Interior_notes')
        Back_images=request.FILES.getlist('Back_images')
        if(len(Back_images)!=0):
            for image_path in Back_images:
                temp_file_path = image_path.temporary_file_path()
                print(temp_file_path)
                destination_path = os.path.join(temp_dir+'/temp_images/'+str(address)+'/Back_images',str(image_path.name))
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                shutil.copy(temp_file_path, destination_path)
        Back_notes=request.POST.get('Back_notes')
        Summary=request.POST.get('Summary')
        settings.Individual_Inventory_Homes.append({'address':address,
                                        "front_notes": front_notes,
                                        "Interior_notes":Interior_notes,
                                        "Back_notes":Back_notes,
                                        "Summary":Summary})
        return HttpResponse('mydta done')
        

def return_list(enter_list):
    list_Temp=[]
    for i in enter_list:
        list_Temp.append(enter_list[i])
    return  list_Temp


def get_image(path, width=1):
    img = utils.ImageReader(path)
    iw, ih = img.getSize()
    aspect = ih / float(iw)
    return Image(path, width=width, height=(width * aspect))

@csrf_exempt
def PDF_FILE(request):
    # print("enter in the PDF_FILE")
    if request.method == 'POST':
        global builder
        global inspected_by
        inspected_by=request.POST.get('inspected_by')
        enter_date=request.POST.get('enter_date')
        builder=request.POST.get('Builder')
        Community=request.POST.get('Community')
        Q_Notes=request.POST.get('Q_Notes')
        S_Notes=request.POST.get('S_Notes')
        H_Notes=request.POST.get('H_Notes')
        F_Notes=request.POST.get('F_Notes')
        Summary_Notes=request.POST.get('Summary_Notes')
        Question_list = json.loads(request.POST.get('Question'))
        Home_list=json.loads(request.POST.get('Home'))
        sales_list=json.loads(request.POST.get('sales'))
        inventory_list=json.loads(request.POST.get('inventory'))
        img_path_Q,img_descrip_Q=cuatom_function.get_image_link('imageFile_Q',7,'imageDescription_Q')
        img_path_H,img_descrip__H=cuatom_function.get_image_link('imageFile_H',15,'imageDescription_H')
        img_path_S,img_descrip_S=cuatom_function.get_image_link('imageFile_S',7,'imageDescription_S')
        img_path_F,img_descrip_F=cuatom_function.get_image_link('imageFile_F',7,'imageDescription_F')
        Data=Builder_Data(Builder_name=builder,Community=Community,Inspected_by=inspected_by,date_time=enter_date,Summary_Description=Summary_Notes)
        Data.save()
        name_Q=[]
        des_Q=[]
        if (img_path_Q!=None):
            for index,path in enumerate(img_path_Q):
                try:
                    if(request.FILES[path]):
                        image_append=request.FILES[path]
                        name_Q.append(image_append)
                        if(request.POST.get(img_descrip_Q[index])):
                            des_Q.append(request.POST.get(img_descrip_Q[index]))
                        else:
                            des_Q.append("No Description")
                except Exception:
                        pass
        name_H=[]
        des_H=[]
        path=None
        if (img_path_H!=None):
            for index,path in enumerate(img_path_H):
                try:
                    if(request.FILES[path]):
                        image_append=request.FILES[path]
                        name_H.append(image_append)
                        if(request.POST.get(img_descrip__H[index])):
                            des_H.append(request.POST.get(img_descrip__H[index]))
                        else:
                            des_H.append("No Description")
                except Exception:
                        pass
        name_S=[]
        des_S=[]
        path=None
        if (img_path_S!=None):
            for index,path in enumerate(img_path_S):
                try:
                    if(request.FILES[path]):
                        image_append=request.FILES[path]
                        name_S.append(image_append)
                        if(request.POST.get(img_descrip_S[index])):
                            des_S.append(request.POST.get(img_descrip_S[index]))
                        else:
                            des_S.append("No Description")
                except Exception:
                        pass
        name_F=[]
        des_F=[]
        path=None
        if (img_path_F!=None):
            for index,path in enumerate(img_path_F):
                try:
                    if(request.FILES[path]):
                        image_append=request.FILES[path]
                        name_F.append(image_append)
                        if(request.POST.get(img_descrip_F[index])):
                            des_F.append(request.POST.get(img_descrip_F[index]))
                        else:
                            des_F.append("No Description")
                except Exception:
                        pass
        create_pdf(Builder_name=builder,Community_name=Community,
                Inspected_by=inspected_by,date=enter_date,summary=Summary_Notes,Q_summary=Q_Notes,S_summary=S_Notes,
            F_summary=F_Notes,H_summary=H_Notes,
            Answer_Q=Question_list,Answer_H=Home_list,Answer_S=sales_list,Answer_F=inventory_list,
            img_path_Q=name_Q,des_Q=des_Q,name_H=name_H,des_H=des_H,name_S=name_S,des_S=des_S,name_F=name_F,des_F=des_F)
        # global pdf_buffer
        # pdf_value = pdf_buffer.getvalue()
        # # pdf_buffer.close()
        # response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = f'attachment; filename="{builder}-{inspected_by}_data.pdf"'
        # response.write(pdf_value)
        # return response
        return JsonResponse({'success': True, 'redirect_url': '/return_pdf/'})


def return_pdf(request):
    global builder
    global inspected_by
    global pdf_buffer
    pdf_value = pdf_buffer.getvalue()
    # pdf_buffer.close()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{builder}-{inspected_by}.pdf"'
    response.write(pdf_value)
    return response

def create_pdf(Builder_name,Community_name,Inspected_by,date,summary,Q_summary,S_summary,
            F_summary,H_summary,
            Answer_Q,Answer_H,Answer_S,Answer_F,img_path_Q,des_Q,name_H,des_H,name_S,
            des_S,name_F,des_F):
    logo = "SSE.png"
    global pdf_buffer
    pdf_buffer= BytesIO()
    global pdf_file_temp_dir
    pdf_file_temp_dir=tempfile.mkdtemp()
    # filename=os.getcwd()+'/'+'static/temp_data/output.pdf'
    filename=pdf_file_temp_dir+'/'+'output.pdf'
    notes=[Q_summary,H_summary,S_summary,F_summary]
    answer_list=[Answer_Q,Answer_H,Answer_S,Answer_F]
    image_path_code=[img_path_Q,name_H,name_S,name_F]
    image_description_list=[des_Q,des_H,des_S,des_F]
    doc = SimpleDocTemplate(pdf_buffer, pagesize=landscape(letter))
    doc_local = SimpleDocTemplate(filename, pagesize=landscape(letter))
    story = []
    im = reportlab.platypus.Image(logo, 1*inch, 1*inch)
    story.append(im)
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    story.append(Paragraph("Builder:  "+str(Builder_name), styles["Normal"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Community:  "+str(Community_name), styles["Normal"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Inspected By:  "+str(Inspected_by), styles["Normal"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Date:  "+str(date), styles["Normal"]))
    story.append(Spacer(1, 12))
    section_data = [
        ("General Community Conditions",Question_num),
        ("Model Home", Modern_num),
        ("Sales Team & Sales Center", Sales_team_num),
        ("Finished Inventory", Finished_Inventory_num),]
    section_id=0
    count=0
    flag=False
    for section, questions in section_data:
        heading = Paragraph(f"<b>{section}</b>", styles["Title"])
        story.append(Spacer(1, 0.5 * inch))
        story.append(heading)
        question_table_data = []
        question_table_data_P=[]
        for question in questions:
            question_table_data.append([question, "1", "2", "3", "4", "5"])
        summary_paragraph = Paragraph("<i>Summary Notes:"+str(notes[section_id])+"</i>", style=getSampleStyleSheet()['Normal'])
        question_table_data_P.append([summary_paragraph])

        question_table = Table(question_table_data, colWidths=[5*inch, 1*inch, 1*inch, 1*inch, 1*inch, 1*inch])
        question_table_P = Table(question_table_data_P, colWidths=[10*inch])
        question_table_properties=TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])
        if(answer_list[section_id]==[]):
            pass
        else:
            for index,j in enumerate(answer_list[section_id]):
                question_table_properties.add('BACKGROUND', (int(answer_list[section_id][str(j)]),index), (int(answer_list[section_id][str(j)]),index), colors.red)
        question_table.setStyle(question_table_properties)
        section_id=section_id+1

        question_table_P.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 20),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        data=[]
        story.append(question_table)
        story.append(question_table_P)
        if(len(image_path_code[count])!=0):
            num=0
            flag=True
            for num in range(len(image_path_code[count])):
                question_table_data_image_description=[]
                if(image_description_list[count][num]!=''): 
                    pass
                data.append([Image(image_path_code[count][num],width=250,height=225)])
            data= cuatom_function.return_double_list(data)
            question_table_data_image_description=cuatom_function.return_double_description_list(image_description_list[count])
            print("data",data)
            print("question_table_data_image_description",question_table_data_image_description)
            if(int(len(data)/3)==0):
                if(len(data)!=0):
                    max=1
            else:
                max=int(len(data)/3)
            for index in range(len(question_table_data_image_description)):
                print("enter in the foorloop",question_table_data_image_description[index])
                table_data_image_description = Table([question_table_data_image_description[index]], colWidths=[3.5*inch,3.5*inch,3*inch])
                table_data_image_description.setStyle(TableStyle([
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 20),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black),]))

                print("LOG_1",data[index][:])
                table_image = Table([data[index][:]],colWidths=[3.5*inch,3.5*inch,3*inch])
                table_image.setStyle(TableStyle([
                            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ]))
                story.append(table_image)
                story.append(table_data_image_description)
                table_image=None
                table_data_image_description=None
            if flag is True:
                    data=[]
                    table_image=None
                    table_data_image_description=None
                    flag=False
        count=count+1
    story.append(Spacer(1, 0.4 * inch))
    Notes_heading = Paragraph(f"<b>Summary Notes</b>", styles["Title"])
    story.append(Notes_heading)
    table_data_Notes=[]
    summary_Notes = Paragraph("<i>Summary Notes:"+str(summary)+"</i>", style=getSampleStyleSheet()['Normal'])
    table_data_Notes.append([summary_Notes])
    table_data_Notes_table=Table(table_data_Notes,colWidths=[10*inch])
    table_data_Notes_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 20),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
    story.append(table_data_Notes_table)
    story.append(Spacer(1, 0.4 * inch))

    # Coding part start of  Inventory!
    # path_main=os.getcwd()
    try:
        global temp_dir
        path=temp_dir+'/temp_images'
        path_list=os.listdir(path)
        print(path_list)
        # ind=path_list.index('null.txt')
        # path_list.pop(ind)
        dict_counter=0
        if(len(path_list)!=0):
            heading = Paragraph("<b>Individual Inventory Homes</b>", styles["Title"])
            story.append(heading)
            story.append(Spacer(1, 0.5 * inch))

            for sub_path in path_list:
                heading = Paragraph("<b>"+str(settings.Individual_Inventory_Homes[dict_counter]['address'])+"</b>", styles["Title"])
                story.append(heading)
                # story.append(Spacer(1, 0.5 * inch))
                image_folder_path=path+'/'+sub_path
                print("sub_path",sub_path)
                for image_class in os.listdir(image_folder_path):
                    table_data_Notes=[]
                    table_data_Notes.append([Paragraph("<b>"+str(image_class)+"</b>", style=getSampleStyleSheet()['Title'])])
                    table_data_Notes_table=Table(table_data_Notes,colWidths=[10*inch])
                    table_data_Notes_table.setStyle(TableStyle([
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 20),
                    # ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ]))
                    story.append(table_data_Notes_table)
                    image_data=[]
                    for image_path in os.listdir(image_folder_path+'/'+image_class):
                        print("final",image_folder_path+'/'+image_class+'/'+image_path)
                        image_data.append([Image(image_folder_path+'/'+image_class+'/'+image_path, width=240, height=235)])
                    image_data=cuatom_function.return_double_list(image_data)
                    table_image_data = Table(image_data,colWidths=[3.5*inch,3.5*inch,3*inch])
                    table_image_data.setStyle(TableStyle([
                                # ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                # ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ]))
                    story.append(table_image_data)

                    if((settings.Individual_Inventory_Homes[dict_counter]['front_notes']!='') and (image_class=='front_images')):
                            print("enter in the settings.Individual_Inventory_Homes ",image_class,(image_class=='front_images'))
                            Front_notes_data=[]
                            front_notes_paragraph = Paragraph("<i> FRONT IMAGES NOTES-:"+str(settings.Individual_Inventory_Homes[dict_counter]['front_notes'])+"</i>", style=getSampleStyleSheet()['Normal'])
                            Front_notes_data.append([front_notes_paragraph])
                            table_Front_notes_data = Table(Front_notes_data, colWidths=[10*inch])
                            table_Front_notes_data.setStyle(TableStyle([
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 20),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black),]))
                            story.append(table_Front_notes_data)
                    elif((settings.Individual_Inventory_Homes[dict_counter]['Interior_notes']!='') and(image_class=='Interior_images')):
                            print("enter in the settings.Individual_Inventory_Homes ",image_class,(image_class=='front_images'))
                            Front_notes_data=[]
                            front_notes_paragraph = Paragraph("<i>INTERIOR IMAGES NOTES-:"+str(settings.Individual_Inventory_Homes[dict_counter]['front_notes'])+"</i>", style=getSampleStyleSheet()['Normal'])
                            Front_notes_data.append([front_notes_paragraph])
                            table_Front_notes_data = Table(Front_notes_data, colWidths=[10*inch])
                            table_Front_notes_data.setStyle(TableStyle([
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 20),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black),]))
                            story.append(table_Front_notes_data)
                    elif((settings.Individual_Inventory_Homes[dict_counter]['Back_notes']!='') and(image_class=='Back_images')):
                            print("enter in the settings.Individual_Inventory_Homes ",image_class,(image_class=='front_images'))
                            Front_notes_data=[]
                            front_notes_paragraph = Paragraph("<i>BACK IMAGES NOTES-:"+str(settings.Individual_Inventory_Homes[dict_counter]['front_notes'])+"</i>", style=getSampleStyleSheet()['Normal'])
                            Front_notes_data.append([front_notes_paragraph])
                            table_Front_notes_data = Table(Front_notes_data, colWidths=[10*inch])
                            table_Front_notes_data.setStyle(TableStyle([
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 20),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black),]))
                            story.append(table_Front_notes_data)
                Notes_heading_1 = Paragraph(f"<b>Summary Notes</b>", styles["Title"])
                story.append(Notes_heading_1)
                table_data_Notes_1=[]
                summary_Notes_1 = Paragraph("<i>"+str(settings.Individual_Inventory_Homes[dict_counter]['Summary'])+"</i>", style=getSampleStyleSheet()['Normal'])
                table_data_Notes_1.append([summary_Notes_1])
                table_data_Notes_table_1=Table(table_data_Notes_1,colWidths=[10*inch])
                table_data_Notes_table_1.setStyle(TableStyle([
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 20),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ]))
                story.append(table_data_Notes_table_1)
                dict_counter=dict_counter+1
    except Exception as e:
        print(e)
    End_heading = Paragraph(f"<b>--------END--------</b>", styles["Title"])
    story.append(End_heading)
    doc.build(story)
    doc_local.build(story)
    try:
        helper.upload_pdf_file(Builder_name+'_'+Inspected_by,filename)
        cuatom_function.delete_files_temp(pdf_file_temp_dir)
        cuatom_function.delete_files_temp(temp_dir)
    except:
        pass