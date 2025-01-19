function toggleDarkMode() {
    if (localStorage.theme === "light") {
        console.log("setting light theme");
        localStorage.theme = "dark";
        document.documentElement.classList.add("dark");
    } else if (localStorage.theme === "dark") {
        console.log("setting dark theme");
        localStorage.theme = "light";
        document.documentElement.classList.remove("dark");
    } else {
        localStorage.theme = "light";
        toggleDarkMode();
    }
}
