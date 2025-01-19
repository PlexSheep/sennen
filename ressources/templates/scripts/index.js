const today = new Date();
const data = await loadDailyData(today);

if (data) {
    const { kanji, word } = data;

    // Update Kanji
    document.getElementById("kanjiWriting").innerHTML = kanji.kanji;
    document.getElementById("kanjiMeaning").innerHTML =
        kanji.meanings.join(", ");
    document.getElementById("kanjiLink").href = `kanji.html?date=${data.date}`;
    document.getElementById("kanjiLoad").remove();

    // Update Word
    document.getElementById("wordWriting").innerHTML = renderFurigana(
        word,
        "6xl",
    );
    document.getElementById("wordMeaning").innerHTML = word.meanings
        .map((m) => m.text)
        .join(", ");
    document.getElementById("wordLink").href = `word.html?date=${data.date}`;
    document.getElementById("wordLoad").remove();

    // Update navigation links
    document.getElementById("yesterdayLink").href = getKanjiUrl(
        getPreviousDay(today),
    );
    document.getElementById("tomorrowLink").href = getKanjiUrl(
        getNextDay(today),
    );
}
