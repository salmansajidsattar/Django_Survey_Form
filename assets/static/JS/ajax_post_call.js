// import {Fetch_data} from './pdf_file'
console.log("enter in the ajax post call")
$(document).ready(function() {
function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');
    /* ... */
    /* send a POST request to create a todo */
    $('#sendCheckboxData').click(function(e) {
    flag=check_validation()
    if (flag=="error"){
            swal("FIELD IS MISSING!");}
    else{
    e.preventDefault(); // prevent the page from reload
    let myFormData = new FormData();
    let Builder=document.querySelector('#Builder').value;
    let Community=document.querySelector('#Community').value;
    let Q_Notes=document.querySelector('#Q_Notes').value;
    let S_Notes=document.querySelector('#S_Notes').value;
    let H_Notes=document.querySelector('#H_Notes').value;
    let F_Notes=document.querySelector('#F_Notes').value;
    let Summary_Notes= document.querySelector("#paragraphInputfinal").value;
    let dict_Question=Fetch_data('#Question_Class', '#Question_label');
    let dict_Home=Fetch_data('#Home_Class', '#Home_label');
    let dict_sales=Fetch_data('#sales_class', '#Sales_label');
    let dict_inventory=Fetch_data('#inventory_class', '#Inventory_label');
    let image_list_F=get_images('#imageFile_F','#imageDescription_F');
    let image_list_Q=get_images('#imageFile_Q','#imageDescription_Q');
    let image_list_S=get_images('#imageFile_S','#imageDesimageDescription_Hcription_S');
    let image_list_H=get_images('#imageFile_H','#imageDescription_H');
    let inspected_by=document.getElementById('textInput').value;
    let enter_date=document.getElementById('dateInput').value;
    let imageDescription_Q=document.querySelectorAll('#imageDescription_Q')
    let imageDescription_H=document.querySelectorAll('#imageDescription_H')
    let imageDescription_S=document.querySelectorAll('#imageDescription_S')
    let imageDescription_F=document.querySelectorAll('#imageDescription_F')
    myFormData.append('Builder',Builder)
    myFormData.append('Community',Community)
    myFormData.append('inspected_by',inspected_by)
    myFormData.append('enter_date',enter_date);
    myFormData.append('Q_Notes',Q_Notes)
    myFormData.append('S_Notes',S_Notes)
    myFormData.append('H_Notes',H_Notes)
    myFormData.append('F_Notes',F_Notes)
    myFormData.append('Summary_Notes',Summary_Notes)
    myFormData.append('Question',JSON.stringify(dict_Question))
    myFormData.append('Home',JSON.stringify(dict_Home))
    myFormData.append('sales',JSON.stringify(dict_sales))
    myFormData.append('inventory',JSON.stringify(dict_inventory))
    myFormData.append('image_list_F',JSON.stringify(image_list_F))
    myFormData.append('image_list_H',JSON.stringify(image_list_H))
    myFormData.append('image_list_Q',JSON.stringify(image_list_Q))
    myFormData.append('image_list_S',JSON.stringify(image_list_S))
    myFormData.append('imageDescription_Q',JSON.stringify(imageDescription_Q))
    myFormData.append('imageDescription_H',JSON.stringify(imageDescription_H))
    myFormData.append('imageDescription_S',JSON.stringify(imageDescription_S))
    myFormData.append('imageDescription_F',JSON.stringify(imageDescription_F))
    let url = "Form_Data"
    console.log("Form_Data",myFormData)
      $.ajax({
        url: url,
        type: 'POST',
        data: myFormData,
        processData: false,
        contentType: false,
        // contentType: 'multipart/form-data',
      }).done(function(response) {
        document.getElementById("uploadForm").reset();
          console.log("log",response) // let's just print the data in the console for now
          Swal.fire({
            position: 'top-end',
            icon: 'success',
            title: 'Your work has been saved',
            showConfirmButton: false,
            timer: 1500
          })
        })
      $(this).trigger('reset') // reset the form
      } 
    })
    
  })