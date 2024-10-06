from astroquery.gaia import Gaia

def	get_table():
	"""
	Query the Gaia archive for all sources within a certain radius from the given point,
	which have parallax below the given limit (within 3 sigma),
	and save the result as a numpy zip archive.
	"""
	job = Gaia.launch_job(
		"SELECT TOP 10 "+
		"source_id, ra, dec, parallax, phot_g_mean_mag "+
		"FROM gaiadr3.gaia_source "+
		"WHERE phot_g_mean_mag < 6 "+
		"ORDER BY phot_g_mean_mag DESC;"
	)
	table = job.get_results()
	return(table)