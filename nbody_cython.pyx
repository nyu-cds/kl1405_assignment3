"""
    Assignment 7 Cython
    Author: Kaiwen Liu
    Date: 03/25/2017
    
    N-body simulation.

    final optimized 

    original time: 90.0s
    optimized time: 43.5s
    relative speedup (R): 90.0/43.5 = 2.0689

"""
import itertools
import timeit
import cython



cdef double PI = 3.14159265358979323
cdef double SOLAR_MASS = 4 * PI * PI
cdef double DAYS_PER_YEAR = 365.24

cdef list body_combinations = list(itertools.combinations(BODIES, 2))

cdef dict BODIES = {
    'sun': ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS),

    'jupiter': ([4.84143144246472090e+00,
                 -1.16032004402742839e+00,
                 -1.03622044471123109e-01],
                [1.66007664274403694e-03 * DAYS_PER_YEAR,
                 7.69901118419740425e-03 * DAYS_PER_YEAR,
                 -6.90460016972063023e-05 * DAYS_PER_YEAR],
                9.54791938424326609e-04 * SOLAR_MASS),

    'saturn': ([8.34336671824457987e+00,
                4.12479856412430479e+00,
                -4.03523417114321381e-01],
               [-2.76742510726862411e-03 * DAYS_PER_YEAR,
                4.99852801234917238e-03 * DAYS_PER_YEAR,
                2.30417297573763929e-05 * DAYS_PER_YEAR],
               2.85885980666130812e-04 * SOLAR_MASS),

    'uranus': ([1.28943695621391310e+01,
                -1.51111514016986312e+01,
                -2.23307578892655734e-01],
               [2.96460137564761618e-03 * DAYS_PER_YEAR,
                2.37847173959480950e-03 * DAYS_PER_YEAR,
                -2.96589568540237556e-05 * DAYS_PER_YEAR],
               4.36624404335156298e-05 * SOLAR_MASS),

    'neptune': ([1.53796971148509165e+01,
                 -2.59193146099879641e+01,
                 1.79258772950371181e-01],
                [2.68067772490389322e-03 * DAYS_PER_YEAR,
                 1.62824170038242295e-03 * DAYS_PER_YEAR,
                 -9.51592254519715870e-05 * DAYS_PER_YEAR],
                5.15138902046611451e-05 * SOLAR_MASS)}



cdef advance(double dt, list body_combinations):
    '''
        advance the system one timestep
    '''

    BODIES_local = BODIES
    cdef list bodykeys = BODIES_local.keys()
    
    # seenit is a uesless list when we use itertools combinations, in nbody_2 I used a set instead of a list.
    cdef list v1, v2, r
    cdef double x1, x2, y1, y2, z1, z2,m1, m2, dx, dy, dz, vx, vy, vz, m


    for (body1, body2) in body_combinations:
        ([x1, y1, z1], v1, m1) = BODIES_local[body1]
        ([x2, y2, z2], v2, m2) = BODIES_local[body2]
        (dx, dy, dz) = (x1-x2, y1-y2, z1-z2)
        # reduce function overhead
        v1[0] -= dx * m2 * dt *((dx * dx + dy * dy + dz * dz) ** (-1.5))
        v1[1] -= dy *  m2 * dt *((dx * dx + dy * dy + dz * dz) ** (-1.5))
        v1[2] -= dz *  m2 * dt *((dx * dx + dy * dy + dz * dz) ** (-1.5))
        v2[0] += dx *  m1 * dt *((dx * dx + dy * dy + dz * dz) ** (-1.5))
        v2[1] += dy *  m1 * dt *((dx * dx + dy * dy + dz * dz) ** (-1.5))
        v2[2] += dz *  m1 * dt *((dx * dx + dy * dy + dz * dz) ** (-1.5))

        
    for body in bodykeys:
        (r, [vx, vy, vz], m) = BODIES_local[body]
        # reduce function overhead
        r[0] += dt * vx
        r[1] += dt * vy
        r[2] += dt * vz


    
cdef double report_energy(list body_combinations, double e=0.0):
    '''
        compute the energy and return it so that it can be printed
    '''
    BODIES_local = BODIES
    cdef list bodykeys = BODIES_local.keys()
    
    for (body1, body2) in body_combinations:
        ((x1, y1, z1), v1, m1) = BODIES_local[body1]
        ((x2, y2, z2), v2, m2) = BODIES_local[body2]
        # reduce function overhead
        (dx, dy, dz) = (x1-x2, y1-y2, z1-z2)
        e -= (m1 * m2) / ((dx * dx + dy * dy + dz * dz) ** 0.5)
        
    for body in bodykeys:
        (r, [vx, vy, vz], m) = BODIES_local[body]
        e += m * (vx * vx + vy * vy + vz * vz) / 2.
        
    return e

cdef offset_momentum(tuple ref, double px=0.0, double py=0.0, double pz=0.0):
    '''
        ref is the body in the center of the system
        offset values from this reference
    '''
    BODIES_local = BODIES
    cdef list bodykeys = BODIES_local.keys()
    for body in bodykeys:
        (r, [vx, vy, vz], m) = BODIES_local[body]
        px -= vx * m
        py -= vy * m
        pz -= vz * m
        
    (r, v, m) = ref
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m


def nbody(loops, reference, iterations, body_combinations):
    '''
        nbody simulation
        loops - number of loops to run
        reference - body at center of system
        iterations - number of timesteps to advance
    '''
    # Set up global state
    offset_momentum(BODIES[reference])

    for _ in range(loops):
        for _ in range(iterations):
            advance(0.01, body_combinations)
        print(report_energy(body_combinations))


if __name__ == '__main__':
    body_combinations = list(itertools.combinations(BODIES, 2))
    nbody(100, 'sun', 20000, body_combinations)

 

