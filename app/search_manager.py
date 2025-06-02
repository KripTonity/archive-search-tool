from app.scrapers import wayback, mementoweb, rusweb, runivers, shidianguji, webarchiv, arquivo

SCRAPER_MAP = {
    "wayback": wayback,
    "mementoweb": mementoweb,
    "rusweb": rusweb,
    "runivers": runivers,
    "shidianguji": shidianguji,
    "webarchiv": webarchiv,
    "arquivo": arquivo
}

def perform_search(query, selected_sites):
    results = {}
    for site in selected_sites:
        scraper = SCRAPER_MAP.get(site)
        if scraper:
            try:
                results[site] = scraper.search(query)  # list of (title, link)
            except Exception as e:
                results[site] = [(f"[ERROR] {site}", str(e))]
    return results

