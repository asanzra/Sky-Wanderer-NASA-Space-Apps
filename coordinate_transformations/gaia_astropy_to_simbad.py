from astropy.coordinates import SkyCoord
from astropy import units as u
from gaia_query import *

def transf_astropy_to_simbad():
    table = get_table()
    # Crear una columna de coordenadas en formato adecuado
    coords = SkyCoord(ra=table['ra'], dec=table['dec'], unit=(u.deg, u.deg))
    table['RA_hms'] = coords.ra.to_string(unit=u.hour, sep=':', precision=2)
    table['Dec_dms'] = coords.dec.to_string(unit=u.degree, sep=':', precision=2)
    table.write('gaia_simbad.xml', format='votable', overwrite=True)
    return (table)