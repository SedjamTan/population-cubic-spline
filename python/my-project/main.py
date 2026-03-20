"""main script of manim"""

import math_functions
import manim
import numpy

# Typically use manim -qh main.py

class PopulationGraph(manim.Scene):
    def construct(self):
        years = [1903,1918,1939,1948,1960,1970,1975,1980,1990,1995,2000,2007,2010,2015,2020,2024]
        population = [15559,239969,319339,394642,514346,737975,
                      899529,1096046,1505219,1784441,2234088,
                      2822216,2924433,3292071,3708890,3876806]

        axes = manim.Axes(
            x_range = (1903, 2024, 11),
            y_range = (0, 4000000, 500000),
            tips = False,
            x_length=manim.config.frame_width-4,
            #axis_config={
            #    "color": BLACK
            #},
            x_axis_config={
                "decimal_number_config": {
                    "group_with_commas": False,
                    "num_decimal_places": 0
                }
            }
        )

        axes.add_coordinates()#(color=BLACK)

        x_lab = axes.get_x_axis_label("Year")
        y_lab = axes.get_y_axis_label("Population")
        #y_lab.color = x_lab.color = BLACK

        self.play(manim.Write(axes), manim.Write(x_lab), manim.Write(y_lab))

        for year, pop in zip(years, population):
            point = (year,pop)
            dot_coord = manim.Dot(axes.c2p(*point),color=manim.YELLOW,z_index=2)
            self.add(dot_coord)
            self.wait(0.06)

        f1_plot = axes.plot(math_functions.f1,x_range=[1903,1918], color = manim.BLUE)
        f2_plot = axes.plot(math_functions.f2,x_range=[1918,1939], color = manim.BLUE)
        f3_plot = axes.plot(math_functions.f3,x_range=[1939,1948], color = manim.BLUE)
        f4_plot = axes.plot(math_functions.f4,x_range=[1948,1960], color = manim.BLUE)
        f5_plot = axes.plot(math_functions.f5,x_range=[1960,1970], color = manim.BLUE)
        f6_plot = axes.plot(math_functions.f6,x_range=[1970,1975], color = manim.BLUE)
        f7_plot = axes.plot(math_functions.f7,x_range=[1975,1980], color = manim.BLUE)
        f8_plot = axes.plot(math_functions.f8,x_range=[1980,1990], color = manim.BLUE)
        f9_plot = axes.plot(math_functions.f9,x_range=[1990,1995], color = manim.BLUE)
        f10_plot = axes.plot(math_functions.f10,x_range=[1995,2000], color = manim.BLUE)
        f11_plot = axes.plot(math_functions.f11,x_range=[2000,2007], color = manim.BLUE)
        f12_plot = axes.plot(math_functions.f12,x_range=[2007,2010], color = manim.BLUE)
        f13_plot = axes.plot(math_functions.f13,x_range=[2010,2015], color = manim.BLUE)
        f14_plot = axes.plot(math_functions.f14,x_range=[2015,2020], color = manim.BLUE)
        f15_plot = axes.plot(math_functions.f15,x_range=[2020,2024], color = manim.BLUE)
        interpolation_func = [f1_plot,f2_plot,f3_plot,f4_plot,f5_plot,
                              f6_plot,f7_plot,f8_plot,f9_plot,f10_plot,
                              f11_plot,f12_plot,f13_plot,f14_plot,f15_plot]

        create_func = []
        for func in interpolation_func:
            create_func.append(manim.Create(func))

        self.play(create_func)
        self.wait(2)

class PopulationGrowth(manim.Scene):
    def construct(self):
        axes = manim.Axes(
            x_range = (1903, 2024, 11),
            y_range = (0, 100000, 10000),
            tips = False,
            x_length=manim.config.frame_width-4,
            #axis_config={
            #    "color": BLACK
            #},
            x_axis_config={
                "decimal_number_config": {
                    "group_with_commas": False,
                    "num_decimal_places": 0
                }
            }
        )

        axes.add_coordinates()#(color=BLACK)

        x_lab = axes.get_x_axis_label("Year")
        y_lab = axes.get_y_axis_label(manim.Tex("Population Growth Rate"))
        #y_lab.color = x_lab.color = BLACK

        self.play(manim.Write(axes), manim.Write(x_lab), manim.Write(y_lab))

        f1p_plot = axes.plot(math_functions.f1p,x_range=[1903,1918],color = manim.BLUE)
        f2p_plot = axes.plot(math_functions.f2p,x_range=[1918,1939],color = manim.BLUE)
        f3p_plot = axes.plot(math_functions.f3p,x_range=[1939,1948],color = manim.BLUE)
        f4p_plot = axes.plot(math_functions.f4p,x_range=[1948,1960],color = manim.BLUE)
        f5p_plot = axes.plot(math_functions.f5p,x_range=[1960,1970],color = manim.BLUE)
        f6p_plot = axes.plot(math_functions.f6p,x_range=[1970,1975],color = manim.BLUE)
        f7p_plot = axes.plot(math_functions.f7p,x_range=[1975,1980],color = manim.BLUE)
        f8p_plot = axes.plot(math_functions.f8p,x_range=[1980,1990],color = manim.BLUE)
        f9p_plot = axes.plot(math_functions.f9p,x_range=[1990,1995],color = manim.BLUE)
        f10p_plot = axes.plot(math_functions.f10p,x_range=[1995,2000],color = manim.BLUE)
        f11p_plot = axes.plot(math_functions.f11p,x_range=[2000,2007],color = manim.BLUE)
        f12p_plot = axes.plot(math_functions.f12p,x_range=[2007,2010],color = manim.BLUE)
        f13p_plot = axes.plot(math_functions.f13p,x_range=[2010,2015],color = manim.BLUE)
        f14p_plot = axes.plot(math_functions.f14p,x_range=[2015,2020],color = manim.BLUE)
        f15p_plot = axes.plot(math_functions.f15p,x_range=[2020,2024],color = manim.BLUE)
        first_derivative_func = [f1p_plot,f2p_plot,f3p_plot,f4p_plot,f5p_plot,
                                 f6p_plot,f7p_plot,f8p_plot,f9p_plot,f10p_plot,
                                 f11p_plot,f12p_plot,f13p_plot,f14p_plot,f15p_plot]

        for func in first_derivative_func:
            self.play(manim.Create(func), run_time=0.5)

        self.wait(2)

        x = numpy.linspace(2000,2001)
        y = math_functions.f11p(x)

        peak_index = manim.np.argmax(y)
        peak_x = x[peak_index]
        peak_y = y[peak_index]

        point = axes.c2p(peak_x, peak_y)
        dot = manim.Dot(point,color=manim.YELLOW,z_index=2)

        title = f"\\text{{Growth rate:}} \\\\ \\text{{{peak_y:.0f} people/year at {peak_x:.2f}}}"
        label = manim.MathTex(title,font_size=25).move_to(axes.c2p(peak_x,peak_y) + manim.LEFT*2)

        self.add(dot)
        self.play(manim.Create(label))
        self.wait(2)

class PopulationAccelerate(manim.Scene):
    def construct(self):
        axes = manim.Axes(
            x_range = (1903, 2024, 11),
            y_range = (-20000, 20000, 5000),
            tips = False,
            x_length=manim.config.frame_width-4,
            #axis_config={
            #    "color": BLACK
            #},
            x_axis_config={
                "decimal_number_config": {
                    "group_with_commas": False,
                    "num_decimal_places": 0
                }
            }
        )

        axes.add_coordinates()#(color=BLACK)
        x_lab = axes.get_x_axis_label("Year")
        y_lab = axes.get_y_axis_label(manim.Tex("Population Growth Acceleration"))
        #y_lab.color = x_lab.color = BLACK

        self.play(manim.Write(axes), manim.Write(x_lab), manim.Write(y_lab))

        f1pp_plot = axes.plot(math_functions.f1pp,x_range=[1903,1918],color = manim.BLUE)
        f2pp_plot = axes.plot(math_functions.f2pp,x_range=[1918,1939],color = manim.BLUE)
        f3pp_plot = axes.plot(math_functions.f3pp,x_range=[1939,1948],color = manim.BLUE)
        f4pp_plot = axes.plot(math_functions.f4pp,x_range=[1948,1960],color = manim.BLUE)
        f5pp_plot = axes.plot(math_functions.f5pp,x_range=[1960,1970],color = manim.BLUE)
        f6pp_plot = axes.plot(math_functions.f6pp,x_range=[1970,1975],color = manim.BLUE)
        f7pp_plot = axes.plot(math_functions.f7pp,x_range=[1975,1980],color = manim.BLUE)
        f8pp_plot = axes.plot(math_functions.f8pp,x_range=[1980,1990],color = manim.BLUE)
        f9pp_plot = axes.plot(math_functions.f9pp,x_range=[1990,1995],color = manim.BLUE)
        f10pp_plot = axes.plot(math_functions.f10pp,x_range=[1995,2000],color = manim.BLUE)
        f11pp_plot = axes.plot(math_functions.f11pp,x_range=[2000,2007],color = manim.BLUE)
        f12pp_plot = axes.plot(math_functions.f12pp,x_range=[2007,2010],color = manim.BLUE)
        f13pp_plot = axes.plot(math_functions.f13pp,x_range=[2010,2015],color = manim.BLUE)
        f14pp_plot = axes.plot(math_functions.f14pp,x_range=[2015,2020],color = manim.BLUE)
        f15pp_plot = axes.plot(math_functions.f15pp,x_range=[2020,2024],color = manim.BLUE)
        second_derivative_func = [f1pp_plot,f2pp_plot,f3pp_plot,f4pp_plot,f5pp_plot,
                                  f6pp_plot,f7pp_plot,f8pp_plot,f9pp_plot,f10pp_plot,
                                  f11pp_plot,f12pp_plot,f13pp_plot,f14pp_plot,f15pp_plot]

        for func in second_derivative_func:
            self.play(manim.Create(func), run_time=0.5)

        self.wait(2)

        x = numpy.linspace(2010,2015)
        y = math_functions.f13pp(x)

        peak_index = manim.np.argmax(y)
        peak_x = x[peak_index]
        peak_y = y[peak_index]

        point = axes.c2p(peak_x, peak_y)
        dot = manim.Dot(point,color=manim.YELLOW,z_index=2)

        title = rf"""
                \text{{Acceleration of Growth Rate:}} \\ 
                \text{{{peak_y:.0f} people / year}}^2 
                \text{{at {peak_x:.2f}}}
                """

        label = manim.MathTex(title,font_size=25).move_to(axes.c2p(peak_x,peak_y) + manim.LEFT*2)

        self.add(dot)
        self.play(manim.Create(label))
        self.wait(2)

class InterpolateExample(manim.Scene):
    def construct(self):
        axes = manim.Axes(
            x_range = (-8, 8, 1),
            y_range = (-4, 8, 1),
            tips = False,
            x_length=manim.config.frame_width-1,
            x_axis_config={
                "decimal_number_config": {
                    "group_with_commas": False,
                    "num_decimal_places": 0
                }
            }
        )

        self.play(manim.Write(axes))

        points = [[-3,1],[-2,5],[-1,3],[0,1],[1,5]]
        for point in points:
            point = (point[0],point[1])
            dot_coord = manim.Dot(axes.c2p(*point),color=manim.YELLOW,z_index=2)
            self.add(dot_coord)
            self.wait(0.5)

        self.wait(1)

        equation = r"""f(x_i)=y_i,\quad for \;i =1,2,3,...,n."""
        eq = manim.MathTex(equation,font_size=40).move_to(manim.RIGHT*4)

        self.play(manim.Write(eq))
        self.wait(1)

        f1_plot = axes.plot(math_functions.example_f,x_range=[-5,5], color = manim.BLUE)

        self.play(manim.Create(f1_plot))

class LogisticGrowthModel(manim.Scene):
    def construct(self):
        equation = r"""P(t) = \frac{a}{1 + e^{-b(t-c)}}"""
        label = r"""\text{Logistic Growth Model}"""

        eq = manim.MathTex(equation,font_size=50)
        title = manim.MathTex(label,font_size=50).next_to(eq, manim.UP)

        self.play(manim.Write(title), manim.Write(eq))
        self.play(
            eq.animate.shift(manim.LEFT * 5),
            title.animate.shift(manim.UP * 2)
        )

        characteristics = manim.Tex(r"""\begin{itemize}
                                    \item Population grows rapidly, then slows down
                                    \item Limited by environmental factors
                                    \item Forms an S-shaped curve
                                \end{itemize}
                                """).next_to(eq, manim.RIGHT*2)

        self.play(manim.Write(characteristics))

class GrowthFunctions(manim.Scene):
    def construct(self):
        growth_rate = r"""P^{\prime}(t) = \frac{dP(t)}{dt}"""
        growth_accelerate = r"""P^{\prime\prime}(t) = \frac{d^2P(t)}{dt^2}"""

        label_growth_rate = r"""Growth Rate"""
        label_growth_accelerate = r"""Growth Acceleration"""

        eq1 = manim.MathTex(growth_rate,font_size=100).move_to((manim.UP*1.5))

        self.play(manim.Write(eq1))
        self.play(eq1.animate.shift(manim.LEFT * 3))

        title1 = manim.Tex(label_growth_rate).move_to(eq1.get_right() + manim.RIGHT*4)

        self.play(manim.Write(title1))
        self.wait(1)

        eq2 = manim.MathTex(growth_accelerate,font_size=100).next_to(eq1,manim.DOWN)
        title2 = manim.Tex(label_growth_accelerate).move_to(eq2.get_right() + manim.RIGHT*4)

        self.play(manim.Write(eq2))
        self.play(manim.Write(title2))
        self.wait(2)

        rule_growth_rate = r"""\text{If } P^{\prime}(t)>0
                            \text{, then the population is increasing} \\
                            \text{If }P^{\prime}(t)<0
                            \text{, then the population is decreasing}"""

        rule_growth_accelerate = r"""\text{If } P^{\prime\prime}(t)>0
                                \text{, then population growth is accelerating} \\
                                \text{If } P^{\prime\prime}(t)<0
                                \text{, then population growth is decelerating}"""

        rule1 = manim.MathTex(rule_growth_rate, font_size=50).move_to((manim.UP*1.5))
        rule2 = manim.MathTex(rule_growth_accelerate, font_size=50).next_to(rule1,manim.DOWN*6)

        self.play(
            manim.FadeOut(eq1),
            manim.FadeOut(eq2),
            title1.animate.next_to(rule1,manim.UP,buff=0.25),
            title2.animate.next_to(rule2,manim.UP,buff=0.25)
        )

        self.play(manim.Write(rule1), manim.Write(rule2))
        self.wait(2)
