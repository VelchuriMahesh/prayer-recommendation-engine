function getRecommendation() {
  const feeling = document.getElementById("feelingInput").value;

  fetch('http://127.0.0.1:5000/recommend', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ feeling })
  })
    .then(response => response.json())
    .then(data => {
      document.getElementById("result").innerText = data.verse || data.error;
    })
    .catch(error => {
      console.error('Error:', error);
      document.getElementById("result").innerText = "Something went wrong. Try again.";
    });
}
