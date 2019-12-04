$(".order_button").on("click",(e)=>{
    e.preventDefault();
    a={
    fname :$("#fname").val(),
    lname :$("#lname").val(),
    country :$("#country").val(),
    address :$("#address").val(),
    zipcode :$("#zipcode").val(),
    city :$("#city").val(),
    phone :$("#phone").val(),
    email:$("#email").val(),
    fname :$("#fname").val(),
    }
    error=""
    var reg = /^\d+$/;
    if(!reg.test(a.phone)){error+="Please enter a valid phone number\n";}
    if(!reg.test(a.zipcode)){error+="Please enter a valid zip code\n";}
    if(!a.fname){error+="Please enter a valid First name\n";}
    if(!a.lname){error+="Please enter a valid Last name\n";}
    if(!a.country){error+="Please enter a valid country\n";}
    if(!a.city){error+="Please select a valid city\n";}
    if(a.email.indexOf("@")==-1){error+="Please select a valid email\n";}
    if(!a.address){error+="Please select a valid address\n";}

    if(error){
        alert(error)
    }else{
        alert("order placed")
        setTimeout("window.location='/'",3000);
    }







})

