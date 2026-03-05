from manim import * 
class axes(Scene):
    def construct(self):
        axes = Axes(x_range = (-1, 12), y_range = (-1, 6), tips = False)
        axes.add_coordinates()
        x_lab = axes.get_x_axis_label("X axis")
        y_lab = axes.get_y_axis_label("Y axis")

        self.play(Write(axes), Write(x_lab), Write(y_lab))
        
        rec = Rectangle(height = 0.5, width = 0.5)
        rec.move_to(axes.c2p(4, 2))

        self.play(Write(rec))
        self.wait(2)