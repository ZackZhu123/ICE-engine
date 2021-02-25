
### Fundamentals of reciprocating engines (for back- ground information only)
The applications of reciprocating internal-combustion (IC) engines are more numer- ous than those of other types of power plant. They include road and off-road vehicles, railway locomotives, ships and smaller marine craft, light aircraft, horticultural ma- chinery, on-site electricity generation (where possible with exhaust energy recovery for space heating, as in the Imperial College combined-heat-and-power (CHP) plant installed in 1999). The output power ranges from below 1 kW (e.g. small lawn-mower engines) to more than 20 MW (large ship and stationary engines).
One complete cycle of operation of a 4-stroke IC engine consists of the following events:

#### 1. Intake or induction stroke the piston moves from top (or inner) dead centre position (TDC) to bottom (or outer) dead centre position (BDC). This draws into the cylinder, through the open inlet valve:
  - air only in the case of CI engines, which use diesel oil fuel (increasingly, in the future, mixed with renewable liquid ’biofuels’ having similar properties)
  - a mixture of air and fuel in the case of conventional SI engines, which use either liquid fuel evaporated before entering the cylinder (normally petrol, also known as gasoline) or compressed gaseous fuel (normally natural gas, as in the College CHP plant)

(In newly-developed gasoline direct injection (GDI) SI engines, petrol is sprayed directly into the cylinder, during the intake or compression stroke depending on the operating condition)

#### 2. Compression stroke piston moves from BDC to TDC, compressing the gas; work input to the gas At or near TDC (depending on the fuel injection or spark timing), combustion is initiated:
  - in CI engines by auto-ignition of a pulsed spray of fuel, as a result of the temperature rise achieved by work input during the compression stroke;
  - in SI engines by a spark

#### 3. Expansion or power stroke piston moves from TDC to BDC, with combustion during the early part of the stroke; work output from the gas
#### 4. Exhaust stroke piston moves from BDC to TDC, expelling the gas (combustion products plus nitrogen and any excess air) through the open exhaust valve

Elementary analyses of engine performance have been made in ME1 and ME2 Ther- modynamics, as part of the lectures or tutorial problems (ME1 Sections 3 "Energy, Heat, Work & 1st Law" and 4 "Properties of Substances" and in ME2 Sections 3 "Power Cycles and Power Plants" and 4 "Gas and Gas-Vapour Mixtures"). These analyses were based on modelling these in-cylinder events as a cycle of ideal processes undergone by a system comprising air only. Compression and expansion were modelled as adia- batic processes with process path equation Pvγ=constant. Combustion was modelled as heat addition from an external source, in a constant-pressure process in the case of a CI engine or a constant-volume process in the case of an SI engine. Exhaust and intake strokes were replaced in the model by a constant-volume process with heat transfer from the gas to the surroundings; this simulates the change from a cylinder full of hot gas to a cylinder full of cold gas while keeping the same gas, as required by the definition of a thermodynamic system. These ideal cycles – the Diesel cycle for CI engines and the Otto cycle for SI engines – will be covered in more detail in the ME2 TF Thermodynamics lectures. However, they give poor estimates of engine efficiency and net power. (Net power can be calculated as net specific work for the cycle multiplied by the number of thermodynamic cycles in unit time, i.e. half the number of shaft revolutions in unit time because the models ignore the exhaust and intake strokes). The P–V diagram for the processes in a real 4-stroke engine (see Q.5 on ME1 Thermodynamics Exercise Sheet 3, Figure 3.13 (page 40) of the ME2 Thermo- dynamics course notes and Figure 1 of this document) differs from that of the ideal cycle in having rounded corners and a region of negative work (an anti-clockwise loop) required to overcome the pressure drop through the valves during the exhaust and intake strokes. The compression and expansion strokes are non-adiabatic (there is considerable heat loss to the surroundings), and other non-ideal effects include gas friction and the combustion process. In addition, there are losses in overcoming friction in the engine’s mechanical parts – between piston rings and cylinder wall, in shaft bearings etc. All these factors contribute to lower power and efficiency than predicted.

Note that the efficiency of a real engine has to be defined as its net power divided by the internal energy released in unit time by conversion of the fuel’s chemical energy, not by a heat input; internal combustion means there is no actual heat transfer from the surroundings to the working fluid. In practice, not all of a hydrocarbon fuel is completely burned to carbon dioxide and water vapour (there are always some hy- drocarbon compounds and carbon monoxide in the exhaust gas), so this represents yet another loss.

You may recall a figure of about 57% for the efficiency of the Diesel cycle from a problem sheet exercise, and would have got a similar value for the Otto cycle for a similar analysis. For real engines, only very large, low-speed diesels get anywhere near 50% in thermal efficiency, while a typical automotive petrol engine rarely does better than 30%. A very approximate but easily remembered rule-of-thumb for the latter type of engine is that, at its most efficient operating condition, one third of the fuel’s chemical energy is transformed to shaft work, one third is transferred to the surroundings as a heat loss directly and via the cooling system, and the remaining one third appears as energy in the exhaust gas.

Another framework for analysing the performance of a real engine is the control vol- ume. Instead of concentrating on the in-cylinder processes, as in the system ap- proach outlined above, we can ’stand back’ and look at the entire engine as a three- port control volume, with two inflows (air and fuel) and one outflow (exhaust gas). They are essentially unsteady flows, but averaged over many cycles of operation the SFEE would be applicable, particularly for a multi-cylinder engine where the sequence of piston strokes in each cylinder is out of phase with that in the other cylinders, for balancing reasons. There is a shaft work output from the control volume, and the only heat transfer is the heat loss to the surroundings. We did not use this approach in ME1, since the SFEE with allowance for combustion is covered in ME2.

### Performance parameters for real IC engines

#### 1 Powers, efficiency and specific fuel consumption

The net shaft power Wnet is called the brake power, Wb when it is obtained as Tω
from measurements of angular speed ω using a tachometer and torque T using a dynamometer. A dynamometer (a brake, in old fashioned terminology) is any piece of apparatus which provides a load for the engine to work against while on a test bed, such that the load is set by applying a known force F at a known radial distance r from the axis of rotation. The applied torque is equal to Fr, and as long as the engine runs at a steady speed, its torque T is equal to the torque applied by the dynamometer. Dynamometers are usually of the hydraulic type (sometimes referred to as a water brake), or are based on an electrical machine, as in this experiment.

Wnet is called indicated power, W, when it is obtained from the enclosed area of a
measured P–V, or indicator, diagram. Indicator diagrams or, more commonly, pres- sure vs crank angle diagrams, would normally be recorded on an oscilloscope or a digital data acquisition system, using a fast-response in-cylinder pressure transducer and a suitable sensor on the crankshaft to trigger the time base. The engines in this experiment are not equipped for obtaining indicator diagrams. Very-low-speed (less than 500 rev/min) engines allow the use of a purely-mechanical indicator mechanism. Indicated power is greater than brake power since it represents the net rate of work transfer from the gas to the piston, before accounting for mechanical losses. The difference between them, W − Wb , is known as the friction power, the power absorbed by friction in the engine’s mechanism (between piston rings and cylinder wall, in the shaft bearings etc.). Friction power is mainly dependent on engine speed and can be measured approximately by motoring the engine, i.e. measuring the power used by an electric dynamometer operating as a motor to turn the engine with its fuel supply cut off. Measurements of brake and friction power allow the indicated power to be estimated in the absence of the equipment needed for an indicator diagram; how- ever, since hydraulic dynamometers are used in this experiment, the engines cannot be motored.

The thermal efficiency ηth of a real IC engine, often called fuel conversion efficiency, can be defined by

![](https://raw.githubusercontent.com/zackzhu123/ICE-engine/master/docs/1.png)

where CVƒ is the calorific value (or heating value) of the fuel. CVƒ is essentially the energy in chemical bonds which is transformed to internal energy during combus- tion of unit mass of fuel (under certain conditions which will be explained in ME2 TF Thermodynamics). When Wb is used as Wnet, the corresponding efficiency is called

brake thermal efficiency. The ratio of brake to indicated power is the mechanical effi- ciency; like friction power, it is not a thermodynamic quantity but reflects the engine mechanical design and the quality of lubrication.
Instead of thermal efficiency, automotive engineers prefer to use the quantity specific fuel consumption, sfc, defined as fuel mass flow rate divided by net shaft power. This a practical inverse measure of engine efficiency, with the fuel calorific value omitted since a given type of engine will normally be restricted to one type of fuel. Use of brake power in the denominator gives brake specific fuel consumption, bsfc:

![](https://raw.githubusercontent.com/zackzhu123/ICE-engine/master/docs/2.png)

̇Rather than the SI unit of kg/s per kW, or kg/kJ, it is usual to express bsfc in g/kWh. Typical best values of bsfc for automotive (high speed) engines are around 270 g/kWh for SI and 200 g/kWh for CI. With a typical liquid fuel CVƒ of 44000 kJ/kg, the corre- sponding values of ηth are approximately 30% and 40% respectively. The best bsfc for large low-speed marine and stationary engines is typically 200 g/kWh for SI and 180 g/kWh for CI. Do not expect the engines in this experiment, under the selected operating conditions, to perform as well as this!

#### 2 Mean effective pressure
Another very common measure of engine performance is mean effective pressure, mep. This is defined as the net work per cycle per unit of displaced (or swept) volume so that it is independent of the size and number of cylinders and of engine speed. It is therefore representative of engine type and design rather than size. It has little to do with the peak pressure in the cylinders and is called a pressure only because it has the units of pressure (work divided by volume). mep is a fictitious pressure which, when multiplied by the displaced volume Vd of the cylinder(s), gives the same net work per cycle as the actual engine. In general1,
 ̇
  > mep = Wnetper cycle/Vd

Using brake work, obtained from a dynamometer, the mep is known as the brake mean effective pressure, bmep. Now ’per cycle’ means ’per two crankshaft revo- lutions’ for a 4-stroke engine, so for an engine speed N expressed in rev/min, the number of cycles per second is N / (2 x 60). Thus

![](https://raw.githubusercontent.com/zackzhu123/ICE-engine/master/docs/3.png)

For an engine of given cylinder capacity (the total displaced volume of all the cylinders), a larger bmep means higher power output at a given speed.

Use of indicated instead of brake work would give the indicated mean effective pres- sure, imep. As sketched in Figure 1, this may be visualised on an engine indicator diagram as the height of a rectangle whose enclosed area is the same as that of the actual pressure vs volume trace.

(The rectangle must have the same horizontal dimension as the indicator diagram, i.e. Vd per cylinder, but its vertical position on the diagram is arbitrary.)

For a given 4-stroke engine, brake mean effective pressure is proportional to torque,
since

![](https://raw.githubusercontent.com/zackzhu123/ICE-engine/master/docs/4.png)

![](https://raw.githubusercontent.com/zackzhu123/ICE-engine/master/docs/5.png)

where N and ω are the rotational speed in rev/min and rad/s respectively. Hence

> bmep = (4π/Vd)T.

An SI engine will normally have a higher bmep than a similar size of CI engine since it needs a near stoichiometric2 air-to-fuel mass ratio (AFR), around 14–15 for liquid fuels, whereas CI engine AFR is greater (lean, or weak, burning, with excess air). The SI engine therefore burns more fuel per cycle.

#### 3 Volumetric efficiency
The air or air-fuel vapour mixture entering the cylinders of a naturally-aspirated (i.e. not turbocharged) engine is at a lower density than the ambient air, because of fric- tional pressure loss in the intake and inlet valves and because of heating (the inlet manifold is hot). The mass of air induced is therefore less than ρmbVd, where ρmb is the ambient air density. Hence the engine’s power output is less than might be expected. A measure of this effect is the volumetric efficiency ηo . It represents the ’breathing capacity’ of an engine and is defined for 4-stroke engines as:

![](https://raw.githubusercontent.com/zackzhu123/ICE-engine/master/docs/6.png)

Another reminder: "per cycle" means "per two crankshaft revolutions" for 4-stroke engines. For example, at a speed of 2400 rev/min, the no. of cycles in unit time is 12 x 2400/60 = 20 per s. For multi-cylinder engines, it makes no difference whether the volumes or masses refer to one of the cylinders or to all of them. Since frictional pressure loss increases with flow rate, ηvol decreases as engine speed rises, but typical maximum values are 80–90% for SI engines and up to 95% for CI engines. The additional pressure drop due to a partly-closed throttle in an SI engine will lead to a volumetric efficiency much lower than these figures. Newer engines with four valves per cylinder will have higher ηvol than those in the experiment, with two valves per cylinder, because the air flow rate and hence the pressure loss in each valve is lower.