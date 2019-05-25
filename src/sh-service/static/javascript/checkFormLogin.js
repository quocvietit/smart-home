function checkUserName(){

    if(document.getElementById('username').value == "")
        {
            document.getElementById('usernamereport').innerHTML = "Please fill in this field !!!";
            return false;
        }
        else
        {

				document.getElementById('usernamereport').innerHTML = "";
				return true;

        }
}

function checkPassword() {

    if (document.getElementById("password").value == "") {
        document.getElementById("passwordreport").innerHTML = "Please fill in this field !!!";
        return false;
    }
      else {
               document.getElementById('passwordreport').innerHTML = "";
              return true;

      }
}


    function checkLogin(){
        if(checkUserName() && checkPassword())
            document.getElementById('login').disabled = false;
        else
            document.getElementById('login').disabled = true;
    }