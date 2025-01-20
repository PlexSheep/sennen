// Base URL is defined in HTML files
const BASE_URL = window.BASE_URL;

// Utility functions for date handling
function formatDate(date) {
    date = new Date(date); // I swear I hate JavaScript so much
    return date.toISOString().split("T")[0];
}

function getNextDay(date) {
    var d = new Date(date);
    d.setDate(d.getDate() + 1);
    return d;
}

function getPreviousDay(date) {
    var d = new Date(date);
    d.setDate(d.getDate() - 1);
    return d;
}

// API functions
async function loadDailyData(date) {
    const dateStr = formatDate(date);
    try {
        const response = await fetch(
            `${BASE_URL}/api/v1/daily/${dateStr}.json`,
        );
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Error loading data:", error);
        return null;
    }
}

// URL parameter handling
function getQueryDate() {
    const params = new URLSearchParams(window.location.search);
    return params.get("date") || formatDate(new Date());
}

// Navigation helpers
function getKanjiUrl(date) {
    return `${BASE_URL}/kanji.html?date=${formatDate(date)}`;
}

function getHomeUrl() {
    return `${BASE_URL}/index.html`;
}

function renderFurigana(word, size = "6xl", furigana_size = "base") {
    if (!word.furigana) {
        return `
            <div class="text-${size} mb-4">${word.writings[0]}</div>
            ${
                word.readings[0]
                    ? `
                <div class="text-2xl text-gray-600 dark:text-gray-400 mb-7">${word.readings[0].text}</div>
            `
                    : ""
            }
        `;
    }

    return `
        <div class="relative text-center leading-loose">
            <div class="flex justify-center items-end self-start" style="min-height: 1.5em">
                ${word.furigana
                    .map((f) => {
                        if (f.type === "kanji") {
                            return `
                            <div class="flex flex-col items-center mx-0.5 mb-6">
                                <span class="text-${furigana_size} text-gray-600 dark:text-gray-400 h-4 mb-2">${f.reading}</span>
                                <span class="text-${size}">${f.text}</span>
                            </div>`;
                        } else {
                            return `
                            <div class="flex flex-col items-center mx-0.5 mb-6">
                                <span class="text-${furigana_size} text-gray-600 dark:text-gray-400 h-4 mb-2"></span>
                                <span class="text-${size}">${f.text}</span>
                            </div>`;
                        }
                    })
                    .join("")}
            </div>
        </div>
    `;
}
