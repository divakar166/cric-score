function getFeaturedData(){
    $.ajax({
        url:'/featuredData',
        success:function(data){
            a = ''
            for(let i = 0;i<=data.length-1;i++){
                a += `${data[i]}`
            }
            $(".fm-item-div").html(a)
        }
    })
}

$(document).ready(function(){
    getFeaturedData()
    setInterval(getFeaturedData,10000);
})