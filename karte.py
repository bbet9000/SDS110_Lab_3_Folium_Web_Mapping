import folium  # Import the folium library for creating interactive maps

# Create a Folium map object
m = folium.Map(
    location=[47.396, 8.549],
    tiles="OpenStreetMap",  # Other options are listed below
    zoom_start=13
)

# Available built-in basemap options in Folium:
# tiles="OpenStreetMap"         # Default OSM basemap
# tiles="Cartodb Positron"      # Light-colored basemap (good for overlays)
# tiles="Cartodb Dark_Matter"   # Dark-colored basemap

# You can also add custom tiles (like SwissTopo or others):
# tiles="https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png", attr="© OpenTopoMap (CC-BY-SA)",

m
