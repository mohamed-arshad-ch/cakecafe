//get ip address 
// var userip;
// $.getJSON("https://api.ipify.org?format=json",
//     function (data) {


//         userip = data.ip;

//         const ipurl = `http://api.ipstack.com/${userip}?access_key=fa17b668b668976cbf394a899dd97b29`;

//         axios.get(ipurl).then(res => {

//             $("#currentip").val(res.data.location.calling_code);
//         })
//     })

//add To Cart

const cartButton = document.querySelectorAll("#addtocart");

cartButton.forEach((btns) => {
    $(btns).click(() => {
        axios.get(`addtocart/${btns.dataset.productid}`).then(res => {
            console.log(res.data);
            if (res.data.message == "Please Login") {
                $.notify("Please Login Then Add To Cart", "warn");
            } else {
                const cartcount = document.querySelectorAll("#cart-count")
                cartcount.forEach((newb) => {
                    $(newb).text(res.data.cartcount)
                })
            }

        })
    })
})


const editbtns = document.querySelectorAll("#editbtns");

editbtns.forEach((mbtns)=>{
    $(mbtns).click(()=>{
        axios.get(`fetchproduct/${mbtns.dataset.productid}`).then(res =>{
            var newData = JSON.parse(res.data)
            console.log(res.data);
            $("#nameedit").val(newData[0].fields.name)
            $("#priceedit").val(newData[0].fields.price)
            $("#stockedit").val(newData[0].fields.stock)
            $("#weightedit").val(newData[0].fields.weight)
            $("#unitedit").val(newData[0].fields.unit)
            $("#editform").attr("action",`editproduct/${newData[0].pk}`)
            $("#editproducts").modal("show");
        });
        
    });
});


const deletebtns = document.querySelectorAll("#deletebtns");

deletebtns.forEach((dbtns)=>{
    $(dbtns).click(()=>{
        
            $("#deleteform").attr("action",`deleteproduct/${dbtns.dataset.productid}`)
            $("#deleteproducts").modal("show");
        
        
    });
});


const editcategorybtns = document.querySelectorAll("#editcategorybtns");

editcategorybtns.forEach((mbtns)=>{
    $(mbtns).click(()=>{
        axios.get(`editcategory/${mbtns.dataset.categoryid}`).then(res =>{
            var newData = JSON.parse(res.data)
            console.log(res.data);
            $("#editcategory").val(newData[0].fields.title)
            
            $("#editcategory-form").attr("action",`editcategory/${mbtns.dataset.categoryid}`)
            $("#editcategorymodal").modal("show");
        });
        
    });
});


const deletecategorybtns = document.querySelectorAll("#deletecategorybtns");

deletecategorybtns.forEach((dbtns)=>{
    $(dbtns).click(()=>{
        
            $("#deletecategoryform").attr("action",`deletecategory/${dbtns.dataset.categoryid}`)
            $("#deletecategory").modal("show");
        
        
    });
});


const fetchorderbtns = document.querySelectorAll("#fetchorderbtns");

fetchorderbtns.forEach((dbtns)=>{
    $(dbtns).click(()=>{
        
            axios.get(`pendingcartdetails/${dbtns.dataset.orderid}`).then(res =>{
                console.log(res.data);
                for (let index = 0; index < res.data.itemname.length; index++) {
                    var html = `<tr>
                    <th scope="row">
                        ${res.data.itemname[index]}
                    </th>
                    <td class="budget">
                    ${res.data.qty[index]}
                    </td>
                    <td class="budget">
                    ${res.data.price[index]}
                    </td>
                    <td class="budget">
                    ${res.data.total[index]}
                    </td>
                   
                </tr>`;

                $("#productiorderitems").append(html)
                    
                }
                $("#fetchordersdetails").modal("show");
            })
            
        
        
    });
});