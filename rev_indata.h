#-------------DETAILS OF SIMULATION------------------------------------------#
boundary    p p p

variable        ave_time    equal 10.0
variable        step        equal 0.005
variable        nsnapshots  equal 1000
variable        Temp        equal 0.44

variable        nsteps      equal ${ave_time}/${step}
variable        frequency   equal ${nsteps}/${nsnapshots}
variable        F_thermo    equal ${frequency}*10

variable        i loop 1
variable        lj_density equal 0.7
variable        lj_temp equal 2.0

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

timestep        ${step} # MD simulation timestep
run_style       verlet

thermo          ${F_thermo} # output to log each 1000 steps

dump dump_2 all custom ${frequency} rev_indata/${step}.txt id type xu yu zu vx vy vz
dump_modify dump_2 sort id

run             ${nsteps}

unfix           nvt

variable vxa atom -vx
variable vya atom -vy
variable vza atom -vz

velocity all set v_vxa v_vya v_vza

fix             nvt all nvt temp ${lj_temp} ${lj_temp} ${lj_temp}

#dump            id all atom 100 dump

timestep        ${step} # MD simulation timestep
run_style       verlet

thermo          ${F_thermo} # output to log each 1000 steps

run             ${nsteps}

unfix           nvt
