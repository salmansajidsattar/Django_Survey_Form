
console.log("enter in the data post call")
function return_image_name(files){
    let temp=[];
for (let i = 0; i < files.length; i++)
{
temp.push(files[i].name);}return temp;
}
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
    $('#submit_click').click(function(e) {
    flag=Individual_validation()
    console.log("FLAG INDID__>",flag)
    if (flag=="error"){
      console.log("flag-->1")
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'FIELD IS MISSING!',
      })
    }
  else{  
    e.preventDefault(); // prevent the page from reload

    let myFormData = new FormData();
    let address=document.getElementById('address').value;
    let front_images=document.getElementById('imageFile1').files
    for(let i=0;i<front_images.length;i++){
        myFormData.append('front_images',front_images[i])
    }
    let front_notes=document.getElementById('paragraphInput').value;
    let Interior_images=document.getElementById('imageFile2').files
    for(let i=0;i<Interior_images.length;i++){
        myFormData.append('Interior_images',Interior_images[i])
    }
    let Interior_notes=document.getElementById('paragraphInput_2').value;
    let Back_images=document.getElementById('imageFile3').files
    for(let i=0;i<Back_images.length;i++){
        myFormData.append('Back_images',Back_images[i])}
    let Back_notes=document.getElementById('paragraphInput_3').value;
    let Summary=document.getElementById('summary').value;
    // let form=document.getElementById("image-upload-form")[0];  
    myFormData.append('address',address)
    myFormData.append('address',address)
    myFormData.append('front_images',front_images)
    myFormData.append('front_notes',front_notes)
    myFormData.append('Interior_images',Interior_images)
    myFormData.append('Interior_notes',Interior_notes)
    myFormData.append('Back_images',Back_images)
    myFormData.append('Back_notes',Back_notes)
    myFormData.append('Summary',Summary)
    let url = "Temp_data"
    console.log("Form_Data",myFormData)
      $.ajax({
        url: url,
        type: 'POST',
        data: myFormData,
        processData: false,
        contentType: false,
      }).done(function(response) {
        document.getElementById('address').value=''
        document.getElementById('imageFile1').value=''
        document.getElementById('paragraphInput').value='';
        document.getElementById('imageFile2').value='';
        document.getElementById('paragraphInput_2').value='';
        document.getElementById('imageFile3').value='';
        document.getElementById('paragraphInput_3').value='';
        document.getElementById('summary').value='';
        console.log("log",response) // let's just print the data in the console for now
        })
      $(this).trigger('reset') // reset the form
  }
    })
  })