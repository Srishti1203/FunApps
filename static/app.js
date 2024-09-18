function getZenQuote() {
    fetch('/zen_timer')
        .then(response => response.json())
        .then(data => {
            document.getElementById('zen-quote').innerText = data;
        });
}

function getCompliment() {
    fetch('/compliment_mirror')
        .then(response => response.json())
        .then(data => {
            document.getElementById('compliment').innerText = data;
        });
}

function getMoodPalette() {
    const mood = document.getElementById('mood-input').value.toLowerCase();
    fetch('/mood_palette', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mood: mood })
    })
    .then(response => response.json())
    .then(palette => {
        document.getElementById('palette').innerText = palette.join(', ');
    });
}

function getEmojiTranslation() {
    const sentence = document.getElementById('emoji-input').value;
    fetch('/emoji_translator', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ sentence: sentence })
    })
    .then(response => response.json())
    .then(translation => {
        document.getElementById('emoji-translation').innerText = translation;
    });
}

function spinDecisionWheel() {
    const options = document.getElementById('decision-input').value.split(',');
    fetch('/decision_wheel', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ options: options })
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('decision-result').innerText = result;
    });
}

function generateGibberish() {
    fetch('/gibberish_generator')
        .then(response => response.json())
        .then(data => {
            document.getElementById('gibberish').innerText = data;
        });
}
