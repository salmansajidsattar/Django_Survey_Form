console.log("LOG:Enter in the JS File");
function on_submit(){
    let myFormData = new FormData();
    myFormData.append('pictureFile', document.getElementById('imageFile_Q1').files[0]);
    let Builder=document.querySelector('#Builder').value
    let Community=document.querySelector('#Community').value
    let Q_Notes=document.querySelector('#Q_Notes').value
    let S_Notes=document.querySelector('#S_Notes').value
    let H_Notes=document.querySelector('#H_Notes').value
    let F_Notes=document.querySelector('#F_Notes').value
    let Summary_Notes= document.querySelector("#paragraphInputfinal").value
    let dict_Question=Fetch_data('#Question_Class', '#Question_label')   
    let dict_Home=Fetch_data('#Home_Class', '#Home_label')
    let dict_sales=Fetch_data('#sales_class', '#Sales_label')
    let dict_inventory=Fetch_data('#inventory_class', '#Inventory_label')
    myFormData.append('Builder',Builder)
    myFormData.append('Community',Community)
    myFormData.append('Q_Notes',Q_Notes)
    myFormData.append('S_Notes',S_Notes)
    myFormData.append('H_Notes',H_Notes)
    myFormData.append('F_Notes',F_Notes)
    myFormData.append('Summary_Notes',Summary_Notes)
    myFormData.append('dict_Question',dict_Question)
    myFormData.append('dict_Home',dict_Home)
    myFormData.append('dict_sales',dict_sales)
    myFormData.append('dict_inventory',dict_inventory)
    // let image_H=get_Image_links('#imageFile_H')
    // console.log("LOG_1",image_H)
    // let image_S=get_Image_links('#imageFile_S')
    // console.log("LOG_1",image_S)
    // let image_F=get_Image_links('#imageFile_F')
    // console.log("LOG_1",image_F)
    final_dict={'Builder':Builder,
    'Community':Community,
    'Q_Notes':Q_Notes,
    'S_Notes':S_Notes,
    'H_Notes':H_Notes,
    'F_Notes':F_Notes,
    'Summary_Notes':Summary_Notes,
        'Question_Class':dict_Question,
        'image_Q':document.querySelector('#imageFile_Q'),
        'image_H':image_H,
        'image_S':image_S,
        'image_F':image_F,
                 'Home_Class':dict_Home,
                'sales_class':dict_sales,
                'inventory_class':dict_inventory}
    console.log("Hello Ji")
    return myFormData;
    
}

function Fetch_data(num_class,num_label)
{
    let count=0
    let dict={}
    let image_description
    let temp1=null;
    let second_list=null;
    temp1=document.querySelectorAll(num_class);
    if(temp1.length==0)
    {
        return 0

    }
    let keys=document.querySelectorAll(num_label)
for (let i = 0; i < temp1.length; i++)
{
    count=0
    second_list=null;
    second_list=temp1[i].querySelectorAll('.form-check-input');
    for ( let j in second_list) {
        if ((count==6) &&(second_list[j].querySelectorAll('#imageDescription').value.length != 0)){
            image_description=second_list[j].querySelectorAll('#imageDescription').value}

        else if ((count==5) &&(second_list[j].querySelectorAll('#imageFile').files.length!=0)){
            image=second_list[j].querySelectorAll('#imageFile').files[0]}
        
        else if(second_list[j].checked){
            dict[keys[i].innerHTML]=second_list[j].value
        }

    }
 
}
return dict
}

function get_Image_links(name){
    let list1=document.querySelectorAll(name)
    let count=0
    let dict={}
for(let i = 0; i < list1.length; i++)
{
    if(list1[i].files.length==0){
        dict[count]="Null"
        count=count+1    
    }
    else
    {
        console.log("enter in else")
    dict[count]=list1[i].files[0]
    count=count+1
}
}
console.log("DICT",dict)
return dict
}
// export{Fetch_data}