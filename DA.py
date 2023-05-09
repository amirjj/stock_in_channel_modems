import pandas as pd
import datetime


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


def not_activated_for_n_years(df, sold_for_n_year=2):
	"""
	difference between sold_date and now for not registered modems
	:param sold_for_n_year: not sold after n year
	:return: list of modems
	"""
	# print(df.dtypes)
	df['DATE_CREATED'] = pd.to_datetime(df['DATE_CREATED'])
	# df['SERIAL_NO'] = df['SERIAL_NO'].astype('string')

	# today = datetime.datetime.now()
	# print(df[df['CUSTOMER_NAME'].eq('AZARAN')]['DATE_CREATED'])
	# print(today - df[df['CUSTOMER_NAME'].eq('AZARAN')]['DATE_CREATED'])
	# print(df.loc['2020-01-01':'2020-01-25'])
	older_df = df[df['DATE_CREATED'] < '2020-01-01']

	not_registered_list = not_registered_modems(older_df)

	return not_registered_list, older_df


def corporate_modems_as_individual(df):
	"""
	number of corporate modems sold as individual
	:return: number of percentage of individual modems
	"""

	df_corporate = df.groupby(['CUSTOMER_NAME']).apply(lambda x: x == 'B')['PROFILE_TYPE_V']\
		.reset_index(name='IS_CORPORATE')\
		.groupby('CUSTOMER_NAME')['IS_CORPORATE'].sum().reset_index(name='INDIVIDUAL_COUNT')

	df_individual = df.groupby(['CUSTOMER_NAME']).apply(lambda x: x == 'I')['PROFILE_TYPE_V'] \
		.reset_index(name='IS_INDIVIDUAL') \
		.groupby('CUSTOMER_NAME')['IS_INDIVIDUAL'].sum().reset_index(name='CORPORATE_COUNT')

	merged_df = pd.merge(df_corporate, df_individual, left_on='CUSTOMER_NAME', right_on='CUSTOMER_NAME', how='inner')

	return merged_df
