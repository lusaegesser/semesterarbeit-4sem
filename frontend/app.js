const API_URL = "/tracks/";
const BASE_URL = "/";

async function createTrack() {

    const trackId = document.getElementById("trackId").value;

    const track = {
        title: document.getElementById("title").value,
        artist: document.getElementById("artist").value,
        genre: document.getElementById("genre").value,
        bpm: parseInt(document.getElementById("bpm").value),
        key: document.getElementById("key").value,
        status: document.getElementById("status").value
    };

    if (
        !track.title ||
        !track.artist ||
        !track.genre ||
        !track.bpm
    ) {
        alert("Bitte Pflichtfelder ausfüllen");
        return;
    }

    let response;

    if (trackId) {

        response = await fetch(
            `${API_URL}${trackId}`,
            {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(track)
            }
        );

    } else {

        response = await fetch(
            API_URL,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(track)
            }
        );
    }

    if (response.ok) {

        clearForm();
        loadTracks();

        alert("Track erfolgreich gespeichert");
    }
}

async function uploadAudio(trackId) {

    const fileInput = document.getElementById(`audio-${trackId}`);

    if (!fileInput.files.length) {
        alert("Bitte eine Audiodatei auswählen");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const response = await fetch(
        `${API_URL}${trackId}/upload`,
        {
            method: "POST",
            body: formData
        }
    );

    if (response.ok) {

        alert("Audiodatei erfolgreich hochgeladen");

        loadTracks();

    } else {

        const error = await response.json();

        alert(error.detail);
    }
}

async function deleteTrack(trackId) {

    const confirmed = confirm(
        "Möchtest du diesen Track wirklich löschen?"
    );

    if (!confirmed) {
        return;
    }

    const response = await fetch(
        `${API_URL}${trackId}`,
        {
            method: "DELETE"
        }
    );

    if (response.ok) {

        loadTracks();

        alert("Track erfolgreich gelöscht");
    }
}

function editTrack(track) {

    document.getElementById("trackId").value = track.id;

    document.getElementById("title").value = track.title;
    document.getElementById("artist").value = track.artist;
    document.getElementById("genre").value = track.genre;
    document.getElementById("bpm").value = track.bpm;
    document.getElementById("key").value = track.key;
    document.getElementById("status").value = track.status;

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}

function clearForm() {

    document.getElementById("trackId").value = "";

    document.getElementById("title").value = "";
    document.getElementById("artist").value = "";
    document.getElementById("genre").value = "";
    document.getElementById("bpm").value = "";
    document.getElementById("key").value = "";
    document.getElementById("status").value = "";
}

async function loadTracks() {

    const title = document.getElementById("titleInput").value;
    const artist = document.getElementById("artistInput").value;
    const genre = document.getElementById("genreInput").value;
    const key = document.getElementById("keyInput").value;
    const minBpm = document.getElementById("minBpmInput").value;
    const maxBpm = document.getElementById("maxBpmInput").value;

    const params = new URLSearchParams();

    if (title) params.append("title", title);
    if (artist) params.append("artist", artist);
    if (genre) params.append("genre", genre);
    if (key) params.append("key", key);
    if (minBpm) params.append("min_bpm", minBpm);
    if (maxBpm) params.append("max_bpm", maxBpm);

    let url = API_URL;

    if (params.toString()) {
        url += "?" + params.toString();
    }

    const response = await fetch(url);

    const tracks = await response.json();

    const trackList = document.getElementById("trackList");

    trackList.innerHTML = "";

    if (tracks.length === 0) {

        trackList.innerHTML =
            "<p>Keine Tracks gefunden.</p>";

        return;
    }

    tracks.forEach(track => {
        const card = document.createElement("div");
        card.className = "track-card";
        const heading = document.createElement("h2");
        heading.textContent = track.title;
        card.append(heading);
        for (const [label, value] of [["Artist", track.artist], ["Genre", track.genre], ["BPM", track.bpm], ["Tonart", track.key], ["Status", track.status]]) {
            const line = document.createElement("p");
            line.textContent = `${label}: ${value}`;
            card.append(line);
        }
        if (track.audio_file) {
            const player = document.createElement("audio");
            player.controls = true;
            player.preload = "metadata";
            player.src = BASE_URL + track.audio_file;
            player.style.width = "100%";
            card.append(player);
        }
        const input = document.createElement("input");
        input.type = "file";
        input.id = `audio-${track.id}`;
        input.accept = ".mp3,.wav";
        card.append(input);
        for (const [label, action] of [["Audio hochladen", () => uploadAudio(track.id)], ["Bearbeiten", () => editTrack(track)], ["Löschen", () => deleteTrack(track.id)]]) {
            const button = document.createElement("button");
            button.textContent = label;
            button.addEventListener("click", action);
            card.append(button);
        }
        trackList.append(card);
    });
}

loadTracks();
