const $ = id => document.getElementById(id);
const shared = new URLSearchParams(location.hash.slice(1));
const shareToken = shared.get("share");
const sharedId = shared.get("set");
let authenticated = false;
function message(text, error = false) { $("message").textContent = text; $("message").classList.toggle("error", error); }
async function api(url, options = {}) {
    const headers = {"X-Archive-Request": "1", ...options.headers};
    if (shareToken) headers["X-Share-Token"] = shareToken;
    const response = await fetch(url, {...options, headers});
    if (!response.ok) {
        const data = await response.json().catch(() => ({}));
        throw new Error(typeof data.detail === "string" ? data.detail : "Eingaben prüfen oder erneut anmelden.");
    }
    return response.json();
}
const json = (method, body) => ({method, headers: {"Content-Type": "application/json"}, body: JSON.stringify(body)});
function run(action) { return async event => { if (event) event.preventDefault(); try { await action(); } catch (error) { message(error.message, true); } }; }
function element(tag, text, className) { const node = document.createElement(tag); if (text !== undefined) node.textContent = text; if (className) node.className = className; return node; }
function button(text, action, secondary = false) { const node = element("button", text, secondary ? "secondary" : ""); node.type = "button"; node.addEventListener("click", run(action)); return node; }
function field(label, input) { const node = element("label", label); node.append(input); return node; }
function input(type, placeholder, maxLength) { const node = document.createElement("input"); node.type = type; node.placeholder = placeholder; if (maxLength) node.maxLength = maxLength; return node; }
function time(seconds) { return `${Math.floor(seconds / 60)}:${String(seconds % 60).padStart(2, "0")}`; }

async function load() {
    const tracks = shareToken && sharedId ? [await api(`/shared/${encodeURIComponent(sharedId)}`)] : await api(`/tracks/?title=${encodeURIComponent($("search").value)}`);
    $("trackList").replaceChildren();
    if (!tracks.length) $("trackList").append(element("p", "Noch keine Sets vorhanden. Erfasse dein erstes Set oben.", "muted"));
    for (const track of tracks) await renderTrack(track);
}
async function renderTrack(track) {
    const card = element("article", undefined, "track-card");
    card.append(element("h2", track.title), element("p", `${track.artist} · ${track.genre}`, "muted"));
    const player = document.createElement("audio");
    if (track.audio_file) {
        player.controls = true; player.preload = "metadata";
        player.src = `/tracks/${track.id}/audio` + (shareToken ? `?share=${encodeURIComponent(shareToken)}` : "");
        card.append(player);
    } else card.append(element("p", "Noch keine Aufnahme hochgeladen.", "muted"));
    if (authenticated && !shareToken) {
        const controls = element("div", undefined, "controls");
        const upload = input("file", ""); upload.accept = ".mp3,.wav";
        controls.append(field("Audiodatei (MP3/WAV, maximal 512 MiB)", upload));
        controls.append(button("Audio hochladen", async () => {
            if (!upload.files.length) throw new Error("Bitte eine Audiodatei auswählen.");
            const data = new FormData(); data.append("file", upload.files[0]);
            message("Aufnahme wird hochgeladen …");
            await api(`/tracks/${track.id}/upload`, {method: "POST", body: data}); await load(); message("Aufnahme gespeichert.");
        }));
        controls.append(button("Bearbeiten", () => {
            $("trackId").value = track.id;
            for (const key of ["title", "artist", "genre", "bpm", "key", "status"]) $(key).value = track[key] || "";
            document.querySelector("details").open = true; $("title").focus();
        }, true));
        const shareOutput = input("text", "Freigabelink"); shareOutput.readOnly = true; shareOutput.hidden = true; shareOutput.setAttribute("aria-label", "Freigabelink zum Kopieren");
        controls.append(button("Neuen Freigabelink erstellen", async () => {
            const result = await api(`/tracks/${track.id}/share`, {method: "POST"});
            shareOutput.hidden = false; shareOutput.value = location.origin + result.path; shareOutput.focus(); shareOutput.select();
            message("Link zum Kopieren bereit. Frühere Links für dieses Set sind jetzt ungültig. localhost-Links funktionieren nur auf diesem Laptop.");
        }, true));
        controls.append(shareOutput, button("Freigabe widerrufen", async () => { await api(`/tracks/${track.id}/share`, {method: "DELETE"}); shareOutput.hidden = true; shareOutput.value = ""; message("Freigabe widerrufen."); }, true));
        controls.append(button("Set löschen", async () => { if (confirm("Set mit Aufnahme und Kommentaren löschen?")) { await api(`/tracks/${track.id}`, {method: "DELETE"}); await load(); } }, true));
        card.append(controls);
    }
    card.append(element("h3", "Feedback mit Zeitmarken"));
    const comments = element("div"); card.append(comments);
    async function loadComments() {
        const values = await api(`/tracks/${track.id}/comments`); comments.replaceChildren();
        if (!values.length) comments.append(element("p", "Noch keine Kommentare.", "muted"));
        for (const value of values) {
            const row = element("div", undefined, "comment");
            row.append(button(time(value.seconds), () => { if (track.audio_file) player.currentTime = value.seconds; }, true), element("strong", value.author), element("p", value.body));
            if (authenticated && !shareToken) row.append(button("Kommentar löschen", async () => { await api(`/comments/${value.id}`, {method: "DELETE"}); await loadComments(); }, true));
            comments.append(row);
        }
    }
    const form = document.createElement("form");
    const name = input("text", "Dein Anzeigename", 80); name.required = true;
    const seconds = input("number", "Sekunden"); seconds.min = 0; seconds.max = 604800; seconds.step = 1; seconds.value = 0; seconds.required = true;
    const body = document.createElement("textarea"); body.maxLength = 2000; body.required = true; body.rows = 3;
    form.append(field("Name", name), field("Zeitmarke in Sekunden", seconds), button("Aktuelle Abspielposition übernehmen", () => { seconds.value = Math.floor(player.currentTime || 0); }, true), field("Kommentar", body));
    const submit = element("button", "Kommentar speichern"); form.append(submit);
    form.addEventListener("submit", run(async () => {
        await api(`/tracks/${track.id}/comments`, json("POST", {author: name.value, seconds: Number(seconds.value), body: body.value}));
        body.value = ""; await loadComments(); message("Kommentar gespeichert.");
    }));
    card.append(form); $("trackList").append(card); await loadComments();
}
$("loginForm").addEventListener("submit", run(async () => { await api("/auth/login", json("POST", {password: $("password").value})); $("password").value = ""; message("Angemeldet."); await init(); }));
$("logout").addEventListener("click", run(async () => { await api("/auth/logout", {method: "POST"}); $("trackList").replaceChildren(); message("Abgemeldet."); await init(); }));
$("setForm").addEventListener("submit", run(async () => {
    const body = Object.fromEntries(["title", "artist", "genre", "key", "status"].map(key => [key, $(key).value])); body.bpm = Number($("bpm").value) || 0;
    const id = $("trackId").value; await api(id ? `/tracks/${id}` : "/tracks/", json(id ? "PUT" : "POST", body));
    $("setForm").reset(); $("trackId").value = ""; await load(); message("Set gespeichert.");
}));
$("cancelEdit").addEventListener("click", () => { $("setForm").reset(); $("trackId").value = ""; });
$("search").addEventListener("change", run(load));
async function init() {
    const state = await api("/auth/status"); authenticated = state.authenticated;
    const isShared = Boolean(shareToken && sharedId);
    $("loginPanel").hidden = authenticated || isShared; $("setupHint").hidden = state.configured;
    $("adminPanel").hidden = !authenticated || isShared; $("sharedHint").hidden = !isShared;
    if (authenticated || isShared) await load();
}
window.addEventListener("hashchange", () => location.reload());
run(init)();
