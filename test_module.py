import unittest
import medical_data_visualizer

class MedicalDataTestCase(unittest.TestCase):
    def test_cat_plot(self):
        fig = medical_data_visualizer.draw_cat_plot()
        self.assertIsNotNone(fig)

    def test_heat_map(self):
        fig = medical_data_visualizer.draw_heat_map()
        self.assertIsNotNone(fig)

if __name__ == "__main__":
    unittest.main()
