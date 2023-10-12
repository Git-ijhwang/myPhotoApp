document.getElementById('clear-btn').addEventListener('click', function() {
    fetch('/clear/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}',
        },
    }).then(function(response) {
        if (response.ok) {
            alert('Successfully cleared static files');
        } else {
            alert('Failed to clear static files');
        }
    });
});
