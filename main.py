import medical_data_visualizer

# Generate and save the categorical plot
cat_plot_fig = medical_data_visualizer.draw_cat_plot()
cat_plot_fig.savefig("catplot.png")

# Generate and save the heatmap
heat_map_fig = medical_data_visualizer.draw_heat_map()
heat_map_fig.savefig("heatmap.png")

print("Plots saved successfully.")
