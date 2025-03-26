document.addEventListener("DOMContentLoaded", function () {
    const chartContainer = document.getElementById('marketChart');
    chartContainer.innerHTML = '';

    const chart = LightweightCharts.createChart(chartContainer, {
        width: chartContainer.clientWidth,
        height: 450,
        layout: { background: { color: '#ffffff' }, textColor: '#000' },
        grid: { vertLines: { color: '#e1e1e1' }, horzLines: { color: '#e1e1e1' } },
    });

    const rawData = JSON.parse(document.getElementById("chart-data").textContent);
    let filteredData = [...rawData];
    let series = chart.addLineSeries({ color: '#26a69a', lineWidth: 2 });

    function parseDate(dateString) {
        return new Date(dateString + "T00:00:00Z");
    }

    function filterDataByDate(range) {
        const now = new Date();
        let startDate = new Date();

        if (range === "one-day") startDate.setDate(now.getDate() - 1);
        else if (range === "one-week") startDate.setDate(now.getDate() - 7);
        else if (range === "one-month") startDate.setMonth(now.getMonth() - 1);
        else if (range === "three-month") startDate.setMonth(now.getMonth() - 3);
        else if (range === "one-year") startDate.setFullYear(now.getFullYear() - 1);

        return rawData.filter(d => parseDate(d.time) >= startDate);
    }

    function updateChart() {
        const type = document.getElementById("chartType").value;
        chart.removeSeries(series);

        if (type === "candlestick") {
            series = chart.addCandlestickSeries({
                upColor: '#26a69a', downColor: '#ef5350',
                borderUpColor: '#26a69a', borderDownColor: '#ef5350',
                wickUpColor: '#26a69a', wickDownColor: '#ef5350',
            });
            series.setData(filteredData);
        } else if (type === "bar") {
            series = chart.addBarSeries({
                upColor: '#26a69a', downColor: '#ef5350',
                borderUpColor: '#26a69a', borderDownColor: '#ef5350',
            });
            series.setData(filteredData);
        } else {
            const lineData = filteredData.map(d => ({ time: d.time, value: d.close }));
            series = chart.addLineSeries({ color: '#26a69a', lineWidth: 2 });
            series.setData(lineData);
        }
    }

    document.getElementById("chartType").addEventListener("change", updateChart);
    document.getElementById("datefilter").addEventListener("change", function (event) {
        filteredData = filterDataByDate(event.target.value);
        updateChart();
    });

    filteredData = filterDataByDate("one-year");
    updateChart();

    window.addEventListener('resize', () => {
        chart.applyOptions({ width: chartContainer.clientWidth });
    });
});
