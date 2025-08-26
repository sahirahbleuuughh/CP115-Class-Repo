'''
A ball is thrown upward from a building at t = 2 seconds. Calculate the ball's position, 
velocity, and kinetic energy. The ball's motion follows these physics formulas:

    Position = initial_height + initial_velocity × time - 0.5 × gravity × time²
    Velocity = initial_velocity - gravity × time
    Kinetic Energy = 0.5 × mass × velocity²

Display a formatted report showing:

    Initial conditions (height, velocity, mass)
    Time-based calculations (position, velocity at t=2s)
    Energy analysis (kinetic energy at t=2s)
    Motion status (moving up/down based on velocity sign)

Use proper variable naming with snake_case, add detailed comments for each calculation step, 
and format all outputs with appropriate units and decimal precision.
'''

import physics_constants

time = 2

position = (physics_constants.building_height + physics_constants.initial_velocity) * (time - 0.5) * physics_constants.standard_gravity * (time**2)
velocity = (physics_constants.initial_velocity - physics_constants.standard_gravity) * time
kinetic_energy = 0.5 * physics_constants.ball_mass * (physics_constants.initial_velocity**2)

print(f"INITIAL CONDITION\nheight: {physics_constants.building_height}\nvelocity: {physics_constants.initial_velocity}\nmass: {physics_constants.ball_mass}\n")
print(f"TIME-BASED CALCULATIONS\nposition: {position}\nvelocity: {velocity}")
print(f"ENERGY ANALYSIS\nkinetic: {kinetic_energy}")
# Motion status (moving up/down based on velocity sign)
# will continue later 