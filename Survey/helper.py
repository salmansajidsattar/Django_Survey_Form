import os
from supabase import create_client, Client
from dotenv import load_dotenv
from datetime import date
today = date.today()
d1 = today.strftime("%d/%m/%Y")

def upload_pdf_file(storage_path):
    load_dotenv()
    SUPABASE_URL=str(os.getenv('SUPABASE_URL'))
    SUPABASE_API_KEY=str(os.getenv('SUPABASE_API_KEY'))
    bucket_name=str(os.getenv('bucket_name'))
    local_file_path = '../static/temp_data/output.pdf'
    # Initialize Supabase client
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_API_KEY)
    print("enter")
    # storage_path = 'file_name2.pdf' 
    storage_path=storage_path+"_"+str(d1)
    print("storage",storage_path)
    with open(local_file_path, 'rb') as f:
        try:
            res = supabase.storage.from_(bucket_name).upload(storage_path, local_file_path)
            print(res)
            pass
            # Check if the upload was successful
            if res.statusCode == 200:
                print("File uploaded successfully!")
        except Exception as e:
                    print("File uploaded successfully!")