const date = getQueryDate();
const data = await loadDailyData(date);

if (data) {
    const word = data.word;
    let readingDisplay = "";

    // Handle furigana display
    if (word.furigana) {
        // Create a series of positioned spans for each character
        readingDisplay = `
<div class="relative inline-block text-center leading-loose">
    <div class="flex justify-center items-end" style="min-height: 1.5em">
        ${word.furigana
            .map((f) => {
                if (f.type === "kanji") {
                    return `
                    <div class="flex flex-col items-center mx-0.5">
                        <span class="text-sm text-gray-600 dark:text-gray-400 h-4">${f.reading}</span>
                        <span class="text-6xl">${f.text}</span>
                    </div>`;
                } else {
                    return `
                    <div class="flex flex-col items-center mx-0.5">
                        <span class="text-sm text-gray-600 dark:text-gray-400 h-4"></span>
                        <span class="text-6xl">${f.text}</span>
                    </div>`;
                }
            })
            .join("")}
    </div>
</div>`;
    } else {
        readingDisplay = `
<div class="text-6xl mb-4">${word.writings[0]}</div>
${
    word.readings[0]
        ? `
<div class="text-2xl text-gray-600 dark:text-gray-400 mb-4">${word.readings[0].text}</div>
`
        : ""
}`;
    }

    document.getElementById("wordDetail").innerHTML = `
<div class="mb-8">
    <div class="text-lg font-bold">Word of the day ${date}</div>
</div>

<div class="text-center mb-8">
    ${readingDisplay}
    <div class="text-2xl font-bold mt-4">${word.meanings.map((m) => m.text).join(", ")}</div>
</div>

<div class="grid grid-cols-1 gap-6">
    <div>
        <h3 class="text-lg font-bold mb-2">Part of Speech</h3>
        <div class="text-lg">${word.pos.join(", ")}</div>
    </div>
    ${
        word.readings.length > 1
            ? `
    <div>
        <h3 class="text-lg font-bold mb-2">Alternative Readings</h3>
        <div class="text-lg">${word.readings
            .slice(1)
            .map((r) => r.text)
            .join(", ")}</div>
    </div>
    `
            : ""
    }
</div>`;

    // Update navigation links
    const prevDate = getPreviousDay(date);
    const nextDate = getNextDay(date);

    document.getElementById("prevDay").href =
        `word.html?date=${formatDate(prevDate)}`;
    document.getElementById("nextDay").href =
        `word.html?date=${formatDate(nextDate)}`;

    // Update page title
    document.title = `千年 - ${word.writings[0]} (${word.meanings[0].text})`;
}
