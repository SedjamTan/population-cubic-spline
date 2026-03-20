from manim import * 
import numpy

# Typically use manim -qh main.py

class population_graph(Scene):
    def construct(self):
        years = [1903,1918,1939,1948,1960,1970,1975,1980,1990,1995,2000,2007,2010,2015,2020,2024]
        population = [15559,239969,319339,394642,514346,737975,
                      899529,1096046,1505219,1784441,2234088,
                      2822216,2924433,3292071,3708890,3876806]

        axes = Axes(
            x_range = (1903, 2024, 11), 
            y_range = (0, 4000000, 500000), 
            tips = False,
            x_length=config.frame_width-4,
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

        self.play(Write(axes), Write(x_lab), Write(y_lab))

        for year, pop in zip(years, population):
            point = (year,pop)
            dot_coord = Dot(axes.c2p(*point),color=YELLOW,z_index=2)
            self.add(dot_coord)
            self.wait(0.06)

        f1 = lambda x: ((12.327801029757717)*((x-1903)**3))+((-9.393051541049447*10**2)*((x-1903)**2))+((2.627648874654535*10**4)*(x-1903))+15559
        f2 = lambda x: ((12.327801029757691)*((x-1918)**3))+((-3.845541077658476*10**2)*((x-1918)**2))+((6.418599818483467*10**3)*(x-1918))+239969
        f3 = lambda x: (-21.467707020583610)*((x-1939)**3)+(3.920973571088866*10**2)*((x-1939)**2)+(6.577008054687293*10**3)*(x-1939)+319339
        f4 = lambda x: (26.441628097571940)*((x-1948)**3)+(-1.875307324468716*10**2)*((x-1948)**2)+(8.418107676645433*10**3)*(x-1948)+394642
        f5 = lambda x: (-6.209322267287571)*((x-1960)**3)+(7.643678790657165*10**2)*((x-1960)**2)+(1.534015343607159*10**4)*(x-1960)+514346
        f6 = lambda x: (26.222742930092501)*((x-1970)**3)+(5.780952235576806*10**2)*((x-1970)**2)+(2.876475530895928*10**4)*(x-1970)+737975
        f7 = lambda x: (-82.660205931814261)*((x-1975)**3)+(9.714749755860248*10**2)*((x-1975)**2)+(3.651253027036523*10**4)*(x-1975)+899529
        f8 = lambda x: (35.738165525725492)*((x-1980)**3)+(-2.684281133911951*10**2)*((x-1980)**2)+(4.002776458133940*10**4)*(x-1980)+1096046
        f9 = lambda x: (2.578065506745601*10**2)*((x-1990)**3)+(8.037168523805697*10**2)*((x-1990)**2)+(4.538065197123315*10**4)*(x-1990)+1505219
        f10 = lambda x: (-2.471194943250273*10**2)*((x-1995)**3)+(4.670815112498964*10**3)*((x-1995)**2)+(7.275331179563086e+04)*(x-1995)+1784441
        f11 = lambda x: (-4.828035513331142*10**2)*((x-2000)**3)+(9.640226976235526*10**2)*((x-2000)**2)+(1.009275008462434*10**5)*(x-2000)+2234088
        f12 = lambda x: (2.016132489715940*10**3)*((x-2007)**3)+(-9.174851880371838*10**3)*((x-2007)**2)+(4.345169656700538*10**4)*(x-2007)+2822216
        f13 = lambda x: (-5.664906056985167*10**2)*((x-2010)**3)+(8.970340527071634*10**3)*((x-2010)**2)+(4.283816250710475*10**4)*(x-2010)+2924433
        f14 = lambda x: (-3.622351823360717*10**2)*((x-2015)**3)+(4.729814415938920*10**2)*((x-2015)**2)+(9.005477235043234*10**4)*(x-2015)+3292071
        f15 = lambda x: (-3.622351823360714*10**2)*((x-2020)**3)+(-4.960546293447180*10**3)*((x-2020)**2)+(6.761694809116586*10**4)*(x-2020)+3708890

        f1_plot = axes.plot(f1,x_range=[1903,1918], color = BLUE)
        f2_plot = axes.plot(f2,x_range=[1918,1939], color = BLUE)
        f3_plot = axes.plot(f3,x_range=[1939,1948], color = BLUE)
        f4_plot = axes.plot(f4,x_range=[1948,1960], color = BLUE)
        f5_plot = axes.plot(f5,x_range=[1960,1970], color = BLUE)
        f6_plot = axes.plot(f6,x_range=[1970,1975], color = BLUE)
        f7_plot = axes.plot(f7,x_range=[1975,1980], color = BLUE)
        f8_plot = axes.plot(f8,x_range=[1980,1990], color = BLUE)
        f9_plot = axes.plot(f9,x_range=[1990,1995], color = BLUE)
        f10_plot = axes.plot(f10,x_range=[1995,2000], color = BLUE)
        f11_plot = axes.plot(f11,x_range=[2000,2007], color = BLUE)
        f12_plot = axes.plot(f12,x_range=[2007,2010], color = BLUE)
        f13_plot = axes.plot(f13,x_range=[2010,2015], color = BLUE)
        f14_plot = axes.plot(f14,x_range=[2015,2020], color = BLUE)
        f15_plot = axes.plot(f15,x_range=[2020,2024], color = BLUE)
        interpolation_func = [f1_plot,f2_plot,f3_plot,f4_plot,f5_plot,
                              f6_plot,f7_plot,f8_plot,f9_plot,f10_plot,
                              f11_plot,f12_plot,f13_plot,f14_plot,f15_plot]
            
        create_func = []
        for func in interpolation_func:
            create_func.append(Create(func))

        self.play(create_func)
        self.wait(2)

class population_growth(Scene):
    def f1p(self, x):
        return (20819805046467927*(x - 1903)**2)/562949953421312 - (4131107755873257*x)/2199023255552 + 7919280669254711711/2199023255552
    def f2p(self, x):
        return (10409902523233941*(x - 1918)**2)/281474976710656 - (6765147407961191*x)/8796093022208 + 6516005664772636149/4398046511104
    def f3p(self, x):
        return (862231206722919*x)/1099511627776 - (9063933500474937*(x - 1939)**2)/140737488355328 - 416158703250908713/274877906944
    def f4p(self, x):
        return (22327969958867667*(x - 1948)**2)/281474976710656 - (3299075534250965*x)/8796093022208 + 1625161399728904075/2199023255552
    def f5p(self, x):
        return (6723450967449877*x)/4398046511104 - (20973226086884721*(x - 1960)**2)/1125899906842624 - 204851518560975691/68719476736
    def f6p(self, x):
        return (158905605065859*x)/137438953472 + (11071568933305959*(x - 1970)**2)/140737488355328 - 309090644113200711/137438953472
    def f7p(self, x):
        return (33379625992195*x)/17179869184 - (8725042327333293*(x - 1975)**2)/35184372088832 - 261189923363853641/68719476736
    def f8p(self, x):
        return (1886137370444091*(x - 1980)**2)/17592186044416 - (2361118655164749*x)/4398046511104 + 1212764726897613755/1099511627776
    def f9p(self, x):
        return (3534784098527853*x)/2199023255552 + (13606142408808069*(x - 1990)**2)/17592186044416 - 3467213623516787039/1099511627776
    def f10p(self, x):
        return (5135615527384477*x)/549755813888 - (26084232716207307*(x - 1995)**2)/35184372088832 - 10205556420992777143/549755813888
    def f11p(self, x):
        return (1059954165477083*x)/549755813888 - (25480709693870685*(x - 2000)**2)/17592186044416 - 129026428161422353/34359738368
    def f12p(self, x):
        return (26601133386955833*(x - 2007)**2)/4398046511104 - (5043928162795667*x)/274877906944 + 10135107734136407897/274877906944
    def f13p(self, x):
        return (4931496857312777*x)/274877906944 - (7474356095896659*(x - 2010)**2)/4398046511104 - 1237566677343925235/34359738368
    def f14p(self, x):
        return (2080194379018957*x)/2199023255552 - (9558763079233689*(x - 2015)**2)/8796093022208 - 3993559135051156403/2199023255552
    def f15p(self, x):
        return 345456657389325993/17179869184 - (597422692452105*(x - 2020)**2)/549755813888 - (681772291220789*x)/68719476736
    
    def construct(self):
        axes = Axes(
            x_range = (1903, 2024, 11), 
            y_range = (0, 100000, 10000), 
            tips = False,
            x_length=config.frame_width-4,
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
        y_lab = axes.get_y_axis_label(MathTex(r"\text{Population Growth Rate}"))
        #y_lab.color = x_lab.color = BLACK

        self.play(Write(axes), Write(x_lab), Write(y_lab))

        f1p_plot = axes.plot(self.f1p,x_range=[1903,1918],color = BLUE)
        f2p_plot = axes.plot(self.f2p,x_range=[1918,1939],color = BLUE)
        f3p_plot = axes.plot(self.f3p,x_range=[1939,1948],color = BLUE)
        f4p_plot = axes.plot(self.f4p,x_range=[1948,1960],color = BLUE)
        f5p_plot = axes.plot(self.f5p,x_range=[1960,1970],color = BLUE)
        f6p_plot = axes.plot(self.f6p,x_range=[1970,1975],color = BLUE)
        f7p_plot = axes.plot(self.f7p,x_range=[1975,1980],color = BLUE)
        f8p_plot = axes.plot(self.f8p,x_range=[1980,1990],color = BLUE)
        f9p_plot = axes.plot(self.f9p,x_range=[1990,1995],color = BLUE)
        f10p_plot = axes.plot(self.f10p,x_range=[1995,2000],color = BLUE)
        f11p_plot = axes.plot(self.f11p,x_range=[2000,2007],color = BLUE)
        f12p_plot = axes.plot(self.f12p,x_range=[2007,2010],color = BLUE)
        f13p_plot = axes.plot(self.f13p,x_range=[2010,2015],color = BLUE)
        f14p_plot = axes.plot(self.f14p,x_range=[2015,2020],color = BLUE)
        f15p_plot = axes.plot(self.f15p,x_range=[2020,2024],color = BLUE)

        first_derivative_func = [f1p_plot,f2p_plot,f3p_plot,f4p_plot,f5p_plot,
                                 f6p_plot,f7p_plot,f8p_plot,f9p_plot,f10p_plot,
                                 f11p_plot,f12p_plot,f13p_plot,f14p_plot,f15p_plot]

        for func in first_derivative_func:
            self.play(Create(func), run_time=0.5)

        self.wait(2)

        x = numpy.linspace(2000,2001)
        y = self.f11p(x)

        peak_index = np.argmax(y)

        peak_x = x[peak_index]
        peak_y = y[peak_index]
        point = axes.c2p(peak_x, peak_y)

        dot = Dot(point,color=YELLOW,z_index=2)
        title = f"\\text{{Growth rate:}} \\\\ \\text{{{peak_y:.0f} people/year at {peak_x:.2f}}}"
        label = MathTex(title,font_size=25).move_to(axes.c2p(peak_x,peak_y) + LEFT*2)

        self.add(dot)
        self.play(Create(label))
        self.wait(2)

class population_accelerate(Scene):

    def f1pp(self, x):
        return (20819805046467927*x)/281474976710656 - 40148870796180241977/281474976710656
    def f2pp(self, x):
        return (10409902523233941*x)/140737488355328 - 10037217699045038947/70368744177664
    def f3pp(self, x):
        return 17630149854651169659/70368744177664 - (9063933500474937*x)/70368744177664
    def f4pp(self, x):
        return (22327969958867667*x)/140737488355328 - 10886917672105557689/35184372088832
    def f5pp(self, x):
        return 5246015606765954677/70368744177664 - (20973226086884721*x)/562949953421312
    def f6pp(self, x):
        return (11071568933305959*x)/70368744177664 - 10864815564409509711/35184372088832
    def f7pp(self, x):
        return 17266139333499261355/17592186044416 - (8725042327333293*x)/17592186044416
    def f8pp(self, x):
        return (1886137370444091*x)/8796093022208 - 1869637115394814839/4398046511104
    def f9pp(self, x):
        return (13606142408808069*x)/8796093022208 - 13531042128566972949/4398046511104
    def f10pp(self, x):
        return 52202383965709880729/17592186044416 - (26084232716207307*x)/17592186044416
    def f11pp(self, x):
        return 796537166474828177/137438953472 - (25480709693870685*x)/8796093022208
    def f12pp(self, x):
        return (26601133386955833*x)/2199023255552 - 53428826132922722167/2199023255552
    def f13pp(self, x):
        return 7531453863805393403/1099511627776 - (7474356095896659*x)/2199023255552
    def f14pp(self, x):
        return 19265067993413921249/4398046511104 - (9558763079233689*x)/4398046511104
    def f15pp(self, x):
        return 75254171849273059/17179869184 - (597422692452105*x)/274877906944

    def construct(self):
        axes = Axes(
            x_range = (1903, 2024, 11), 
            y_range = (-20000, 20000, 5000), 
            tips = False,
            x_length=config.frame_width-4,
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
        y_lab = axes.get_y_axis_label(MathTex(r"\text{Population Growth Acceleration}"))
        #y_lab.color = x_lab.color = BLACK

        self.play(Write(axes), Write(x_lab), Write(y_lab))

        f1pp_plot = axes.plot(self.f1pp,x_range=[1903,1918],color = BLUE)
        f2pp_plot = axes.plot(self.f2pp,x_range=[1918,1939],color = BLUE)
        f3pp_plot = axes.plot(self.f3pp,x_range=[1939,1948],color = BLUE)
        f4pp_plot = axes.plot(self.f4pp,x_range=[1948,1960],color = BLUE)
        f5pp_plot = axes.plot(self.f5pp,x_range=[1960,1970],color = BLUE)
        f6pp_plot = axes.plot(self.f6pp,x_range=[1970,1975],color = BLUE)
        f7pp_plot = axes.plot(self.f7pp,x_range=[1975,1980],color = BLUE)
        f8pp_plot = axes.plot(self.f8pp,x_range=[1980,1990],color = BLUE)
        f9pp_plot = axes.plot(self.f9pp,x_range=[1990,1995],color = BLUE)
        f10pp_plot = axes.plot(self.f10pp,x_range=[1995,2000],color = BLUE)
        f11pp_plot = axes.plot(self.f11pp,x_range=[2000,2007],color = BLUE)
        f12pp_plot = axes.plot(self.f12pp,x_range=[2007,2010],color = BLUE)
        f13pp_plot = axes.plot(self.f13pp,x_range=[2010,2015],color = BLUE)
        f14pp_plot = axes.plot(self.f14pp,x_range=[2015,2020],color = BLUE)
        f15pp_plot = axes.plot(self.f15pp,x_range=[2020,2024],color = BLUE)

        second_derivative_func = [f1pp_plot,f2pp_plot,f3pp_plot,f4pp_plot,f5pp_plot,
                                  f6pp_plot,f7pp_plot,f8pp_plot,f9pp_plot,f10pp_plot,
                                  f11pp_plot,f12pp_plot,f13pp_plot,f14pp_plot,f15pp_plot]
        for func in second_derivative_func:
            self.play(Create(func), run_time=0.5)

        self.wait(2)

        x = numpy.linspace(2010,2015)
        y = self.f13pp(x)

        peak_index = np.argmax(y)

        peak_x = x[peak_index]
        peak_y = y[peak_index]

        point = axes.c2p(peak_x, peak_y)

        dot = Dot(point,color=YELLOW,z_index=2)
        title = f"\\text{{Acceleration of Growth Rate:}} \\\\ \\text{{{peak_y:.0f} people / year}}^2 \\text{{at {peak_x:.2f}}}"
        label = MathTex(title,font_size=25).move_to(axes.c2p(peak_x,peak_y) + LEFT*2)
        self.add(dot)
        self.play(Create(label))
        self.wait(2)


