import pandas as pd


def top_assigned_modem_distributor(df, top_n=10):
	"""
	top distributors assigned modems
	:param df: dataframe to analyze on
	:param top_n: top n distributors to be returned
	:return: list, count and percentage
	"""

	ag = df.groupby(['CUSTOMER_NAME'])['SERIAL_NO'].count()\
		.sort_values(ascending=False)\
		.reset_index(name='COUNT')\
		.head(top_n)
	return ag


def not_registered_modems(df):
	df_isnull = df.groupby(['CUSTOMER_NAME']) \
		.apply(lambda x: x.isnull().mean())['MSISDN_V']\
		.reset_index(name='NOT_REGISTERED_PERCENTAGE')

	df_all = df.groupby(['CUSTOMER_NAME'])['SERIAL_NO'].count()\
		.reset_index(name='MODEM_COUNT')

	merged_df = pd.merge(df_isnull, df_all, left_on='CUSTOMER_NAME', right_on='CUSTOMER_NAME', how='inner')

	return merged_df


def not_activated_for_n_years(sold_for_n_year=2):
	"""
	difference between sold_date and now for not registered modems
	:param sold_for_n_year: not sold after n year
	:return: list of modems
	"""
	pass


def stock_in_channel_count():
	"""
	count and percentage of not registered sold modems
	:return: count and percentage of not registered sold modems
	"""
	pass


def stock_in_channel_list():
	"""
	count and percentage of not registered sold modems
	:return: list of not registered sold modems
	"""
	pass


def number_of_stock_in_channel():
	pass


def corporate_modems_as_individual():
	"""
	number of corporate modems sold as individual
	:return: number of percentage of individual modems
	"""
	pass
