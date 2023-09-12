import shutil
import os
import io

def get_image_link(table,count,image_description):
    arr=[]
    # print('table',table)
    image_count=[]
    # if(arr==[]):
        # return None,None
    for i in range(1,count):
        arr.append(str(table)+str(i))
        image_count.append(str(image_description)+str(i))
    return arr,image_count

def delete_files():
    path='./temp_images'
    path_list=os.listdir(path)
    # print(path_list)
    for files in path_list:
        shutil.rmtree(path+'/'+files, ignore_errors = False)
    return 0

            
def return_keys_value(dict):
    answer=list(dict.values())
    question=list(dict.keys())
    return answer,question

def return_double_list(list):
    lenght=len(list)
    temp=[]
    count=0
    for _ in range(lenght):
        if((lenght-count)==0):
            break
        elif((lenght-count)<3):
            if((lenght-count)==2):
                temp.append([list[count],list[count+1],""])
                count=count+2
                break
            if((lenght-count)==1):
                temp.append([list[count],"",""])
                count=count+1
                break
        else:
            temp.append([list[count],list[count+1],list[count+2]])
            count=count+3
    # print("TESTING LIST TEMP",temp)
    return temp

def return_double_description_list(list):
    lenght=len(list)
    temp=[]
    count=0
    for _ in range(lenght):
        if((lenght-count)==0):
            break
        elif((lenght-count)<3):
            if((lenght-count)==2):
                temp.append([list[count],list[count+1],""])
                # print("[list[count],list[count+1],No description]",[list[count],list[count+1],""])
                count=count+2
                break
            if((lenght-count)==1):
                # print("[list[count]",[list[count],"",""])
                temp.append([list[count],"",""])
                count=count+1
                break
        else:
            temp.append([list[count],list[count+1],list[count+2]])
            count=count+3
    print("TESTING  Description TEMP",temp)
    return temp

def read_pdf_into_memory(pdf_path='./temp_data/output.pdf'):
    with open(pdf_path, "rb") as pdf_file:
        pdf_buffer = io.BytesIO(pdf_file.read())
    return pdf_buffer

def write_pdf_from_memory(pdf_buffer, output_path):
    with open(output_path, "wb") as output_file:
        output_file.write(pdf_buffer.read())