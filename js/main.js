function myurl(value){
	inserershorturl.value=(new URL(value)).origin;
	$.ajax({url:"/mydiv",type:"post",data:{"user_id":myuserid.innerHTML,"div1": inserershorturl.value},
	success:function(data){
		if (data.div1.length > 0){
		insererurldiv1.value=data.div1;
		insererurldiv1.parentElement.style.display="block";
		}else{
		insererurldiv1.value="";
		insererurldiv1.parentElement.style.display="block";
		}
	}});
}
function myband(value){
	$.ajax({url:"/myband",type:"post",data:{"div1": value},
	success:function(data){
		var member_list=data.member;
	        inserermembre.innerHTML="<option value=\"\"></option>";
		for(var i = 0;i<member_list.length;i++){
			inserermembre.innerHTML+="<option value=\""+member_list[i].id+"\">"+member_list[i].name+"</option>";
		}
	}});
}

$(function(){
if (window.location.pathname !== "/sign_in" && window.location.pathname !== "/sign_up" && window.location.pathname !== "/aboutme" && myuserid.innerHTML == "") {
alert("pas connecté-e vous allez être redirigé(e)")
window.location="/sign_in";

}
if (document.getElementById("editmypost")){

document.getElementById("members").onchange = function() {

        
        if(editmypost.value !== ""){

            

            editmypost.onfocus = function () {
                var myvalue = (document.getElementById("members").value).toLowerCase();
                var hi = editmypost.value.toLowerCase().indexOf(myvalue);

                if (hi !== -1){
                    console.log(hi,myvalue.length);

                editmypost.setSelectionRange(hi, (hi+myvalue.length));
                editmypost.onfocus = undefined;
document.getElementById("message").innerHTML="";
                }else{
document.getElementById("message").innerHTML="le membre n'a pas été trouvé";

                }
            } 
            editmypost.focus();        
            
        }   

    }
    }
if (document.getElementById("link")){
link.onchange = () => {
if (link.value !== ""){
  var textarea=document.getElementById("editmypost");
  if (textarea.selectionStart !== textarea.selectionEnd){
  let first = textarea.value.slice(0, textarea.selectionStart);
  let rest = textarea.value.slice(textarea.selectionEnd, textarea.value.length);

  textarea.value = first + link.value + rest;

  // Bonus: place cursor behind replacement
  textarea.selectionEnd = (first + link.innerText).length;
};
link.value="";
members.value="";
};
};
};

});
$(document).ready(function () {
	var myselect=$(".someselect");
	
      myselect.selectize({
          sortField: 'text'
      })
	if(myselect.data("text")){
		myselect[0].selectize.addOption({text: myselect.data("text"), value: myselect.data("selectize1")})
		myselect[0].selectize.setValue(myselect.data("selectize1"));
	}
  });

