console.log("enetr check_validation")
function check_validation(){
    console.log("calling the check validation function")
    let Builder=document.querySelector('#Builder')
    let Community=document.querySelector('#Community')
    let Q_Notes=document.querySelector('#Q_Notes')
    let S_Notes=document.querySelector('#S_Notes')
    let H_Notes=document.querySelector('#H_Notes')
    let F_Notes=document.querySelector('#F_Notes')
    let Summary_Notes= document.querySelector("#paragraphInputfinal")
    let dict_Question=Fetch_data('#Question_Class', '#Question_label')
    let dict_Home=Fetch_data('#Home_Class', '#Home_label')
    let dict_sales=Fetch_data('#sales_class', '#Sales_label')
    let dict_inventory=Fetch_data('#inventory_class', '#Inventory_label')
    if((Builder.checkValidity()==false)||(Community.checkValidity()==false)||(Q_Notes.checkValidity()==false)||(S_Notes.checkValidity()==false)||(H_Notes.checkValidity()==false)||(F_Notes.checkValidity()==false)||(Summary_Notes.checkValidity==false)){
        console.log("error-->1")
        return "error"
    }
    else if (Object.keys(dict_Question).length!=7==true){
        console.log("error-->2")
        return "error"
    }
    else if (Object.keys(dict_Home).length!=15==true){
        console.log("error-->3")
        return "error"
    }
    else if (Object.keys(dict_sales).length!=7==true){
        console.log("error-->4")
        return "error"
    }
    else if (Object.keys(dict_inventory).length!=7==true){
        console.log("error-->5")
        return "error"
    }
    else{python
        console.log("OK-->1")
        return "ok"
    }   
    // return "ok"
}

function Individual_validation(){
    let address=document.getElementById('address').checkValidity()
    let image1=document.getElementById('imageFile1').checkValidity()
    let para1=document.getElementById('paragraphInput').checkValidity()
    let image2=document.getElementById('imageFile2').checkValidity()
    let para2=document.getElementById('paragraphInput_2').checkValidity()
    let image3=document.getElementById('imageFile3').checkValidity()
    let para3=document.getElementById('paragraphInput_3').checkValidity()
    let summary=document.getElementById('summary').checkValidity()
    if(address&&image1&&para1&&image2&&para2&&image3&&para3&&summary){
        return "ok"
    }
    else{
        return "error"
    }
}