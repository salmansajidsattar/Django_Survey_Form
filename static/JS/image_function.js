console.log("enter in the image_function.js")
function get_images(image,descrip){
    console.log("Enter in the get images")
    console.log(image)
    console.log(descrip)
    let image_list = []
    let image_description=[]
    let count=0
    list1=document.querySelectorAll(image)
    description=document.querySelectorAll(descrip)
    console.log(list1)
    console.log(description)
    for (let i = 0; i < list1.length; i++)
    {
        console.log(list1[i])
        console.log(list1[i].files[0])
        console.log(list1[i].files.length)
        let temp=list1[i].files.lenght
        if (list1[i]) {
            console.log("enter in the if condition")
            image_list.push(list1[i].files[0])
            if(description[i]){
            image_description.push(description[i].value)}
            else{
                image_description.push("No description added with the image")
            }
     }
     }
     let dict={'image_list':image_list} 
                // 'image_description':image_description}
    console.log(image_list)
    console.log(image_description)
    return dict
}

function return_images_ids(table,count){
    let arr=[]
    for (let i=1;i<count;i++){
        arr.push(table+i)

    }
    return arr

}