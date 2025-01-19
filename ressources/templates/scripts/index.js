const today = new Date();
const data = await loadDailyData(today);

if (data) {
    const { kanji, word } = data;

    // Update Kanji
    document.getElementById("kanjiContent").innerHTML = `
        <a href="kanji.html?date=${data.date}" class="block text-center hover:opacity-80 transition-opacity">
            <div class="text-7xl mb-4">${kanji.kanji}</div>
            <div class="text-xl">${kanji.meanings.join(", ")}</div>
        </a>
    `;

    // Update Word
    document.getElementById("wordContent").innerHTML = `
        <a href="word.html?date=${data.date}" class="block text-center hover:opacity-80 transition-opacity">
            ${renderFurigana(word, "4xl")}
            <div class="text-lg">${word.meanings.map((m) => m.text).join(", ")}</div>
        </a>
    `;

    // Update navigation links
    document.getElementById("yesterdayLink").href = getKanjiUrl(
        getPreviousDay(today),
    );
    document.getElementById("tomorrowLink").href = getKanjiUrl(
        getNextDay(today),
    );
}
