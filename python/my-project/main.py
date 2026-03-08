from manim import * 
class axes(Scene):
    def construct(self):
        axes = Axes(
            x_range = (1903, 2024, 11), 
            y_range = (0, 4000000, 500000), 
            tips = False,
            x_axis_config={
                "decimal_number_config": {
                    "group_with_commas": False,
                    "num_decimal_places": 0
                }
            }
            )
        axes.shift(RIGHT * 0.7)
        axes.add_coordinates()
        x_lab = axes.get_x_axis_label("Year")
        y_lab = axes.get_y_axis_label("Population")

        self.play(Write(axes), Write(x_lab), Write(y_lab))

        f1 = axes.plot(lambda x: ((12.327801029757717)*((x-1903)**3))+((-9.393051541049447*10**2)*((x-1903)**2))+((2.627648874654535*10**4)*(x-1903))+15559,x_range=[1903,1918], color = BLUE)

        self.play(Write(f1))
        self.wait(2)
    # use manim -pqh main.py