console.log("enter in the datafile.js")
import {Individual_Inventory_Homes} from './data.js'
$(document).ready(function(){
    $('#image-upload-form').submit(function() {
        console.log("Enter in the middle")
        let address=document.getElementById('address')
        let front_images=return_image_name(document.getElementById('imageFile1').files)
        let front_notes=document.getElementById('paragraphInput')
        let Interior_images=return_image_name(document.getElementById('imageFile2').files)
        let Interior_notes=document.getElementById('paragraphInput_2')
        let Back_images=return_image_name(document.getElementById('imageFile3').files)
        let Back_notes=document.getElementById('paragraphInput_3')
        let Summary=document.getElementById('summary')
        temp={'address':address,
        "front_images":front_images,"front_notes":  front_notes,
        "Interior_images" :Interior_images,"Interior_notes":Interior_notes,
        "Back_images":Back_images,"Back_notes":Back_notes,
    "Summary":Summary}
        console.log(temp)
        Individual_Inventory_Homes.push({'address':address,
                                        "front_images":front_images,"front_notes": front_notes,
                                        "Interior_images" :Interior_images,"Interior_notes":Interior_notes,
                                        "Back_images":Back_images,"Back_notes":Back_notes,
                                    "Summary":Summary})
    });
});

function return_image_name(files){temp=[];
for (let i = 0; i < files.length; i++);{
temp.push(files[i].name);}return temp;}