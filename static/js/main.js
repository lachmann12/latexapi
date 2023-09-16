function send_data(){
    payload = {
        "q": document.getElementById("question").value,
        "a": document.getElementById("answer1").value,
        "decoys": [
            document.getElementById("answer1").value,
            document.getElementById("answer2").value,
            document.getElementById("answer3").value,
            document.getElementById("answer4").value
        ]
    }
    fetch('http://localhost:5557/latex/api/v1/texify', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(response => console.log(JSON.stringify(response)))

}