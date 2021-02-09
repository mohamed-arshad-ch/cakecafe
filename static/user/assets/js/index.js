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

//add To Cart

const cartButton = document.querySelectorAll("#addtocart");

cartButton.forEach((btns)=>{
    $(btns).click(()=>{
        axios.get(`addtocart/${btns.dataset.productid}`).then(res=>{
            console.log(res.data);

            const cartcount = document.querySelectorAll("#cart-count")
            cartcount.forEach((newb)=>{
                $(newb).text(res.data.cartcount)
            })
        })
    })
})


