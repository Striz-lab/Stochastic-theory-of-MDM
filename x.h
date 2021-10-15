boundary    p p p

variable        ave_time    equal 10.0
variable        step        equal 0.0005
variable        nsnapshots  equal 1000
variable        Temp        equal 0.44

variable        nsteps      equal ${ave_time}/${step}
variable        frequency   equal ${nsteps}/${nsnapshots}
variable        F_thermo    equal ${frequency}*10

#если шаг -- 0.01 то 10000 снапшотов, 10000 шагов

units           lj # define units for model
atom_style      atomic # model without bonds

region          box block 0 10 0 10 0 10 # create box by multiplying by 10x10x10 initial unit cell
create_box      1 box # create box

read_dump start/start.dump 10000 x y z vx vy vz add yes
mass            1 1.0

pair_style      lj/cut 2.5 # force field parameters
pair_coeff      1 1 1.0 1.0 2.5 # force field parameters

reset_timestep  0

fix             nvt all nvt temp ${Temp} ${Temp} ${Temp}

dump dump_1 all custom ${frequency} ${step}.txt id type fx fy fz
dump_modify dump_1 sort id

thermo          ${F_thermo}
run             ${nsteps}

unfix           nvt

