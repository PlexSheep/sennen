const date = getQueryDate();
const data = await loadDailyData(date);
if (data) {
    const kanji = data.kanji;
    document.getElementById("kanjiDetail").innerHTML = `
<div class="mb-8">
    <div class="text-lg font-bold">Kanji of the day ${date}</div>
</div>
<div class="text-center mb-8">
    <div class="text-8xl mb-4">${kanji.kanji}</div>
    <div class="text-2xl font-bold">${kanji.meanings.join(", ")}</div>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-8">
    <div>
        <h3 class="text-lg font-bold mb-2">Kun Readings</h3>
        <div class="text-lg">${kanji.kun_readings.join(", ") || "None"}</div>
    </div>
    <div>
        <h3 class="text-lg font-bold mb-2">On Readings</h3>
        <div class="text-lg">${kanji.on_readings.join(", ") || "None"}</div>
    </div>
</div>
<div class="mt-8 grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
    <div class="stats bg-gray-50 dark:bg-gray-700 p-4 rounded">
        <div class="font-bold">Grade</div>
        <div>${kanji.grade || "N/A"}</div>
    </div>
    <div class="stats bg-gray-50 dark:bg-gray-700 p-4 rounded">
        <div class="font-bold">JLPT</div>
        <div>N${kanji.jlpt || "N/A"}</div>
    </div>
    <div class="stats bg-gray-50 dark:bg-gray-700 p-4 rounded">
        <div class="font-bold">Strokes</div>
        <div>${kanji.stroke_count}</div>
    </div>
    <div class="stats bg-gray-50 dark:bg-gray-700 p-4 rounded">
        <div class="font-bold">Frequency</div>
        <div>${kanji.frequency || "N/A"}</div>
    </div>
</div>
`;
    // Update navigation links
    const prevDate = getPreviousDay(date);
    const nextDate = getNextDay(date);
    document.getElementById("prevDay").href = getKanjiUrl(prevDate);
    document.getElementById("nextDay").href = getKanjiUrl(nextDate);
    // Update page title
    document.title = `千年 - ${kanji.self} (${kanji.meanings[0]})`;
}
