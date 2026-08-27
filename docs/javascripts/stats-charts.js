// PEPkit usage statistics charts.
// Data source: https://github.com/databio/stats, served via GitHub Pages at
// https://stats.databio.org and refreshed monthly by that repo's
// .github/workflows/update_stats.yaml.
(function () {
  var STATS_BASE = 'https://stats.databio.org';

  // Maps data-chart-type to the directory under /stats/ in the stats repo.
  var SOURCES = {
    pypi: 'pypi_downloads',
    cran: 'cran_downloads',
    bioc: 'bioc_downloads'
  };

  var chartConfig = {
    title: {
      fontSize: 18, font: 'Arial', anchor: 'middle',
      color: '#000000', fontWeight: 'normal'
    },
    axis: {
      titleFontSize: 14, titleFont: 'Arial', titleFontWeight: 'normal',
      labelFontSize: 11, labelFont: 'Arial', labelFontWeight: 'normal',
      grid: false
    },
    view: { strokeWidth: 0 }
  };

  function downloadsSpec(source, pkg, label) {
    return {
      $schema: 'https://vega.github.io/schema/vega-lite/v5.json',
      title: 'Downloads of ' + (label || pkg),
      width: 'container',
      height: 150,
      data: {
        url: STATS_BASE + '/stats/' + source + '/' + pkg + '.tsv',
        format: { type: 'dsv', delimiter: '\t' }
      },
      transform: [{ calculate: 'datum.downloads / 1000', as: 'downloads_k' }],
      mark: { type: 'bar', color: '#5a5a5a' },
      encoding: {
        x: {
          field: 'month', timeUnit: 'utcyearmonth', type: 'ordinal',
          title: 'Date', axis: { labelAngle: -90 }
        },
        y: {
          field: 'downloads_k', type: 'quantitative',
          title: 'Downloads (thousands)'
        },
        tooltip: [
          { field: 'month', type: 'temporal', title: 'Month', format: '%B %Y' },
          { field: 'downloads', type: 'quantitative', title: 'Downloads', format: ',' }
        ]
      },
      config: chartConfig
    };
  }

  function renderCharts() {
    document.querySelectorAll('[data-chart-type]').forEach(function (el) {
      if (el.dataset.chartRendered) return;
      el.dataset.chartRendered = '1';

      var source = SOURCES[el.getAttribute('data-chart-type')];
      if (!source) return;

      var spec = downloadsSpec(
        source,
        el.getAttribute('data-package'),
        el.getAttribute('data-label')
      );

      vegaEmbed('#' + el.id, spec, { renderer: 'svg', actions: false })
        .catch(function () {
          el.innerHTML = '<p class="chart-error">No data available</p>';
        });
    });
  }

  if (window.document$ && typeof window.document$.subscribe === 'function') {
    window.document$.subscribe(renderCharts);   // mkdocs-material instant nav
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderCharts);
  } else {
    renderCharts();
  }
})();
