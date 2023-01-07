var el = document.getElementById('video_form');

if (el){
    // Add an event listener to the form
    el.addEventListener('submit', function(event) {
    // Prevent the form from being submitted
    event.preventDefault();

    // Get the video URL from the form
    var videoUrl = document.getElementById('video_url').value;
    console.log(videoUrl);

    // Send an HTTP request to the server-side script
    fetch('./main.py', {
        method: 'GET',
        body: JSON.stringify({
        video_url: videoUrl
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
        console.error(error);
    });
    });
}
else{
    console.log('There is no form present');
}