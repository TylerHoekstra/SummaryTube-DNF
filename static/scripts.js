var el = document.getElementById('video_form');

if (el){
    // Add an event listener to the form
    el.addEventListener('submit', function(event) {
    // Prevent the form from being submitted
    event.preventDefault();

    // Get the video URL from the form
    var videoUrl = document.getElementById('video_url').value;
    console.log(videoUrl);
    
    // get url ID token
    temp = videoUrl.split("=")
    console.log(temp)
    vidId = temp[1]
    console.log(vidId)
    var tn = document.getElementById("thumbnail").src = "https://www.youtube.com/embed/" + vidId

    // Send an HTTP request to the server-side script
    fetch('http://localhost:8000/api/process_video', {
        method: 'POST',
        body: JSON.stringify({
        inputUrl: videoUrl
        }),
        headers: {
        'Content-Type': 'application/json'
        }
    }).then(function(response) {
        return response.text();
    }).then(function(summary) {
        // Display the summary in the summary div
        document.getElementById('summary').innerHTML = summary;
    }).catch(function(error) {
        console.error('HEYHEYHEYSTOP' + error);
    });
    });
}
else{
    console.log('We were not able to generate a summary for you because this video does not have a transcript');
}
