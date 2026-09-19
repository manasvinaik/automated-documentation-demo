(function () {
    const CHECK_INTERVAL = 30000; // 30 seconds

    let currentVersion = null;

    async function checkForUpdates() {
        try {
            const response = await fetch(
                `/version.txt?cacheBust=${Date.now()}`,
                {
                    cache: "no-store"
                }
            );

            if (!response.ok) {
                return;
            }

            const newVersion = (await response.text()).trim();

            if (!newVersion) {
                return;
            }

            if (currentVersion === null) {
                currentVersion = newVersion;
                return;
            }

            if (newVersion !== currentVersion) {
                console.log("New documentation version detected.");
                window.location.reload();
            }

        } catch (error) {
            console.log("Could not check for documentation updates.");
        }
    }

    checkForUpdates();

    setInterval(checkForUpdates, CHECK_INTERVAL);
})();