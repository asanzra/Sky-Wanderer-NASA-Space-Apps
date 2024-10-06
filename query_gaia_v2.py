from astroquery.gaia import Gaia

def	get_table(ra_exo, dec_exo, parallax_exo, num_stars, min_mag_p):
	job = Gaia.launch_job(
    "WITH cartesian_coords AS ( " +
    "SELECT " +
    "source_id, ra, dec, parallax, phot_g_mean_mag, " + 
    "(((cos(radians(ra)) * cos(radians(dec))) / parallax) - " + f"(cos(radians({ra_exo})) * cos(radians({dec_exo}))) / {parallax_exo}) AS x_rel,
        (((sin(radians(ra)) * cos(radians(dec))) / parallax) - (sin(radians({ra_exo})) * cos(radians({dec_exo}))) / {parallax_exo}) AS y_rel,
        (((sin(radians(dec))) / parallax) - (sin(radians({dec_exo}))) / {parallax_exo}) AS z_rel, " +
        "ABS(1 / parallax) AS dist_t " + 
    "FROM gaiadr3.gaia_source_lite" +
    ")" +
    f"SELECT TOP {num_stars} " +
            "source_id, ra, dec, parallax, phot_g_mean_mag, dist_t " +
        "FROM " +
            "cartesian_coords AS c " +
    "WHERE " +
        "x_rel + y_rel + z_rel != 0 AND " +
        f"(phot_g_mean_mag - 5 * LOG10 (dist_t / (SQRT(POWER(x_rel, 2) + POWER(y_rel, 2) + POWER(z_rel, 2))))) < {min_mag_p} " +
    "ORDER BY phot_g_mean_mag ASC "
	)
	table = job.get_results()
	table.write('gaia_stars.xml', format='votable')
	return(table)