import tkinter as tk
from tkinter import filedialog
import shape_matching
import file_io
import visualization

class ShapeMatchingGUI:
    def __init__(self, root):
        self.root = root
        self.file_path = ""
        # Create GUI components and layout

    def select_file(self):
        # Open file dialog to select a measurement file
        self.file_path = filedialog.askopenfilename()

    def match_shapes(self):
        # Load the measurement file and perform shape matching
        shape1 = file_io.load_measurement_file(self.file_path)
        shape2 = []  # Replace with the second shape to be matched
        processed_shape1 = shape_matching.preprocess_shape(shape1)
        processed_shape2 = shape_matching.preprocess_shape(shape2)
        cost_matrix = shape_matching.compute_cost_matrix(processed_shape1, processed_shape2)
        accumulated_cost_matrix = shape_matching.compute_accumulated_cost_matrix(cost_matrix)
        optimal_path = shape_matching.compute_optimal_path(accumulated_cost_matrix)
        similarity = shape_matching.measure_similarity(optimal_path)
        # Display the matching results
        visualization.visualize_shapes(shape1, shape2, alignment=optimal_path)
        # Update GUI to show the similarity measure and other relevant information
        # Update GUI to show the similarity measure and other relevant information
        self.result_label.config(text=f"Similarity: {similarity}")
        
    def save_results(self):
        # Save the matching results to a file
        results = {}  # Replace with the actual results to be saved
        file_io.save_results(results, self.file_path)
        
    def export_visualization(self):
        # Export the visualization to a file
        visualization.export_visualization(self.canvas, self.file_path)

    def create_gui_components(self):
        # Create and configure the GUI components
        self.file_button = tk.Button(self.root, text="Select File", command=self.select_file)
        self.match_button = tk.Button(self.root, text="Match Shapes", command=self.match_shapes)
        self.save_button = tk.Button(self.root, text="Save Results", command=self.save_results)
        self.export_button = tk.Button(self.root, text="Export Visualization", command=self.export_visualization)
        self.result_label = tk.Label(self.root, text="Similarity: ")

    def layout_gui_components(self):
        # Layout the GUI components using grid or pack
        self.file_button.grid(row=0, column=0)
        self.match_button.grid(row=1, column=0)
        self.save_button.grid(row=2, column=0)
        self.export_button.grid(row=3, column=0)
        self.result_label.grid(row=4, column=0)

    def start_gui(self):
        # Initialize and start the GUI
        self.create_gui_components()
        self.layout_gui_components()
        self.root.mainloop()
