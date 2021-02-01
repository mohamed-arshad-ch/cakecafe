//get ip address 
var userip;
$.getJSON("https://api.ipify.org?format=json",
    function (data) {

        
        userip = data.ip;

        const ipurl = `http://api.ipstack.com/${userip}?access_key=fa17b668b668976cbf394a899dd97b29`;

        axios.get(ipurl).then(res => {
           
            $("#currentip").val(res.data.location.calling_code);
        })
    })

//get location using ip 

