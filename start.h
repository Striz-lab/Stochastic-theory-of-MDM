#-------------DETAILS OF SIMULATION------------------------------------------#
boundary    p p p

variable        i loop 1
variable        lj_density equal 0.5
variable        lj_temp equal 0.44

units           lj # define units for model
atom_style      atomic # model without bonds

lattice         fcc ${lj_density} # number density for fcc crystall
region          box block 0 10 0 10 0 10 # create box by multiplying by 10x10x10 initial unit cell
create_box      1 box # create box
create_atoms    1 box # create atoms
mass            1 1.0

pair_style      lj/cut 2.5 # force field parameters
pair_coeff      1 1 1.0 1.0 2.5 # force field parameters

neighbor        0.3 bin
neigh_modify    every 20 delay 0 check no

#------------MELTING----------------------------------------------------------#



velocity        all create 3.0 87287 # create initial velocities to melt the structure
fix             nvt all nvt temp ${lj_temp} ${lj_temp} ${lj_temp}

dump            id all atom 100 dump

timestep        0.01 # MD simulation timestep
run_style       verlet

thermo          1000 # output to log each 1000 steps

dump dump_1 all custom 10000 start/start.dump id type x y z vx vy vz

dump_modify dump_1 sort id

run             10000

unfix           nvt
