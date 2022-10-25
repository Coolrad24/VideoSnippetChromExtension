document.querySelector('#download').addEventListener('click',function(){
    chrome.tabs.query({currentWindow:true,active: true},function(tabs){
        console.log('hi')
        chrome.tabs.sendMessage(tabs[0].id,{command:'download'})
        var st=document.querySelector('#start').value
        var stp=document.querySelector('#stop').value
        link=st+"/"+stp
        fetch("http://127.0.0.1:5000/videos", 
        {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'Accept': 'application/json'
            },
        // Strigify the payload into JSON:
        body:JSON.stringify(link)}).then(res=>{
                if(res.ok){
                    return res.json()
                }else{
                    alert("something is wrong")
                }
            }).then(jsonResponse=>{
                
                
                console.log(jsonResponse)
        } 
        ).catch((err) => console.error(err));
    })
})