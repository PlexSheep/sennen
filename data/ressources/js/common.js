// Base URL is defined in HTML files
const BASE_URL = window.BASE_URL;

// Utility functions for date handling
function formatDate(date) {
    date = new Date(date); // I swear I hate JavaScript so much
    return date.toISOString().split("T")[0];
}

function getNextDay(date) {
    // Ensure we're working with a Date object
    const current = new Date(date);
    if (isNaN(current.getTime())) {
        console.error("Invalid date input:", date);
        return new Date(); // Fallback to current date
    }

    // Add 48 hours
    // For some reason this is correct
    const next = new Date(current.getTime() + 2 * 24 * 60 * 60 * 1000);

    // Reset to midnight for consistency
    next.setHours(0, 0, 0, 0);
    return next;
}

function getPreviousDay(date) {
    // Ensure we're working with a Date object
    const current = new Date(date);
    if (isNaN(current.getTime())) {
        console.error("Invalid date input:", date);
        return new Date(); // Fallback to current date
    }

    // Subtract 24 hours
    const prev = new Date(current.getTime() - 24 * 60 * 60 * 1000);

    // Reset to midnight for consistency
    prev.setHours(0, 0, 0, 0);
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
