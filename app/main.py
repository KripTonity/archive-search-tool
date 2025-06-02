import dearpygui.dearpygui as dpg
from app.search_manager import perform_search
from app.web_preview import open_preview

# Liste des sites disponibles
available_sites = [
    "wayback",
    "mementoweb",
    "rusweb",
    "runivers",
    "shidianguji",
    "webarchiv",
    "arquivo"
]

# Callback déclenché quand on clique sur "Search"
def on_search_click():
    query = dpg.get_value("search_input")
    selected_sites = [site for site in available_sites if dpg.get_value(f"checkbox_{site}")]
    results = perform_search(query, selected_sites)

    # Nettoyage de la zone de résultats
    dpg.delete_item("results_group", children_only=True)

    for site, entries in results.items():
        dpg.add_text(f"--- {site.upper()} ---", parent="results_group")
        for title, link in entries:
            # Capture correcte du lien dans lambda
            dpg.add_button(label=title, callback=lambda _, s=link: open_preview(s), parent="results_group")

# Fonction principale
def main():
    dpg.create_context()
    dpg.create_viewport(title="Multi-Archive Search Tool", width=700, height=500)

    with dpg.window(label="Search Tool", width=680, height=480):
        dpg.add_input_text(label="Search", tag="search_input")
        dpg.add_text("Select sources:")

        for site in available_sites:
            dpg.add_checkbox(label=site.capitalize(), tag=f"checkbox_{site}", default_value=True)

        dpg.add_button(label="Search", callback=on_search_click)

        # Zone où les résultats s'affichent dynamiquement
        with dpg.group(tag="results_group"):
            dpg.add_text("Results will appear here")

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
