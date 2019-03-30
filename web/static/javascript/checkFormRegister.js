function checkUserName(){
    var re = /^[A-Z][a-zA-Z0-9]{5,}$/;

    if(document.getElementById('username').value == "")
        {
            document.getElementById('usernamereport').innerHTML = "Please fill in this field !!!";
            return false;
        }
        else
        {
            if (!re.test(document.getElementById("username").value)) {
                document.getElementById("usernamereport").innerHTML = "Name must begin with uppercase, at least 5 characters";
                return false;
            }else{
				document.getElementById('usernamereport').innerHTML = "";
				return true;
			}
        }
}

function checkPassword() {
    var re = /^[a-zA-Z0-9]+$/;

    if (document.getElementById("password").value == "") {
        document.getElementById("passwordreport").innerHTML = "Please fill in this field !!!";
        return false;
    }
      else {
          if (!re.test(document.getElementById("password").value == document.getElementById("password").value)){
          document.getElementById("passwordreport").innerHTML = "Passwords must be at least 6 characters long!!!";
              return false;

          }else{
               document.getElementById('passwordreport').innerHTML = "";
              return true;
          }
      }
}

    function checkConfirm() {
        if (document.getElementById("confirmPassword").value == "") {
            document.getElementById("confirmreport").innerHTML = "Please fill in this field !!!";
            return false;
        }
        else
        {
            if (document.getElementById("password").value == document.getElementById("confirmPassword").value){
                document.getElementById('confirmreport').innerHTML = "";
                return true;
            }else{
                document.getElementById("confirmreport").innerHTML = "Please enter the correct password again!!!";
                return false;
               }

        }
    }

    function checkRegister(){
        if(checkUserName() && checkPassword() && checkConfirm())
            document.getElementById('register').disabled = false;
        else
            document.getElementById('register').disabled = true;
    }