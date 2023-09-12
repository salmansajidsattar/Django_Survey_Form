import os
from supabase import create_client, Client
from dotenv import load_dotenv
import datetime
date_now = datetime.datetime.now()
def upload_pdf_file(storage_path,input_path):
    load_dotenv()
    SUPABASE_URL=str(os.getenv('SUPABASE_URL'))
    SUPABASE_API_KEY=str(os.getenv('SUPABASE_API_KEY'))
    bucket_name=str(os.getenv('bucket_name'))
    # local_file_path = '../static/temp_data/output.pdf'
    local_file_path=input_path
    # Initialize Supabase client
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_API_KEY)
    print("enter")
    # storage_path = 'file_name2.pdf' 
    global date_now
    storage_path=storage_path+"_"+str(date_now)+'.pdf'
    print("storage",storage_path)
    try:
            res = supabase.storage.from_(bucket_name).upload(storage_path, local_file_path)
            # res = supabase.storage.from_(bucket_name).get_public_url(storage_path, local_file_path)
            print(res)
            # Check if the upload was successful
            if res.statusCode == 200:
                print("File uploaded successfully!")
            return res
    except Exception as e:
                    print("File uploaded successfully!")