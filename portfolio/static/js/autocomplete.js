document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("symbolInput");
    const resultsContainer = document.getElementById("autocomplete-results");
    const portfolioId = input.dataset.portfolioId;
    let debounceTimeout = null;
    let currentController = null;


    async function fetchResults(query) {
        if (currentController) {
            currentController.abort();
        }
        currentController = new AbortController();

        try {
            const response = await fetch(`/portfolio/${portfolioId}/search/?query=${query}`, {
                headers: { "X-Requested-With": "XMLHttpRequest" },
                signal: currentController.signal,
            });

            if (!response.ok) throw new Error("❌ Error in the API");

            const data = await response.json();
            displayResults(data);
        } catch (error) {
            if (error.name !== "AbortError") {
                console.error("❌ Error in the API:", error);
            }
        }
    }

    function displayResults(data) {
        resultsContainer.innerHTML = "";
        if (data.length > 0) {
            resultsContainer.style.display = "block";
            data.slice(0, 7).forEach(asset => {
                const item = document.createElement("a");
                item.href = "#";
                item.classList.add("list-group-item", "list-group-item-action");
                item.textContent = `${asset.symbol} - ${asset.name}`;

                item.addEventListener("click", function (e) {
                    e.preventDefault();
                    input.value = asset.symbol;
                    resultsContainer.style.display = "none";
                    document.querySelector("form").submit();
                });

                resultsContainer.appendChild(item);
            });
        } else {
            resultsContainer.style.display = "none";
        }
    }

    input.addEventListener("input", function () {
        clearTimeout(debounceTimeout);
        const query = input.value.trim();

        if (query.length < 1) {
            resultsContainer.style.display = "none";
            return;
        }

        debounceTimeout = setTimeout(() => {
            fetchResults(query);
        }, 300);
    });

    document.addEventListener("click", function (e) {
        if (!resultsContainer.contains(e.target) && e.target !== input) {
            resultsContainer.style.display = "none";
        }
    });
});
