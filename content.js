link=window.location.href;
console.log(link)
chrome.runtime.onMessage.addListener((msg,sender,response)=>{
    console.log(msg.command)
    if(msg.command=='download'){
        
        
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
        
    }
});