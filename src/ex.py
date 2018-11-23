

foo = [3,1,2]
bar = sort(foo)
print(foo)
# [1,2,3]

# Make a sequence from 0 to 10^18
gen1 = range(1, 1000000000000000000)
# Square them all
gen2 = (i ** 2 for i in gen1)
# Include only odd numbers
gen3 = (i for i in gen2 if i % 2 == 0)
# Enumerate them all
gen4 = enumerate(gen3)

for i, value in gen4:
    print(i, value)
    if value > 120:
        break
# 0 4
# 1 16
# 2 36
# 3 64
# 4 100
# 5 144



runs_data_number = {
    'M29-768': 345
    'M35-1536': 138
    ...
}

print(runs_data_number['M35-1536'])  # 138

for run in dataset:
    run_number = runs_data_number[run]
    file = open(run + '/' + data_number, 'r')
    ...

def 

def plot_my_data(data):
    plot(data)
    xlabel("")




data1    = read_in_data(...)
data2    = read_in_data(...)
merged   = match_data(data1, data2)
reduced  = analyze_data(merged)
plot_data(reduced)

    dim_len = r_cube.shape[0]
    rho_length = dim_len*2
    
    output_cube = ones((rho_length, 180, 360),dtype=float)*np.nan
    
    # Can't go outside of closest edge of cube (don't go all the way into the corners).
    max_r_overall = min([
        r_cube[dim_len//2,dim_len//2,0],
        r_cube[0,dim_len//2,dim_len//2],
        r_cube[dim_len//2,0,dim_len//2],
    ])
    if max_r > max_r_overall:
        max_r = max_r_overall
    
    # Mask off data outside the radius range.
    index_mask = logical_and(
        min_r < radius_cube, 
        radius_cube < max_r
    )
    rho = radius_cube[index_mask]
    x = x_cube[index_mask]
    y = y_cube[index_mask]
    z = z_cube[index_mask]
    # Perform conversion to spherical coordinates
    theta = arctan2(sqrt(x**2 + y**2),z) * 180/np.pi
    phi = arctan2(y,x) * 180/np.pi + 180
    # Map value from input cube to new coordinates in output cube.
    # This one assignment statement does the full shuffling
    output_cube[
        np.array(rho/max_r_overall*rho_length, dtype=int),
        np.array(theta, dtype=int),
        np.array(phi, dtype=int)
    ] = data_cube[index_mask]
    
    radius_arr = np.linspace(0, max_r_overall, rho_length)
    return output_cube, radius_arr



def show_masked_slice(data_slice, radius_slice, radius_start, radius_stop):
    """
    Use show_slice and mask_shell to show an image focussed on a shell.
    
    INPUT:
    data_slice
    radius_slice
    radius_start
    radius_stop
    """
    masked = mask_shell(data_slice, radius_slice, radius_start, radius_stop)
    show_slice(masked)



my_particle = {
    'x': 12.0,
    'y': 13.5,
    'z': -12.0,
}

def print_particle(particle_dict):
    print("x: ", particle_dict['x'])
    print("y: ", particle_dict['y'])
    print("z: ", particle_dict['z'])