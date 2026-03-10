from manim import * 
import numpy

# Typically use manim -qh main.py

class population(Scene):
    def construct(self):
        years = [1903,1918,1939,1948,1960,1970,1975,1980,1990,1995,2000,2007,2010,2015,2020,2024]
        population = [15559,239969,319339,394642,514346,737975,899529,1096046,1505219,1784441,2234088,2822216,2924433,3292071,3708890,3876806]

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

        f1 = axes.plot(lambda x: ((12.327801029757717)*((x-1903)**3))+((-9.393051541049447*10**2)*((x-1903)**2))+((2.627648874654535*10**4)*(x-1903))+15559,x_range=[1903,1918], color = BLUE)
        f2 = axes.plot(lambda x: ((12.327801029757691)*((x-1918)**3))+((-3.845541077658476*10**2)*((x-1918)**2))+((6.418599818483467*10**3)*(x-1918))+239969,x_range=[1918,1939], color = BLUE)
        f3 = axes.plot(lambda x: (-21.467707020583610)*((x-1939)**3)+(3.920973571088866*10**2)*((x-1939)**2)+(6.577008054687293*10**3)*(x-1939)+(319339),x_range=[1939,1948], color = BLUE)
        f4 = axes.plot(lambda x: (26.441628097571940)*((x-1948)**3)+(-1.875307324468716*10**2)*((x-1948)**2)+(8.418107676645433*10**3)*(x-1948)+(394642),x_range=[1948,1960], color = BLUE)
        f5 = axes.plot(lambda x: (-6.209322267287571)*((x-1960)**3)+(7.643678790657165*10**2)*((x-1960)**2)+(1.534015343607159*10**4)*(x-1960)+(514346),x_range=[1960,1970], color = BLUE)
        f6 = axes.plot(lambda x: (26.222742930092501)*((x-1970)**3)+(5.780952235576806*10**2)*((x-1970)**2)+(2.876475530895928*10**4)*(x-1970)+(737975),x_range=[1970,1975], color = BLUE)
        f7 = axes.plot(lambda x: (-82.660205931814261)*((x-1975)**3)+(9.714749755860248*10**2)*((x-1975)**2)+(3.651253027036523*10**4)*(x-1975)+(899529),x_range=[1975,1980], color = BLUE)
        f8 = axes.plot(lambda x: (35.738165525725492)*((x-1980)**3)+(-2.684281133911951*10**2)*((x-1980)**2)+(4.002776458133940*10**4)*(x-1980)+(1096046),x_range=[1980,1990], color = BLUE)
        f9 = axes.plot(lambda x: (2.578065506745601*10**2)*((x-1990)**3)+(8.037168523805697*10**2)*((x-1990)**2)+(4.538065197123315*10**4)*(x-1990)+(1505219),x_range=[1990,1995], color = BLUE)
        f10 = axes.plot(lambda x: (-2.471194943250273*10**2)*((x-1995)**3)+(4.670815112498964*10**3)*((x-1995)**2)+(7.275331179563086e+04)*(x-1995)+(1784441),x_range=[1995,2000], color = BLUE)
        f11 = axes.plot(lambda x: (-4.828035513331142*10**2)*((x-2000)**3)+(9.640226976235526*10**2)*((x-2000)**2)+(1.009275008462434*10**5)*(x-2000)+(2234088),x_range=[2000,2007], color = BLUE)
        f12 = axes.plot(lambda x: (2.016132489715940*10**3)*((x-2007)**3)+(-9.174851880371838*10**3)*((x-2007)**2)+(4.345169656700538*10**4)*(x-2007)+(2822216),x_range=[2007,2010], color = BLUE)
        f13 = axes.plot(lambda x: (-5.664906056985167*10**2)*((x-2010)**3)+(8.970340527071634*10**3)*((x-2010)**2)+(4.283816250710475*10**4)*(x-2010)+(2924433),x_range=[2010,2015], color = BLUE)
        f14 = axes.plot(lambda x: (-3.622351823360717*10**2)*((x-2015)**3)+(4.729814415938920*10**2)*((x-2015)**2)+(9.005477235043234*10**4)*(x-2015)+(3292071),x_range=[2015,2020], color = BLUE)
        f15 = axes.plot(lambda x: (-3.622351823360714*10**2)*((x-2020)**3)+(-4.960546293447180*10**3)*((x-2020)**2)+(6.761694809116586*10**4)*(x-2020)+(3708890),x_range=[2020,2024], color = BLUE)
        interpolation_func = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15]

        for i in range(len(years)):
            point = (years[i],population[i])
            dot_coord = Dot(axes.c2p(*point),color=YELLOW,z_index=2)
            self.add(dot_coord)
            self.wait(0.06)
            
        create_func = []
        for func in interpolation_func:
            create_func.append(Create(func))

        self.play(create_func)
        self.wait(2)

class population_growth(Scene):
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

        f1p = axes.plot(lambda x: (20819805046467927*(x - 1903)**2)/562949953421312 - (4131107755873257*x)/2199023255552 + 7919280669254711711/2199023255552,x_range=[1903,1918],color = BLUE)
        f2p = axes.plot(lambda x: (10409902523233941*(x - 1918)**2)/281474976710656 - (6765147407961191*x)/8796093022208 + 6516005664772636149/4398046511104,x_range=[1918,1939],color = BLUE)
        f3p = axes.plot(lambda x: (862231206722919*x)/1099511627776 - (9063933500474937*(x - 1939)**2)/140737488355328 - 416158703250908713/274877906944,x_range=[1939,1948],color = BLUE)
        f4p = axes.plot(lambda x: (22327969958867667*(x - 1948)**2)/281474976710656 - (3299075534250965*x)/8796093022208 + 1625161399728904075/2199023255552,x_range=[1948,1960],color = BLUE)
        f5p = axes.plot(lambda x: (6723450967449877*x)/4398046511104 - (20973226086884721*(x - 1960)**2)/1125899906842624 - 204851518560975691/68719476736,x_range=[1960,1970],color = BLUE)
        f6p = axes.plot(lambda x: (158905605065859*x)/137438953472 + (11071568933305959*(x - 1970)**2)/140737488355328 - 309090644113200711/137438953472,x_range=[1970,1975],color = BLUE)
        f7p = axes.plot(lambda x: (33379625992195*x)/17179869184 - (8725042327333293*(x - 1975)**2)/35184372088832 - 261189923363853641/68719476736,x_range=[1975,1980],color = BLUE)
        f8p = axes.plot(lambda x: (1886137370444091*(x - 1980)**2)/17592186044416 - (2361118655164749*x)/4398046511104 + 1212764726897613755/1099511627776,x_range=[1980,1990],color = BLUE)
        f9p = axes.plot(lambda x: (3534784098527853*x)/2199023255552 + (13606142408808069*(x - 1990)**2)/17592186044416 - 3467213623516787039/1099511627776,x_range=[1990,1995],color = BLUE)
        f10p = axes.plot(lambda x: (5135615527384477*x)/549755813888 - (26084232716207307*(x - 1995)**2)/35184372088832 - 10205556420992777143/549755813888,x_range=[1995,2000],color = BLUE)
        f11p = axes.plot(lambda x: (1059954165477083*x)/549755813888 - (25480709693870685*(x - 2000)**2)/17592186044416 - 129026428161422353/34359738368,x_range=[2000,2007],color = BLUE)
        f12p = axes.plot(lambda x: (26601133386955833*(x - 2007)**2)/4398046511104 - (5043928162795667*x)/274877906944 + 10135107734136407897/274877906944,x_range=[2007,2010],color = BLUE)
        f13p = axes.plot(lambda x: (4931496857312777*x)/274877906944 - (7474356095896659*(x - 2010)**2)/4398046511104 - 1237566677343925235/34359738368,x_range=[2010,2015],color = BLUE)
        f14p = axes.plot(lambda x: (2080194379018957*x)/2199023255552 - (9558763079233689*(x - 2015)**2)/8796093022208 - 3993559135051156403/2199023255552,x_range=[2015,2020],color = BLUE)
        f15p = axes.plot(lambda x: 345456657389325993/17179869184 - (597422692452105*(x - 2020)**2)/549755813888 - (681772291220789*x)/68719476736,x_range=[2020,2024],color = BLUE)

        first_derivative_func = [f1p,f2p,f3p,f4p,f5p,f6p,f7p,f8p,f9p,f10p,f11p,f12p,f13p,f14p,f15p]
        for func in first_derivative_func:
            self.play(Create(func), run_time=0.5)

        self.wait(2)

        f11 = lambda x: (1059954165477083*x)/549755813888 - (25480709693870685*(x - 2000)**2)/17592186044416 - 129026428161422353/34359738368
        x = numpy.linspace(2000,2001)
        y = f11(x)

        peak_index = np.argmax(y)

        peak_x = x[peak_index]
        peak_y = y[peak_index]
        point = axes.c2p(peak_x, peak_y)

        dot = Dot(point,color=YELLOW,z_index=2)
        label = MathTex(f"\\text{{Growth rate:}} \\\\ \\text{{{peak_y:.0f} people/year at {peak_x:.2f}}}",font_size=25).move_to(axes.c2p(peak_x,peak_y) + LEFT*2)
        self.add(dot)
        self.play(Create(label))
        self.wait(2)

class population_accelerate(Scene):
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

        f1pp = axes.plot(lambda x: (20819805046467927*x)/281474976710656 - 40148870796180241977/281474976710656,x_range=[1903,1918],color = BLUE)
        f2pp = axes.plot(lambda x: (10409902523233941*x)/140737488355328 - 10037217699045038947/70368744177664,x_range=[1918,1939],color = BLUE)
        f3pp = axes.plot(lambda x: 17630149854651169659/70368744177664 - (9063933500474937*x)/70368744177664,x_range=[1939,1948],color = BLUE)
        f4pp = axes.plot(lambda x: (22327969958867667*x)/140737488355328 - 10886917672105557689/35184372088832,x_range=[1948,1960],color = BLUE)
        f5pp = axes.plot(lambda x: 5246015606765954677/70368744177664 - (20973226086884721*x)/562949953421312,x_range=[1960,1970],color = BLUE)
        f6pp = axes.plot(lambda x: (11071568933305959*x)/70368744177664 - 10864815564409509711/35184372088832,x_range=[1970,1975],color = BLUE)
        f7pp = axes.plot(lambda x: 17266139333499261355/17592186044416 - (8725042327333293*x)/17592186044416,x_range=[1975,1980],color = BLUE)
        f8pp = axes.plot(lambda x: (1886137370444091*x)/8796093022208 - 1869637115394814839/4398046511104,x_range=[1980,1990],color = BLUE)
        f9pp = axes.plot(lambda x: (13606142408808069*x)/8796093022208 - 13531042128566972949/4398046511104,x_range=[1990,1995],color = BLUE)
        f10pp = axes.plot(lambda x: 52202383965709880729/17592186044416 - (26084232716207307*x)/17592186044416,x_range=[1995,2000],color = BLUE)
        f11pp = axes.plot(lambda x: 796537166474828177/137438953472 - (25480709693870685*x)/8796093022208,x_range=[2000,2007],color = BLUE)
        f12pp = axes.plot(lambda x: (26601133386955833*x)/2199023255552 - 53428826132922722167/2199023255552,x_range=[2007,2010],color = BLUE)
        f13pp = axes.plot(lambda x: 7531453863805393403/1099511627776 - (7474356095896659*x)/2199023255552,x_range=[2010,2015],color = BLUE)
        f14pp = axes.plot(lambda x: 19265067993413921249/4398046511104 - (9558763079233689*x)/4398046511104,x_range=[2015,2020],color = BLUE)
        f15pp = axes.plot(lambda x: 75254171849273059/17179869184 - (597422692452105*x)/274877906944,x_range=[2020,2024],color = BLUE)

        second_derivative_func = [f1pp,f2pp,f3pp,f4pp,f5pp,f6pp,f7pp,f8pp,f9pp,f10pp,f11pp,f12pp,f13pp,f14pp,f15pp]
        for func in second_derivative_func:
            self.play(Create(func), run_time=0.5)

        self.wait(2)

        f13 = lambda x: 7531453863805393403/1099511627776 - (7474356095896659*x)/2199023255552
        x = numpy.linspace(2010,2015)
        y = f13(x)

        peak_index = np.argmax(y)

        peak_x = x[peak_index]
        peak_y = y[peak_index]

        point = axes.c2p(peak_x, peak_y)

        dot = Dot(point,color=YELLOW,z_index=2)
        label = MathTex(f"\\text{{Acceleration of Growth Rate:}} \\\\ \\text{{{peak_y:.0f} people / year}}^2 \\text{{at {peak_x:.2f}}}",font_size=25).move_to(axes.c2p(peak_x,peak_y) + LEFT*2)
        self.add(dot)
        self.play(Create(label))
        self.wait(2)