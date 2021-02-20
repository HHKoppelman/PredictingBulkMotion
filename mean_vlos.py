# The only input parameters are: (x,y,z) and distance; both w.r.t. the Sun.


vlsr = 229   # Eilers+2019
U=11.1       # Schoenrich+2010
V=12.24      # Schoenrich+2010
W=7.25       # Schoenrich+2010
Rsun = 8.122 # GravityCollaboration+2018

vx_sun = U
vy_sun = V+vlsr
vz_sun = W

# These are mean values taken from Gaia EDR3
mean_vR, mean_vphi, mean_vz = 0.45504686703112296, 210.83976551386272, -0.6101459530135516

# Galactocentric
df['phi'] = (df.y/(df.x-Rsun)).arctan() # x, y are wrt the Sun
df['vx_gc_bulk'] = mean_vR * (df.phi).cos() - mean_vphi * (df.phi).sin()
df['vy_gc_bulk'] = mean_vR * (df.phi).sin() + mean_vphi * (df.phi).cos()
df['vz_gc_bulk'] = mean_vz * (df['l/l'].values) # l/l is just to create an array of ones


# Heliocentric
df['vx_hc_bulk'] = df.vx_gc_bulk - vx_sun
df['vy_hc_bulk'] = df.vy_gc_bulk - vy_sun
df['vz_hc_bulk'] = df.vz_gc_bulk - vz_sun


# x, y, z and distance are wrt the Sun
df['mean_vlos_bulk'] = (df.x*df.vx_hc_bulk+df.y*df.vy_hc_bulk+df.z*df.vz_hc_bulk)/df.distance