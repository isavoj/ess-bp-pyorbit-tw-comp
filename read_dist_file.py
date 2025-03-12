from numpy import fromfile, dtype

Header_Type = dtype([('dummy1', 'int8'),
                     ('dummy2', 'int8'),
                     ('Np','int32'),
                     ('Ib', 'float64'),
                     ('freq', 'float64'),
                     ('dummy3','int8')])

Particle_Type = dtype([('x','float64'),
                       ('xp','float64'),
                       ('y','float64'),
                       ('yp','float64'),
                       ('phi','float64'),
                       ('E','float64')])

Footer_Type = dtype([('mass','float64')])

with open('dist-rfq_6mA_eps-025_iris-8p5.dst','r') as f:
    Header = fromfile(f, dtype=Header_Type, count=1)
    Particles = fromfile(f, dtype=Particle_Type, count=int(Header['Np']))
    Footer = fromfile(f, dtype=Footer_Type, count=1)
    print(Particles)

