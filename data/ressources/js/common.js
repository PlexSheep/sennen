// Base URL is defined in HTML files
const BASE_URL = window.BASE_URL;

// Utility functions for date handling
function formatDate(date) {
    date = new Date(date); // I swear I hate JavaScript so much
    return date.toISOString().split("T")[0];
}

function getNextDay(date) {
    const next = new Date(date);
    next.setDate(next.getDate() + 1);
    return next;
}

function getPreviousDay(date) {
    const prev = new Date(date);
    prev.setDate(prev.getDate() - 1);
    return prev;
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
